# git-lab

A tiny practice project to learn the Git and GitHub workflow
(branch, pull request, review, merge).
It computes consumption from cumulative meter readings.

## Files

| File | Purpose |
| --- | --- |
| `consumption.py` | Reads `readings.csv` and prints the consumption per PDR and period |
| `readings.csv` | Sample cumulative readings for three PDRs |
| `tests/test_consumption.py` | One basic test (run with `python -m pytest`, optional) |
## Usage

```bash
python consumption.py
```