# 📊 Student Performance Analysis

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA)** of student academic performance data to understand how various factors such as **study hours, sleep patterns, attendance, and screen time** influence students' final grades and overall improvement.

The goal is to extract meaningful insights from data using **Python-based data analysis and visualization techniques**, making this project suitable for beginners as well as for showcasing analytical skills on GitHub and LinkedIn.

---

## 🎯 Objectives

* Clean and preprocess raw student performance data
* Handle missing values and duplicate records
* Perform exploratory data analysis (EDA)
* Analyze correlations between academic and lifestyle factors
* Engineer new features such as **grade improvement** and **study-to-sleep ratio**
* Visualize insights using clear and meaningful plots

---

## 🧠 Key Insights Explored

* Relationship between **study hours and final grades**
* Impact of **sleep hours on grade improvement**
* Correlation between academic performance and lifestyle habits
* Distribution of student grade improvement

---

## 🛠 Tools & Technologies Used

* **Python**
* **Pandas** – data manipulation and cleaning
* **NumPy** – numerical operations
* **Matplotlib** – basic plotting
* **Seaborn** – advanced data visualization

---

## 🗂 Dataset Description

The dataset (`student_performance.csv`) includes the following columns:

* `Student_ID`
* `Age`
* `Gender`
* `Attendance`
* `Study_Hours`
* `Sleep_Hours`
* `Screen_Hours`
* `Previous_Grade`
* `Final_Grade`

---

## 🧪 Data Cleaning & Preprocessing

* Removed duplicate records
* Handled missing numeric values using **median imputation**
* Handled categorical missing values (`Gender`) with an `Unknown` category
* Converted categorical variables into numerical form

---

## ⚙️ Feature Engineering

New features created for deeper analysis:

* **Improvement** = `Final_Grade - Previous_Grade`
* **Study-to-Sleep Ratio** = `Study_Hours / Sleep_Hours`

These features help measure student growth and balance between effort and rest.

---

## 📈 Visualizations Included

* Correlation heatmap
* Scatter plot: Sleep Hours vs Final Grade
* Scatter + regression plot: Sleep Hours vs Grade Improvement
* Scatter plot: Study Hours vs Final Grade
* Distribution plots for grade improvement

Each visualization is designed to answer a specific analytical question.


<img width="771" height="632" alt="image" src="https://github.com/user-attachments/assets/cc845d92-c492-4397-847a-73e2b0143bea" />
<img width="764" height="580" alt="image" src="https://github.com/user-attachments/assets/22da7b7d-d7e1-430d-b4c5-05b653095bf3" />
<img width="858" height="572" alt="image" src="https://github.com/user-attachments/assets/8e5e4111-7dcc-40de-b0bb-f40215039b35" />
<img width="840" height="575" alt="image" src="https://github.com/user-attachments/assets/2392b7a4-2ead-40b0-b6e7-c4824631c2f8" />

---

## 🚀 How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/piyushp69/student-performance-analysis.git
   ```
2. Navigate to the project directory
3. Install required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
4. Run the Python script or Jupyter Notebook

---

## 📌 Project Highlights

* Beginner-friendly EDA project
* Real-world academic dataset
* Clean, interpretable visualizations
* Strong focus on insight extraction

---

## 🔮 Future Improvements

* Add machine learning models to predict final grades
* Perform feature importance analysis
* Expand dataset with more behavioral factors
* Deploy insights using a dashboard (Power BI / Tableau)

---

## 📬 Contact

**Piyush Priyanshu**
B.Tech Student | Aspiring Data Analyst / ML Engineer

Feel free to connect on LinkedIn or explore my other projects!

---

⭐ If you found this project useful, consider giving it a star!

