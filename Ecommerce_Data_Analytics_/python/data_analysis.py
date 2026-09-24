import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\DELL\Desktop\Ecommerce_Data_Analytics\dataset\Sample - Superstore.csv",
    encoding="latin1"
)

# Convert date columns
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Create useful date columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Year_Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Display information
print("Dataset shape:", df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Save cleaned dataset
df.to_csv(
    r"C:\Users\DELL\Desktop\Ecommerce_Data_Analytics\dataset\cleaned_sales.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")