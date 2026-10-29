# 📊 Employee Attendance Analytics Dashboard
> **An End-to-End Workforce Intelligence, Attendance Analytics & Performance Evaluation System**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.x-013243.svg)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.x-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c.svg)](https://matplotlib.org/)
[![OpenPyXL](https://img.shields.io/badge/Excel-Dashboard-217346.svg)](https://openpyxl.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Project Overview

The **Employee Attendance Analytics Dashboard** is an enterprise-grade analytics solution built to evaluate workforce attendance patterns, detect absenteeism trends, analyze overtime distribution, and compute department-level productivity benchmarks.

This project covers all fundamental and advanced requirements across **Python**, **NumPy**, **Pandas**, **Matplotlib**, and **Dashboard Design (Interactive Python GUI + Styled Multi-Sheet Excel Dashboard)**.

---

## 🛠️ Complete Technology Structure & Requirement Mapping

Every requirement requested in your curriculum has been implemented and organized into clean, modular code:

| Category | Topics Covered | Implementation File & Details |
| :--- | :--- | :--- |
| **Python** | • Variables, conditions, loops<br>• Functions & type hints<br>• List, Tuple, Set, Dictionary<br>• File handling (Read/Write) | [`src/data_generator.py`](src/data_generator.py), [`main.py`](main.py)<br>Generates structured logs, uses Sets for unique employee IDs, Dictionaries for role mappings, Tuples for shift rules, and writes raw audit logs. |
| **NumPy** | • 1D/2D arrays<br>• Indexing & slicing<br>• Statistical operations<br>• Mathematical operations<br>• Reshaping | [`src/numpy_analytics.py`](src/numpy_analytics.py)<br>1D/2D attendance matrices, Boolean masks, Mean/Median/Std/IQR/Percentiles, Vectorized overtime calculations, Dot product overtime payouts, Array reshaping into `(4, 5)` weekly grids. |
| **Pandas** | • DataFrame / Series<br>• CSV/Excel reading<br>• Data cleaning<br>• Filtering & Sorting<br>• GroupBy & Aggregation<br>• Missing-value handling<br>• Merge / Join<br>• Basic statistics | [`src/pandas_analytics.py`](src/pandas_analytics.py)<br>Reads CSV and Excel, string standardization, missing-value imputation (`fillna`/`isna`), `pd.merge()` on `Employee_ID`, multi-level aggregations (`.agg()`), `.describe()`, and `.corr()`. |
| **Visualization (Matplotlib)** | • Bar chart<br>• Line chart<br>• Pie / Donut chart<br>• Histogram<br>• Scatter plot<br>• Composite Master Dashboard | [`src/visualizer.py`](src/visualizer.py)<br>Generates 6 publication-ready charts (Department Bar, Monthly Line with Moving Average, Status Donut, Work Hours Histogram with Mean line, Scatter Plot with regression trendline, and 6-in-1 Executive Master Dashboard). |
| **Dashboard** | • Excel Dashboard<br>• Python Desktop Dashboard<br>• Summary tables<br>• Monthly/yearly comparisons | [`src/excel_dashboard.py`](src/excel_dashboard.py), [`src/gui_dashboard.py`](src/gui_dashboard.py)<br>**1. Excel Dashboard**: Styled KPI cards, Department breakdown, Monthly trend table, embedded native Excel Bar & Line charts.<br>**2. Python Desktop GUI**: Interactive Tkinter + Matplotlib dashboard with dynamic department filtering, interactive charts, and Treeview tables. |

---

## 📂 Project Architecture & Directory Structure

```text
Employee_Attendance_Analytics/
├── data/                                    # Generated datasets
│   ├── employees.csv                        # Employee master demographics
│   ├── attendance_logs.csv                  # 6,600+ daily attendance records
│   ├── raw_attendance.xlsx                  # Multi-sheet Excel dataset
│   └── sample_audit_log.txt                 # Raw text audit logs
├── outputs/                                 # Analytics outputs & reports
│   ├── charts/                              # High-resolution charts (PNG)
│   │   ├── bar_department_metrics.png       # Department attendance & overtime
│   │   ├── line_monthly_trends.png          # Monthly trend & 7-day moving avg
│   │   ├── pie_status_distribution.png      # Status breakdown donut chart
│   │   ├── histogram_work_hours.png         # Shift hours distribution
│   │   ├── scatter_hours_vs_overtime.png    # Work hours vs overtime correlation
│   │   └── attendance_analytics_master_dashboard.png # 6-in-1 composite dashboard
│   ├── Employee_Attendance_Dashboard.xlsx   # Styled corporate Excel dashboard
│   └── executive_attendance_summary.txt     # Executive summary report
├── src/                                     # Core modular Python packages
│   ├── __init__.py                          # Package identifier
│   ├── data_generator.py                    # Python data structures & file I/O
│   ├── numpy_analytics.py                   # Complete NumPy operations suite
│   ├── pandas_analytics.py                  # Complete Pandas analytics pipeline
│   ├── visualizer.py                        # Matplotlib visualizations suite
│   ├── excel_dashboard.py                   # Automated OpenPyXL Excel dashboard
│   └── gui_dashboard.py                     # Interactive Tkinter desktop GUI
├── main.py                                  # Master pipeline runner & CLI
├── run_pipeline.bat                         # 1-Click launcher for full analytics
├── launch_gui_dashboard.bat                 # 1-Click launcher for Desktop GUI
├── requirements.txt                         # Project dependencies
├── .gitignore                               # Git ignore configuration
└── README.md                                # Comprehensive documentation
```

---

## 🚀 How to Run the Project

### Prerequisites
Make sure Python 3.10+ is installed on your system.

### Option 1: 1-Click Execution (Windows)
Double-click either of the batch files in the project folder:
* **`run_pipeline.bat`**: Runs the entire data cleaning, NumPy analysis, chart generation, and Excel dashboard creation.
* **`launch_gui_dashboard.bat`**: Launches the interactive Desktop GUI dashboard directly.

### Option 2: Command Line Execution (PowerShell or Terminal)

1. Open PowerShell / Command Prompt and navigate to the project directory:
   ```powershell
   cd Employee_Attendance_Analytics
   ```

2. Run the complete end-to-end pipeline:
   ```powershell
   python main.py
   ```

3. Launch the Interactive Desktop GUI Dashboard:
   ```powershell
   python main.py --gui
   ```

4. Generate only the styled Excel Dashboard:
   ```powershell
   python main.py --excel
   ```

5. Generate only the Matplotlib Visualizations:
   ```powershell
   python main.py --visuals
   ```

---

## 📈 Detailed Breakdown of Analytics Deliverables

### 1. NumPy Deep-Dive Analytics (`src/numpy_analytics.py`)
* **1D & 2D Arrays**: Daily work hours converted to 1D vector; `(50 employees x 132 days)` 2D attendance matrix.
* **Statistical Operations**: Mean ($6.36$h), Median ($7.79$h), Standard Deviation ($3.13$h), Variance ($9.81$), $Q_1$, $Q_2$, $Q_3$, and Interquartile Range ($3.87$h).
* **Indexing & Slicing**: Sub-matrix slicing (`[:5, :10]`), step-slicing (`[::2, ::5]`), and Boolean masking (`hours > 8.0`).
* **Mathematical Operations**: Vectorized overtime calculation (`np.maximum(0, hours - 8.0)`), matrix dot-product for overtime financial liability calculations (₹850,000+ computed automatically).
* **Reshaping**: Converting flat 20-day vectors into `(4, 5)` (4 weeks x 5 days) weekly grids, and matrix transposition (`(132, 50)`).

### 2. Pandas Analytics Engine (`src/pandas_analytics.py`)
* **Data Cleaning & Standardization**: String whitespace trimming, title casing, and department name harmonization.
* **Missing Value Imputation**: `df.isna().sum()`, conditional imputation (absent records filled with 0.0, present records imputed with category median), invalid negative hours correction.
* **Merge / Join**: Left merge between `attendance_logs` and `employee_master` on `Employee_ID`.
* **GroupBy & Aggregation**: Department-wise and Monthly summaries computing workforce count, total overtime, days worked, and attendance percentage.
* **Sorting & Filtering**: Performance scorecard sorted by attendance rate descending, multi-level filtering by department and month.

### 3. Matplotlib Visualizations (`src/visualizer.py`)
1. **Department Bar Chart** (`bar_department_metrics.png`): Dual-axis bar chart comparing Attendance % against average overtime per department.
2. **Monthly Trend Line Chart** (`line_monthly_trends.png`): 6-month attendance trajectory with target benchmark ($85\%$) and 7-day rolling moving average.
3. **Status Donut Pie Chart** (`pie_status_distribution.png`): Attendance status split (Present, WFH, Late, Half-Day, On Leave, Absent).
4. **Work Hours Histogram** (`histogram_work_hours.png`): Distribution of daily hours worked with Mean ($6.36$h), Median ($7.79$h), and Standard ($8.0$h) lines.
5. **Scatter Plot** (`scatter_hours_vs_overtime.png`): Daily work hours vs. Overtime hours with linear regression trendline ($y = mx + c$) and department color coding.
6. **Master Executive Dashboard** (`attendance_analytics_master_dashboard.png`): High-resolution 6-in-1 multi-panel summary figure.

### 4. Styled Excel Dashboard (`outputs/Employee_Attendance_Dashboard.xlsx`)
* **Sheet 1: `Executive_Dashboard`**: Navy-styled KPI cards (Total Workforce, Overall Attendance %, Total Overtime, Absenteeism Rate), formatted Department summary table, Monthly trend table, and embedded native Excel Bar and Line charts.
* **Sheet 2: `Employee_Scorecard`**: Employee-by-employee scorecard with attendance rate, days present, and performance tier.
* **Sheet 3: `Cleaned_Data_Sample`**: Cleaned audit records.

### 5. Interactive Desktop GUI Dashboard (`src/gui_dashboard.py`)
* **Dark Slate Modern Theme** with live KPI metric cards.
* **Dynamic Department Filter**: Selecting any department instantly recalculates KPIs, updates charts, and filters the table.
* **Tabs**: Visualizations tab, Employee Scorecard table (Treeview), and NumPy/Pandas statistical insights explorer.
* **Action Buttons**: 1-click export to Excel, PNG images, and text reports.

---

## 🌐 Step-by-Step GitHub Upload & Submission Guide

You can upload this project to GitHub using either of the following two easy methods:

### Method A: Upload Directly via GitHub Web UI (Quickest & Easiest)

1. **Log in to GitHub**: Go to [https://github.com](https://github.com) and log into your account.
2. **Create a New Repository**:
   - Click the **`+`** icon in the top right corner and click **New repository**.
   - Repository name: `Employee-Attendance-Analytics-Dashboard`
   - Description: `Employee Attendance Analytics Dashboard using Python, NumPy, Pandas, Matplotlib, and Excel`
   - Set repository visibility to **Public**.
   - **Do NOT** check "Add a README file" (we already have a complete one).
   - Click **Create repository**.
3. **Upload Files**:
   - On the newly created repository page, click the link: **"uploading an existing file"**.
   - Open your folder: `C:\Users\HP\Downloads\SHREYA\Employee_Attendance_Analytics`
   - Select and drag all files and folders (`main.py`, `requirements.txt`, `README.md`, `run_pipeline.bat`, `launch_gui_dashboard.bat`, `src/`, `data/`, `outputs/`) into the GitHub upload area.
   - Under **Commit changes**, type: `Initial commit: Complete Employee Attendance Analytics Project`
   - Click **Commit changes**.
4. **Copy Repository Link**:
   - Copy the URL from your browser address bar (e.g. `https://github.com/your-username/Employee-Attendance-Analytics-Dashboard`).
   - Submit this link!

---

### Method B: Upload via Git Command Line / Git Bash

If you have Git installed, run these commands inside the `Employee_Attendance_Analytics` directory:

```bash
# 1. Initialize git repository
git init

# 2. Add all project files
git add .

# 3. Create initial commit
git commit -m "feat: complete employee attendance analytics dashboard project"

# 4. Set main branch
git branch -M main

# 5. Connect to your GitHub repository (replace with your repo URL)
git remote add origin https://github.com/<YOUR-GITHUB-USERNAME>/Employee-Attendance-Analytics-Dashboard.git

# 6. Push to GitHub
git push -u origin main
```

---

## 📝 मराठीत माहिती (Project Summary in Marathi)

या प्रोजेक्टमध्ये तुम्ही विचारलेली प्रत्येक टेक्नोलॉजी आणि प्रत्येक टूल सविस्तरपणे इम्प्लिमेंट केले आहे:
1. **Python**: Variables, conditions, loops, Functions, List, Tuple, Set, Dictionary, आणि File handling वापरून डेटा जनरेशन आणि ऑडिट लॉग तयार केले आहेत.
2. **NumPy**: 1D/2D arrays, Indexing & slicing, Statistical operations (Mean, Median, Std, IQR), Mathematical operations (Vectorized overtime, Dot product payroll), आणि Reshaping ((4, 5) weekly grids) पूर्ण केले आहे.
3. **Pandas**: Data cleaning, Missing value imputation (`fillna`), Merging (`pd.merge`), GroupBy & Aggregations, Filtering, आणि Sorting करून डिपार्टमेंट व मंथली रिपोर्ट बनवले आहेत.
4. **Matplotlib Visualizations**: Bar chart, Line chart (7-Day Moving Avg), Donut Pie chart, Histogram, Scatter plot, आणि 6-in-1 Master Dashboard इमेज सेव्ह केली आहे.
5. **Dashboard**: 
   - **Excel Dashboard**: ऑटोमॅटिक स्टाईल केलेले KPI कार्ड्स, टेबल्स आणि एक्सेल चार्ट्ससह `Employee_Attendance_Dashboard.xlsx` तयार केले आहे.
   - **Desktop Python GUI Dashboard**: Tkinter आणि Matplotlib वापरून इंटरॅक्टिव्ह डार्क-थीम डॅशबोर्ड तयार केला आहे, ज्यामध्ये फिल्टर, चार्ट्स आणि टेबल्स आहेत.
6. **GitHub Ready**: हा प्रोजेक्ट पूर्णपणे GitHub वर अपलोड करण्यासाठी रेडी आहे. वरील **GitHub Upload Guide** वाचून 2 मिनिटांत लिंक सबमिट करता येईल.

---

## 👤 Author & Submission Details
* **Project**: Employee Attendance Analytics Dashboard
* **Technologies**: Python, NumPy, Pandas, Matplotlib, OpenPyXL, Tkinter
* **Status**: Complete & Ready for Evaluation
