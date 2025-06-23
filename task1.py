import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('KaggleV2-May-2016.csv')

# Initial inspection
print(df.info())
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert date columns to datetime 
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Plot histograms (handle types accordingly)
cols_to_plot = [
    'PatientId', 'AppointmentID', 'Gender', 'ScheduledDay', 'AppointmentDay',
    'Age', 'Neighbourhood', 'Scholarship', 'Hipertension', 'Diabetes',
    'Alcoholism', 'Handcap', 'SMS_received', 'No-show'
]

for col in cols_to_plot:
    plt.figure(figsize=(8, 4))
    
    if pd.api.types.is_numeric_dtype(df[col]):
        sns.histplot(df[col], kde=False, bins=30)
    elif pd.api.types.is_datetime64_any_dtype(df[col]):
        sns.histplot(df[col].dt.date, bins=30)  # Use .dt.date for better aggregation
    else:
        sns.countplot(x=df[col], order=df[col].value_counts().index)

    plt.title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

numeric_cols = ['Age', 'Scholarship', 'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'SMS_received']

# Boxplot before removing outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplot Before Outlier Removal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Remove outliers using IQR
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

df_clean = remove_outliers_iqr(df, ['Age']) 

# Boxplot after removing outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_clean[numeric_cols])
plt.title("Boxplot After Outlier Removal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()