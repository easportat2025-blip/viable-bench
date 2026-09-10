# viable-bench (private)

GPU farm (Kaggle/Colab) sinh outputs/patch -> GitHub Actions chấm bằng docker -> JSON điểm.

## Chay thu cong (smoke, khong patch)

Actions > swe-lite-docker > Run workflow >
`target_repo=https://github.com/pytest-dev/pytest.git`,
`commit=<sha>`, `patch_url` bo trong, `tests=<node>`, `run_id=smoke-001`.

## Chay co patch cua model

1. Kernel sinh `model.diff` (unified diff, `git diff` format).
2. Upload diff dau do lay raw URL (gist / dataset / release asset).
3. Dispatch workflow voi `patch_url=<raw url>`.
4. Doc artifact `score-<run_id>.json`: `passed/failed/pass_rate`.

## Quy uoc patch

- Unified diff ap dung duoc bang `git apply` tu repo root.
- Chi cham test trong `tests` (F2P/P2P theo SWE-bench).
