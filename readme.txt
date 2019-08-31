Loan Delinquency Prediction

I solved this problem using Machine Learning with XGBRegressor
initially i load all the dataset to the dataframe and done some preprocessing in the records.
preprocessing steps:
i Convert first_payment_date to month and day of year saperate numeric column (feature engineering)
Simliarly i converted origination_date to month and day of year saperate numeric column (feature engineering)
additionally is created a saperate column for saving difference of origination_day and first_payment_day
then i dropped fields like loan_id, origination_date, first_payment_date etc
then i combained both train and text dataset to find deal with catogerical data.
then i created a lmplot visuvalization to remove the outliers rows from unpaid_principal_bal, m12, and m13
then i created correlation heat map to find all most correlated fields and i formed a new dataframe with most corelated field
changed all the category fields to pandas dummies
finally i used XGBRegressor to train and predict the loan Delinquency

Software Requirement

Pytorch, numpy, pandas, torchvision, sklearn, scipy, matplotlib, seaborn

Installation.

You can install all the softwares saperately or just run this command with requirements.txt given in the zip

pip install -r requirements.txt

Finally create a folder name "save" in the same place where put the notepad file for saving the model temporarily
