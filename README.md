# Credit Risk: Give Me Some Credit

Predict which borrowers are likely to fall into serious financial distress in the next two years.

> Status: in progress. Results, limitations and reproduction steps will be added as the project develops.

## The problem

Banks decide who gets a loan and how much credit to give. A wrong "yes" means lending to someone who won't pay back. A wrong "no" means turning away a good customer.

This project builds a **credit scoring model**: given a borrower's credit history and finances, estimate the **probability** that they will become seriously delinquent (90+ days late on a payment) within two years.

## The Kaggle competition

- **Competition:** [Give Me Some Credit](https://www.kaggle.com/competitions/GiveMeSomeCredit)
- **Task:** binary classification. Predict a probability for each borrower, not just yes/no.
- **Target:** `SeriousDlqin2yrs` = 1 if the person was 90 days or more past due in the next two years, else 0.
- **Kaggle metric:** AUC (area under the ROC curve). It measures how well the model *ranks* risky borrowers above safe ones.

## The data

150,000 borrowers in `cs-training.csv`, with 10 features:

| Feature | Meaning |
|---|---|
| `RevolvingUtilizationOfUnsecuredLines` | Credit card and personal credit line balance divided by credit limits |
| `age` | Borrower age in years |
| `NumberOfTime30-59DaysPastDueNotWorse` | Times 30 to 59 days late in the last 2 years |
| `NumberOfTime60-89DaysPastDueNotWorse` | Times 60 to 89 days late in the last 2 years |
| `NumberOfTimes90DaysLate` | Times 90+ days late |
| `DebtRatio` | Monthly debt payments and living costs divided by monthly gross income |
| `MonthlyIncome` | Monthly income |
| `NumberOfOpenCreditLinesAndLoans` | Open loans (car, mortgage) and credit lines (credit cards) |
| `NumberRealEstateLoansOrLines` | Mortgages and real estate loans, including home equity lines |
| `NumberOfDependents` | Dependents in the family, excluding the borrower |

`cs-test.csv` has no target, because it was only used for Kaggle submissions. So my own holdout set comes from a stratified split of `cs-training.csv`.

The data is not in this repo. Download it from the competition page into `data/raw/`.

## My objective

Go beyond the Kaggle score and build a model a bank could actually use:

1. **Explore the data:** class imbalance, missing values, impossible values.
2. **Start from a baseline:** a trivial model, then logistic regression.
3. **Try stronger models** (tree-based), compared with stratified cross-validation, and keep the simplest one that does the job.
4. **Evaluate honestly:** AUC and precision-recall (the classes are imbalanced, so accuracy is misleading), a calibration check, and uncertainty in every result.
5. **Choose a decision threshold** from the cost of each error (approving a defaulter vs. rejecting a good customer), not the default 0.5.
6. **Explain the model:** which factors drive risk, and why.

## Project structure

```
data/raw/      original Kaggle files (not committed)
notebooks/     analysis, numbered in order (01_eda, 02_baseline, ...)
src/           reusable Python code imported by the notebooks
reports/       figures and results summaries
```
