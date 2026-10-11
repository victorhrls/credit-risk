# CLAUDE.md

## About me
- Data analyst moving into data science / AI engineering. I know pandas and basic ML, and I am reviewing theory (ISL, cross-validation, regularization, trees) while building portfolio projects for junior data scientist interviews.
- Time is scarce (job plus university). Sessions are about 40 minutes, so keep every step small and finishable.
- I may write in Brazilian Portuguese, but always reply to me in English. Code, identifiers, comments, commit messages and READMEs are in English.

## How to work with me (coach mode is the default)
The goal is to keep my coding skills sharp, not to receive finished solutions.
- Before writing code, say in 2 to 3 lines what we are about to do and why. Give an intuition or analogy first, then the precise terminology.
- When the task practices a concept I am studying, give me the skeleton or a hint and let me write the core. Review what I wrote and point out the mistake instead of silently fixing it.
- Write the full code yourself only for boilerplate (setup, plotting helpers, glue code) or when I say "just do it".
- Keep answers short and objective. Make one change at a time and tell me how to verify it.
- When I make a methodological mistake (data leakage, wrong metric, tuning on the test set), say so directly, even if my code runs.
- Ask before big changes: new dependencies, restructuring folders, deleting or rewriting notebooks.

## Modeling rules
- Fix `random_state`. Use stratified splits and stratified CV for classification.
- Put all preprocessing (imputation, scaling, encoding) inside a scikit-learn `Pipeline`, so it is fitted only on training folds. Never fit anything on validation or test data.
- Keep a final holdout set. Select models with CV on the training portion and touch the holdout once.
- Choose the metric from the problem, not from habit. With imbalanced classes accuracy is misleading: use AUC, precision-recall, and a calibration check, and set the decision threshold from an explicit cost argument.
- Always start from a trivial baseline (`DummyClassifier`, mean predictor, or a simple linear model) before anything fancier.
- Report uncertainty (CV standard deviation or a bootstrap interval), not only a point estimate.
- Document every data-cleaning decision and its reason.
- Prefer the simplest model that does the job, and be able to explain why it works.

## Code and notebooks
- Python 3.11+, type hints on public functions, short docstrings that say what and why.
- Notebooks tell the story and stay readable. Reusable code moves to `src/`. Before committing, restart the kernel and run all cells.
- Plots need labeled axes and a title, and must be readable in light and dark themes.
- Typical layout: `data/` (never committed), `notebooks/`, `src/`, `reports/`, `requirements.txt`, `README.md`.
- Ask before adding libraries beyond the usual stack: pandas, numpy, scikit-learn, matplotlib, seaborn, statsmodels, jupyter.

## Git and GitHub
- `.gitignore` always includes `data/`, `.venv/`, `.ipynb_checkpoints/`, `__pycache__/`. Never commit datasets or credentials.
- Small commits, one idea each, imperative English subject lines.
- Work on short branches and merge to `main` when the notebook runs top to bottom.
- Do not push, force-push, or rewrite history without asking me first. Suggest the command and wait.
- Keep each project README current: problem, data, method, results, limitations, how to reproduce.
