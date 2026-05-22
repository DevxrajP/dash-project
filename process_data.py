import pandas as pd
import glob

files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Remove $ symbol and convert price
    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

    # Create sales column
    df["sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["sales", "date", "region"]]

    all_data.append(df)

# Combine all CSV files
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("formatted_output.csv", index=False)

print("Processing complete!")