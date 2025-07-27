from load_data import load_dataset
from preprocess import preprocess_dataset

df = load_dataset("Training Dataset.csv")
text_data = preprocess_dataset(df)

print("First processed row:\n")
print(text_data[0])
