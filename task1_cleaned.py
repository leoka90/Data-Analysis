import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('KaggleV2-May-2016.csv')

# Initial inspection
print("=== Dataset Info ===")
print(df.info())
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns to datetime
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace('-', '_')

# Quick histogram / count plot visualizations
cols_to_plot = [
    'patientid', 'appointmentid', 'gender', 'scheduledday', 'appointmentday',
    'age', 'neighbourhood', 'scholarship', 'hipertension', 'diabetes',
    'alcoholism', 'handcap', 'sms_received', 'no_show'
]

for col in cols_to_plot:
    plt.figure(figsize=(8, 4))
    
    if pd.api.types.is_numeric_dtype(df[col]):
        sns.histplot(df[col], kde=False, bins=30)
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        sns.histplot(df[col].dt.date, bins=30)
    else:
        sns.countplot(x=df[col], order=df[col].value_counts().index)
    
    plt.title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Select numeric columns for boxplot analysis
numeric_cols = ['age', 'scholarship', 'hipertension', 'diabetes', 'alcoholism', 'handcap', 'sms_received']

# Boxplot before outlier removal
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplot Before Outlier Removal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Remove outliers using IQR method
def remove_outliers_iqr(data, columns):
    cleaned_data = data.copy()
    for col in columns:
        Q1 = cleaned_data[col].quantile(0.25)
        Q3 = cleaned_data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        cleaned_data = cleaned_data[(cleaned_data[col] >= lower) & (cleaned_data[col] <= upper)]
    return cleaned_data

df_clean = remove_outliers_iqr(df, ['age'])  

# Boxplot after outlier removal
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean[numeric_cols])
plt.title("Boxplot After Outlier Removal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Show the cleaned dataset (first 10 rows)
print("\n=== Cleaned Dataset (First 10 Rows) ===")
print(df_clean.head(10))


print("\n=== Shape of Cleaned Dataset ===")
print(df_clean.shape)

print("\n=== Summary Statistics ===")
print(df_clean.describe())

df_clean.to_csv('cleaned_medical_appointments.csv', index=False)
print("Cleaned dataset saved as 'cleaned_medical_appointments.csv'")
