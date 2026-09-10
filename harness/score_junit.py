"""Parse pytest junit.xml -> compact score JSON for ViAble bench."""
import argparse
import json
import xml.etree.ElementTree as ET


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("junit", help="path to junit.xml")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--apply-status", default="no-patch")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    tree = ET.parse(args.junit)
    root = tree.getroot()
    suite = root if root.tag == "testsuite" else root.find("testsuite")

    passed = failed = error = skipped = 0
    failed_names = []
    for tc in suite.iter("testcase"):
        name = tc.get("classname", "") + "::" + tc.get("name", "")
        if tc.find("failure") is not None:
            failed += 1
            failed_names.append(name)
        elif tc.find("error") is not None:
            error += 1
            failed_names.append(name)
        elif tc.find("skipped") is not None:
            skipped += 1
        else:
            passed += 1

    total = passed + failed + error
    if args.apply_status == "rejected":
        verdict = "patch-rejected"
    else:
        verdict = "ok" if total else "no-tests-collected"
    score = {
        "run_id": args.run_id,
        "apply": args.apply_status,
        "verdict": verdict,
        "passed": passed,
        "failed": failed,
        "error": error,
        "skipped": skipped,
        "total": total,
        "pass_rate": round(passed / total, 4) if total else 0.0,
        "failed_names": failed_names[:20],
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(score, f, indent=2)
    print(json.dumps(score, indent=2))


if __name__ == "__main__":
    main()
