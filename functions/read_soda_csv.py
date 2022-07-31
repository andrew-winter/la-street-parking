# %%
import datetime
import pandas as pd

# function to read through SODA (Socrata Open Data API) endpoint in csv
# takes an endpoint and returns a dataframe

def read_soda_csv(
    endpoint='https://data.lacity.org/resource/e7h6-4a3e.csv?'):
        df = pd.read_csv(endpoint)
        df['dt_mod'] = datetime.datetime.now()
        return df

if __name__ == "__main__":
    print(read_soda_csv())
