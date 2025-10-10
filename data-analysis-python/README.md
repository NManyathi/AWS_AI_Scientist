## 👨🏽‍💻 Author
**Walter Njabulo Manyathi**  
📍 Data Analyst | Statistician | AWS AI Scholar  
🔗 [GitHub](https://github.com/NManyathi) • [LinkedIn](https://www.linkedin.com/in/walter-njabulo-manyathi-0b4981172/)

---

# 📘 Data Analysis with Python — Lessons, Exercises, and Mini-Projects

This repository contains my learning progress and practice work for the **Data Analysis** section of the **AWS AI Scientist Scholarship (Udacity)**.  
It covers **Python data analysis fundamentals** using Jupyter, NumPy, Pandas, Matplotlib, and Seaborn.  
Each lesson includes guided exercises and a mini-project demonstrating hands-on application of the concepts learned.

---

## 🧠 Lessons Overview

### 1️⃣ Jupyter Notebooks (Setup)
**Objective:**  
Set up and use Jupyter Notebooks as an interactive environment for running Python code.

**Key Topics:**
- Installing Jupyter and configuring virtual environments  
- Running and saving notebooks (`.ipynb` files)  
- Combining code, text, and visuals using Markdown  
- Inline plotting and documentation best practices  

> 🧩 *All lessons below (NumPy, Pandas, Matplotlib & Seaborn) are developed and run within Jupyter.*

---

### 2️⃣ NumPy
**Objective:**  
Understand and use NumPy for efficient numerical computation and array manipulation.

**Key Topics:**
- Arrays, vectors, and matrices  
- Broadcasting and slicing  
- Element-wise operations  
- Random number generation and statistical functions  

**Exercises:**  
- Create and manipulate arrays  
- Compute mean, median, and standard deviation  
- Compare list vs array performance  

**Mini-Project:**  
📊 *“Statistical Summary Calculator”* — build a tool to compute descriptive statistics using NumPy arrays.

---

### 3️⃣ Pandas
**Objective:**  
Work with structured data using Pandas for cleaning, transformation, and statistical analysis.

**Key Topics:**
- Series and DataFrames  
- Importing and exporting data (CSV, Excel)  
- Handling missing values  
- Filtering, grouping, and merging datasets  
- Data summarization and correlation  

**Exercises:**  
- Load, clean, and analyze tabular datasets  
- Apply custom and lambda functions  
- Explore real-world data using descriptive statistics  

**Mini-Project:**  
📈 *“Statistics From Stock Data”* — apply NumPy and Pandas to analyze stock price trends.  
Tasks include loading CSV data, computing daily returns and moving averages, and visualizing trends with Matplotlib and Seaborn.

---

### 4️⃣ Matplotlib and Seaborn — Part 1
**Objective:**  
Visualize data using Matplotlib and Seaborn to identify trends and insights.

**Key Topics:**
- Basic plots (line, bar, histogram, scatter)  
- Customizing axes, titles, and legends  
- Plot aesthetics with color palettes and styles  

**Exercises:**  
- Create different chart types using both libraries  
- Customize visuals with annotations and labels  

**Mini-Project:**  
📉 *“COVID-19 Data Trends”* — visualize infection rates, recoveries, and regional comparisons using real-world data.

---

### 5️⃣ Matplotlib and Seaborn — Part 2
**Objective:**  
Advance your visualization skills with multi-plot layouts, statistical visualizations, and presentation-ready graphics.

**Key Topics:**
- Subplots and figure grids  
- Heatmaps, pairplots, and boxplots  
- Theming and fine-tuning visual presentation  

**Exercises:**  
- Create multi-panel dashboards  
- Explore relationships using Seaborn’s statistical plots  

**Mini-Project:**  
📊 *“Sales Performance Dashboard”* — build a visual analytics dashboard showing key sales and revenue metrics.

---

## 🧩 Repository Structure

```bash
📂 AWS_AI_Scientist/
│
├── 📁 aws_ai_env/                # Shared virtual environment for all projects
│
├── 📁 data-analysis-python/
│   ├── 📁 01_numpy/
│   │   ├── lesson.ipynb
│   │   ├── exercises/
│   │   └── mini_project_statistical_summary.ipynb
│   │
│   ├── 📁 02_pandas/
│   │   ├── lesson.ipynb
│   │   ├── exercises/
│   │   └── mini_project_stock_statistics.ipynb
│   │
│   ├── 📁 03_matplotlib_seaborn_part1/
│   │   ├── lesson.ipynb
│   │   ├── exercises/
│   │   └── mini_project_covid_trends.ipynb
│   │
│   ├── 📁 04_matplotlib_seaborn_part2/
│   │   ├── lesson.ipynb
│   │   ├── exercises/
│   │   └── mini_project_sales_dashboard.ipynb
│   │
│   └── README.md
```

---

## 🚀 How to Run

1. **Activate your shared virtual environment (created under main repository):**
   ```bash
   # Windows
   cd path\to\AWS_AI_Scientist
   aws_ai_env\Scripts\activate

   # macOS/Linux
   cd path/to/AWS_AI_Scientist
   source aws_ai_env/bin/activate
   ```

2. **Navigate to this project folder:**
   ```bash
   cd data-analysis-python
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

4. Open any lesson or mini-project notebook and run the cells sequentially to explore the analysis and visualizations.

> 💡 Tip: If you want Jupyter to always use this environment, register it once using:
> ```bash
> python -m ipykernel install --user --name=aws_ai_env --display-name "Python (aws_ai_env)"
> ```
> Then select **Python (aws_ai_env)** as the kernel in Jupyter.

---

## 🧾 Notes
- Developed using **Python 3.x** and **Jupyter Notebook**.  
- Core libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`.  
- All exercises and mini-projects demonstrate end-to-end data analysis workflow — from data loading and transformation to visualization and interpretation.  
- Created as part of the **AWS AI Scientist Scholarship (Udacity)** program.

> 💬 All projects and exercises (except the Pandas lesson) are based on my own work — from selecting datasets to defining project goals and analysis steps.  
> The Pandas mini-project uses Udacity-provided data and guidance as part of the structured lesson content.

---

