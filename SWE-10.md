# ViAble-SWE-10 — internal SWE benchmark (TRUE F2P, repro-based)

Protocol: task chi vao bank khi base-FAIL + gold-PASS (repro tay).
Khong dung file test goc cua repo (drift env) — moi task 1 repro 10 dong.

## Chay 1 task (GitHub Actions, docker)
`Actions > swe-lite-docker > Run workflow` voi:
`target_repo`, `commit`, `tests=test_repro_viable.py -q`,
`test_url=<raw repro>`, `patch_url` (trong = base; co = model/gold),
`extra_pip` (neu can), `run_id` rieng.
Doc artifact `score-<run_id>.json`: `verdict/apply/passed/failed`.

## Tasks

| # | id | repo | commit | repro | gold | pins |
|---|---|---|---|---|---|---|
| 1 | mime282 | lk-geimfari/mimesis | 6025cfc0 | repro_mime282.py | mime282-gold.diff | — |
| 2 | ela889 | elastic/elasticsearch-py | da2d5c46 | repro_elastic889.py | elastic889-gold.diff | — |
| 3 | swe168 | litestar-org/litestar | 7211dee1 | repro168.py | swe168-gold.diff | pydantic<2 httpx2 pytest-asyncio anyio trio freezegun pytest-mock requests |
| 4 | clk1400 | pallets/click | b24c51f3 | repro_click1400.py | click1400-gold.diff | — |
| 5 | clk1913 | pallets/click | b131f71d | repro_click1913.py | click1913-gold.diff | — |
| 6 | lite186 | litestar-org/litestar | 2f002e19 | repro_lite186.py | lite186-gold.diff | (same litestar pins) |
| 7 | clk1099 | pallets/click | 3e17a3d2 | repro_click1099.py | click1099-gold.diff | — |
| 8 | clk1329 | pallets/click | 0b1e32b0 | repro_click1329.py | click1329-gold.diff | — |
| 9 | clk2107 | pallets/click | 41f5b7a7 | repro_click2107.py | click2107-gold.diff | — |
| 10 | mime640 | lk-geimfari/mimesis | 4f15c215 | repro_mime640.py | mime640-gold.diff | — |

Raw base: `https://raw.githubusercontent.com/easportat2025-blip/viable-bench/main/runs/<file>`

## De mo ta ngan (issue -> cho can kiem)
1. **mime282** — `Numbers.primes()` tra ve so le thay vi so nguyen to. Repro: `primes(2,30) == [2,3,5,7,11,13,17,19,23,29]`.
2. **ela889** — `str(TransportError)` no khi error body la string (can `string indices must be integers`). Repro: 3-arg form, doi `not supported` trong str.
3. **swe168** — default exception handler thieu `status_code` trong content (schema bao co). Repro: goi handler, body phai co status_code 404.
4. **clk1400** — `open_file(atomic=True)` set perms 600, bo qua umask. Repro: file moi phai 0o100644.
5. **clk1913** — `flag_value=42` bi stringify thanh `'42'`. Repro: CliRunner `--answer` ra `42` (int).
6. **lite186** — `get_exception_handler` uu tien fallback 500 truoc MRO (subclass HTTPException bi bat nham). Repro: subclass → phai ve handler HTTPException.
7. **clk1099** — thieu type `click.DateTime`. Repro: `DateTime().convert("2021-01-02") == datetime(2021,1,2)`.
8. **clk1329** — khong phan biet default vs command-line (thieu `ParameterSource`). Repro: `get_parameter_source` → DEFAULT / COMMANDLINE.
9. **clk2107** — `open_file(Path("-"))` tao file ten `-` thay vi stdout. Repro: khong co file `-` nao duoc tao.
10. **mime640** — `Path.home()` thua trailing slash + logic platform cu. Repro: `Path(platform="linux").home() == "/home"`.

## Model scores (R1-agent, read-only era)
- mime282: PASS (idea dung, sua headers co hoc) · swe168: PASS dang gold-form (sua 1 char header)
- Con lai: chua cham (cho agent-vNext / R6-merged)
