# Narrative Review — Imputation for Multivariate Time Series in Air Quality

**Working title:** *From Statistical Missing-Data Inference to Deep Generative Imputation for Multivariate Time Series: A Narrative Review*

**Authors:** Valeria García Hernández, Fernando

**Supervisors:** Raúl Gómez Muñoz, Blanca Rosa Ruiz Hernández

This repository contains the research artifacts for a narrative review on imputation methods for multivariate time series, with a focus on air pollution monitoring data from SIMA (Sistema Integral de Monitoreo Ambiental) in Monterrey, Mexico.

## Repository structure

```
.
├── PLAN.md                          # Project plan, timeline, and task tracking
├── search_log.csv                   # Traceable log of all literature searches (OpenAlex)
├── Matriz Extracción Literatura*.csv # Literature extraction matrix (104 references, 16 columns)
└── Notebooklm/
    ├── TRIAGE_WORKFLOW.md           # Paper triage process using NotebookLM
    ├── candidates_veredict.csv      # ADD/SKIP verdicts for candidate papers
    ├── peer-review-evaluation.md    # Simulated peer review of the collection
    ├── research-report-bridging-missing-data.md   # Gap analysis: MNAR bridge (2018–2025)
    └── classical-theoretical-foundations.md        # Gap analysis: pre-2018 MNAR foundations
```

## Narrative arc

The review traces the evolution of imputation methods through five eras:

1. **Foundations** — Rubin's missing-data framework, EM algorithm, multiple imputation
2. **Classical approaches** — Interpolation, regression, KNN, Kalman filtering
3. **Deep learning** — GANs (GAIN), RNNs (BRITS), transformers (SAITS), diffusion (CSDI)
4. **Evaluation** — RMSE vs. inferential validity, uncertainty calibration
5. **Open challenges** — MNAR in sensor data, burst missingness, the theory-practice gap

## Related repositories

- [PaperConnect](https://github.com/Krul-dev/PaperConnect) — Citation graph visualization tool built for this project (interactive graph + timeline view, OpenAlex API)

## Tools used

- **Zotero** — Reference management
- **OpenAlex API** — Citation lookup and paper search
- **NotebookLM** — Literature triage and gap analysis
- **Claude Code** — Research assistance and tooling
