"""main.py
=======
Master execution and orchestration script for the
Employee Attendance Analytics Dashboard project.

Usage:
  python main.py           # Runs complete analysis, prints summaries, exports files
  python main.py --gui     # Launches the interactive Tkinter GUI dashboard
  python main.py --excel   # Exports the styled Excel dashboard workbook
  python main.py --visuals # Generates all 6 Matplotlib charts
"""

import os
import sys
import argparse
from typing import Dict, Any

# Ensure project root is in Python module search path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.data_generator import generate_all_datasets
from src.numpy_analytics import AttendanceNumPyAnalytics
from src.pandas_analytics import AttendancePandasAnalytics
from src.visualizer import AttendanceVisualizer
from src.excel_dashboard import AttendanceExcelDashboard


def print_banner():
    banner = """
================================================================================
          EMPLOYEE ATTENDANCE ANALYTICS DASHBOARD - WORKFORCE INTELLIGENCE      
================================================================================
    Technology Stack:
      * Python    : Data Structures (List, Tuple, Set, Dict), Loops, File I/O
      * NumPy     : 1D/2D Arrays, Indexing, Slicing, Statistics, Matrix Math, Reshaping
      * Pandas    : DataFrames, Cleaning, Imputation, Merging, GroupBy, Filtering
      * Matplotlib: Bar, Line, Pie, Histogram, Scatter, Master Multi-Panel Dashboard
      * Dashboard : Automated Styled Excel Dashboard & Interactive Desktop GUI
================================================================================
    """
    print(banner)


def run_complete_pipeline(launch_gui_after: bool = False):
    """Executes the entire analytics workflow end-to-end."""
    print_banner()

    # ---------------------------------------------------------
    # STEP 1: DATA INGESTION & CORE PYTHON DEMONSTRATION
    # ---------------------------------------------------------
    print("\n[STEP 1/5] Checking Datasets & Python Data Structures...")
    data_dir = os.path.join(PROJECT_ROOT, "data")
    emp_csv = os.path.join(data_dir, "employees.csv")
    att_csv = os.path.join(data_dir, "attendance_logs.csv")

    if not os.path.exists(emp_csv) or not os.path.exists(att_csv):
        print("  -> Generating synthetic raw datasets...")
        generate_all_datasets(data_dir)
    else:
        print("  -> Datasets found in data/ directory.")

    # ---------------------------------------------------------
    # STEP 2: PANDAS DATA CLEANING, MERGING & AGGREGATION
    # ---------------------------------------------------------
    print("\n[STEP 2/5] Running Pandas Data Pipeline (Cleaning, Merge, GroupBy)...")
    pandas_engine = AttendancePandasAnalytics(data_dir)
    df_cleaned = pandas_engine.clean_and_preprocess()
    dept_df = pandas_engine.department_summary()
    monthly_df = pandas_engine.monthly_trend_summary()
    scorecard_df = pandas_engine.employee_scorecard_summary()
    basic_stats = pandas_engine.compute_basic_statistics()

    print(f"  -> Cleaned Records   : {len(df_cleaned):,} daily logs")
    print(f"  -> Total Employees   : {len(df_cleaned['Employee_ID'].unique())} active personnel")
    print(f"  -> Departments       : {', '.join(sorted(df_cleaned['Department'].unique()))}")

    print("\n--- DEPARTMENT ATTENDANCE & OVERTIME SUMMARY ---")
    print(dept_df.to_string(index=False))

    print("\n--- MONTHLY ATTENDANCE TREND SUMMARY ---")
    print(monthly_df.to_string(index=False))

    # ---------------------------------------------------------
    # STEP 3: NUMPY MATHEMATICAL & STATISTICAL OPERATIONS
    # ---------------------------------------------------------
    print("\n[STEP 3/5] Running NumPy Statistical & Reshaping Suite...")
    df_employees = pandas_engine.df_employees_raw
    numpy_engine = AttendanceNumPyAnalytics(df_cleaned, df_employees)
    numpy_results = numpy_engine.run_full_numpy_suite()

    stat_1d = numpy_results["1D_Statistics"]
    slice_res = numpy_results["Indexing_and_Slicing"]
    math_res = numpy_results["Mathematical_Operations"]
    shape_res = numpy_results["Reshaping_Operations"]

    print(f"  * 1D Work Hours Mean: {stat_1d['Mean_Hours']:.2f}h | Median: {stat_1d['Median_Hours']:.2f}h | Std: {stat_1d['Std_Deviation']:.2f}h")
    print(f"  * Quartiles: Q1={stat_1d['25th_Percentile (Q1)']:.2f}h | Q2={stat_1d['50th_Percentile (Q2)']:.2f}h | Q3={stat_1d['75th_Percentile (Q3)']:.2f}h | IQR={stat_1d['Interquartile_Range_IQR']:.2f}h")
    print(f"  * 2D Slicing (First 5 Emps x 10 Days) Mean Hours: {slice_res['Sub_Matrix_5x10_Mean']:.2f}h")
    print(f"  * Vectorized Overtime Hours: {math_res['Vectorized_Total_Overtime_Hours']:,.1f} hrs")
    print(f"  * Estimated Overtime Payout: INR {math_res['Total_Estimated_Overtime_Payout_INR']:,.2f}")
    print(f"  * Reshaped (4 Weeks x 5 Days) Grid Shape: {shape_res['Reshaped_Weekly_Grid_Shape']}")
    print(f"  * Weekly Mean Hours Array: {[round(x, 2) for x in shape_res['Weekly_Average_Hours']]}")

    # ---------------------------------------------------------
    # STEP 4: MATPLOTLIB VISUALIZATIONS GENERATION
    # ---------------------------------------------------------
    print("\n[STEP 4/5] Generating Matplotlib High-Resolution Visualizations...")
    charts_dir = os.path.join(PROJECT_ROOT, "outputs", "charts")
    visualizer = AttendanceVisualizer(df_cleaned, output_dir=charts_dir)
    chart_paths = visualizer.export_all_visualizations()

    for name, path in chart_paths.items():
        print(f"  [+] Saved {name:<26} -> {os.path.basename(path)}")

    # ---------------------------------------------------------
    # STEP 5: EXCEL ANALYTICS DASHBOARD GENERATION
    # ---------------------------------------------------------
    print("\n[STEP 5/5] Building Styled Corporate Excel Analytics Dashboard...")
    excel_path = os.path.join(PROJECT_ROOT, "outputs", "Employee_Attendance_Dashboard.xlsx")
    excel_gen = AttendanceExcelDashboard(
        df_cleaned, dept_df, monthly_df, scorecard_df, output_filepath=excel_path
    )
    excel_gen.generate()

    # Save Executive Summary Text Report (Python File Handling)
    report_file = os.path.join(PROJECT_ROOT, "outputs", "executive_attendance_summary.txt")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("EMPLOYEE ATTENDANCE ANALYTICS - EXECUTIVE SUMMARY\n")
        f.write("=" * 65 + "\n\n")
        f.write("[1. DEPARTMENT PERFORMANCE]\n")
        f.write(dept_df.to_string(index=False) + "\n\n")
        f.write("[2. MONTHLY WORKFORCE TRENDS]\n")
        f.write(monthly_df.to_string(index=False) + "\n\n")
        f.write("[3. NUMPY STATISTICAL HIGHLIGHTS]\n")
        for k, v in stat_1d.items():
            f.write(f"  * {k:<25}: {v}\n")
    print(f"  [+] Executive summary text report saved -> {os.path.basename(report_file)}")

    print("\n" + "=" * 80)
    print("ALL PROJECT DELIVERABLES SUCCESSFULLY GENERATED!")
    print(f"  1. Datasets            : {os.path.join(PROJECT_ROOT, 'data')}")
    print(f"  2. Visualizations (6x) : {charts_dir}")
    print(f"  3. Excel Dashboard     : {excel_path}")
    print(f"  4. Text Report         : {report_file}")
    print("=" * 80)

    if launch_gui_after:
        print("\n[*] Launching Interactive Tkinter GUI Dashboard...")
        from src.gui_dashboard import launch_gui
        launch_gui()


def main():
    parser = argparse.ArgumentParser(description="Employee Attendance Analytics Master Pipeline")
    parser.add_argument("--gui", action="store_true", help="Launch the Desktop GUI Dashboard directly")
    parser.add_argument("--excel", action="store_true", help="Generate Excel Dashboard workbook only")
    parser.add_argument("--visuals", action="store_true", help="Generate Matplotlib charts only")
    parser.add_argument("--all", action="store_true", help="Run full pipeline and launch GUI")

    args = parser.parse_args()

    if args.gui:
        from src.gui_dashboard import launch_gui
        launch_gui()
    elif args.excel:
        data_dir = os.path.join(PROJECT_ROOT, "data")
        pandas_engine = AttendancePandasAnalytics(data_dir)
        df_cleaned = pandas_engine.clean_and_preprocess()
        dept_df = pandas_engine.department_summary()
        monthly_df = pandas_engine.monthly_trend_summary()
        scorecard_df = pandas_engine.employee_scorecard_summary()
        excel_path = os.path.join(PROJECT_ROOT, "outputs", "Employee_Attendance_Dashboard.xlsx")
        AttendanceExcelDashboard(df_cleaned, dept_df, monthly_df, scorecard_df, excel_path).generate()
    elif args.visuals:
        data_dir = os.path.join(PROJECT_ROOT, "data")
        pandas_engine = AttendancePandasAnalytics(data_dir)
        df_cleaned = pandas_engine.clean_and_preprocess()
        charts_dir = os.path.join(PROJECT_ROOT, "outputs", "charts")
        AttendanceVisualizer(df_cleaned, charts_dir).export_all_visualizations()
    else:
        run_complete_pipeline(launch_gui_after=args.all)


if __name__ == "__main__":
    main()
