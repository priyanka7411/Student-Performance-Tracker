# src/utils.py

import pandas as pd
import json
import pickle

# Load data from CSV
def load_data(file_path):
    return pd.read_csv(file_path)

# Save data to CSV
def save_to_csv(df, file_path):
    df.to_csv(file_path, index=False)

# Save data to JSON
def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Save data to Pickle
def save_to_pickle(data, file_path):
    with open(file_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)
