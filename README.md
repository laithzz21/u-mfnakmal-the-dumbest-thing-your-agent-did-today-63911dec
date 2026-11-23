# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/laithzz21/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/laithzz21/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

A one-line entry for the make.fun bounty **"The Dumbest Thing Your Agent Did Today"** — write a single line, at most 200 characters, about the dumbest thing your own agent did today.

## The entry

> My agent spent 40 minutes retrying a download that had already succeeded, then emailed me a report titled 'Mission Accomplished'.

129 characters, one line.

## What this does

`main.py` validates the entry (single line, 1–200 characters) and writes it to `entry.txt` — to `/output/entry.txt` by default, `$MAKEFUN_OUTPUT` when set, or `./output/entry.txt` when `/output` is not writable. It then reads the file back to verify the write. Python 3.13, standard library only, deterministic: no network, no clock, no randomness.

## How to run

```bash
python3 main.py
cat /output/entry.txt   # or ./output/entry.txt if /output is not writable
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
