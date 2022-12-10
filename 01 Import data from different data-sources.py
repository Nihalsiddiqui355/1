import pandas as pd
data = pd.read_csv("here file path what we have given in the exam")
d = pd.read_csv("Income_data - Income_data.csv")
data.head()

# Q2. Import file from http://winterolympicsmedals.com/medals.csv and print the last 5 rows.

medal = pd.reas_csv("Use here in the exam link and path file")
medal.tail()

# Q3 Import text file SampleData.

SD = pd.read_csv("Use here in the exam link and path file")
print(SD)

# Q4. Import HTML file http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/.

des = pd.read_html(
    "http://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/")
print(des)

# Q5. Import Data 1 spreadsheet from https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls except the first two rows.

pd.read_excel("D:\RBRTed.xls", sheet_name='Data 1', skiprows=2)
