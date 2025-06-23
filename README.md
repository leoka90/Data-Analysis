# 🩺 Medical Appointment No-Shows - Data Cleaning

## 📄 Dataset
This dataset contains information about over 100k medical appointments in Brazil and whether patients showed up or not.  
Source: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

---

## ✅ Steps Performed

1. **Column Standardization**
   - Renamed all columns to lowercase and replaced hyphens (`-`) with underscores for Python compatibility.

2. **Data Type Conversion**
   - Converted `scheduledday` and `appointmentday` columns to `datetime` format using `pd.to_datetime()`.

3. **Duplicate Handling**
   - Removed duplicate rows using `drop_duplicates()`.

4. **Missing Values**
   - Checked for nulls using `isnull().sum()` — no missing values found.

5. **Visual Exploratory Analysis**
   - Plotted distributions for each column:
     - `histplot` used for numerical and datetime features.
     - `countplot` used for categorical features.

6. **Outlier Detection and Removal**
   - Applied the **IQR method** on the `age` column.
   - Removed entries with extremely low or high ages (e.g., negative or >100).

7. **Boxplot Analysis**
   - Visualized key numeric features before and after outlier removal.

8. **Exported Cleaned Dataset**
   - Saved final cleaned dataset as:  
     ✅ `cleaned_medical_appointments.csv`

---

## 📁 Files in Repo

- `task1_cleaning.py` — Python script for cleaning and preprocessing  
- `cleaned_medical_appointments.csv` — Final cleaned dataset  
- `README.md` — Summary of the cleaning process

---

## 🧠 Learning Outcomes

- Used **Pandas** for robust data wrangling
- Improved familiarity with **date conversion**, **column cleaning**, **IQR-based outlier removal**
- Built confidence in preparing datasets for analysis or machine learning

---