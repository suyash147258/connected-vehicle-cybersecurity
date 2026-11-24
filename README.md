# Connected Vehicle Cybersecurity — Academic Article

This repository contains a LaTeX research-style article and a small offline Python demonstration for the course **Cybersecurity for Connected Vehicles**.

## Files

- `main.tex` — article source (two-column academic layout)
- `references.bib` — bibliography database
- `src/can_log_checker.py` — offline CSV sanity checker for CAN logs
- `data/sample_can_log.csv` — synthetic demonstration data

## Build in Overleaf

1. Create a blank project in Overleaf.
2. Upload `main.tex` and `references.bib` (or upload the ZIP).
3. Set `main.tex` as the main document.
4. Select pdfLaTeX.
5. Recompile. If references do not appear on the first run, compile again.

## Run the offline demonstration

Requires Python 3.

```bash
python src/can_log_checker.py data/sample_can_log.csv
```

Optional threshold and allowlist:

```bash
python src/can_log_checker.py data/sample_can_log.csv --max-per-second 5 --allow 0x100,0x101,0x120
```

The dataset is synthetic. The script reads a CSV only; it does not connect to a vehicle, send CAN frames, or control any vehicle function. Thresholds and allowlists are illustrative and must be derived from an authorized test environment.

## Important academic note

This is a draft starting point. Add your name, institution, course details, and any faculty-specific formatting requirements. Verify every bibliography entry and adapt the discussion to your instructor's rubric before submission. The article does not claim that the demonstration is a complete automotive IDS or that it has measured detection accuracy.
