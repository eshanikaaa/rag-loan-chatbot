import pandas as pd

def load_dataset(csv_path="Training Dataset.csv"):
    df = pd.read_csv(csv_path)
    print("Dataset loaded successfully. Shape:", df.shape)

    # Drop rows where Loan_Status is missing
    df = df.dropna(subset=["Loan_Status"])
    return df
