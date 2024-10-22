#DATA SCIENCE CLASS
import pandas as pd

SURVEY = {
    'Name' : ['Ugoeze', 'Adaeze', 'Odogwu'],
    'Age' : [16, 20, 18],
    'Favourite Color' : ['Purple', 'Blue', 'Red']
}
df_survey = pd.DataFrame(SURVEY)
print(df_survey)