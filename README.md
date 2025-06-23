# Medical Appointment No-Shows - Data Cleaning

## 📄 Dataset
This dataset contains information about medical appointments in Brazil and whether or not patients showed up for their appointments.

Original dataset source: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

---



### ✅ Steps Performed:
1. **Column Standardization**
   - Renamed all columns to lowercase and replaced spaces with underscores.

2. **Data Type Conversion**
   - Converted `scheduledday` and `appointmentday` to `datetime` format.

3. **Duplicate Check**
   - No duplicate rows found.

4. **Missing Values**
   - No missing values present in the dataset.

5. **Text Standardization**
   - Standardized values in `gender` (e.g., "m" → "M") and `no-show` (e.g., "no " → "No").

6. **Outlier Removal**
   - Removed outliers from the `age` column using the IQR method.
   - This eliminated extreme values like negative ages or unrealistically high entries.

7. **Exported Cleaned Data**
   - Saved cleaned dataset as `medical_appointments_cleaned.csv`.

---

## 📁 Files in Repo
- `task1_cleaning.py` — Full Python script used for cleaning and preprocessing
- `medical_appointments_cleaned.csv` — Final cleaned dataset
- `README.md` — Summary of what was done

---

## 🧠 Learning Outcomes
- Practical experience with Pandas for data cleaning
- Hands-on understanding of missing value handling, duplicates, standardization, and outlier removal
- Improved data quality for further analysis or modeling

---

