import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv("real_state_scrapping\\training_site_laptops.csv")

def inspect_data(df):
    print("\nData Overview:")
    print(df.info())
    print("\nFirst Few Rows:")
    print(df.head())

inspect_data(df)

# cleaning the data
def clean_data(df):
    print("\nHandling Missing Data...")
    # replace invalid values with nan (not a number)
    df.replace({'-':np.nan, 'N/A': np.nan, '':np.nan}, inplace=True)

    # drop rows with missing essential values
    df.dropna(subset=["Title", "Price", "Description", "Reviews", "Link"], inplace=True)

    # reset index
    df.reset_index(drop=True, inplace=True)

    print(f"Cleaned Data: {len(df)} rows remaining.")

    return df

df = clean_data(df)

