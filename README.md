# 🌍 EU27 vs USA: Energy Policy Analysis

> **Nuclear and Renewable Energy Comparison**  
> Analysis of European Union and USA energy transition processes using real data from Our World in Data (OWID)

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

## 📋 About the Project

This project analyzes the time series trends of **nuclear energy** and **renewable energy** usage between the **European Union (EU27)** and the **USA**. It works with real and current data using **Our World in Data (OWID)** datasets.

### 🌍 What is EU27?

**EU27** represents the **27 member countries** of the European Union. After Brexit in 2020, when the United Kingdom left, it decreased from EU28 to EU27.

#### **EU27 Member Countries:**

**Western Europe:** France, Germany, Italy, Spain, Portugal, Belgium, Netherlands, Luxembourg, Ireland

**Northern Europe:** Sweden, Denmark, Finland, Estonia, Latvia, Lithuania

**Central Europe:** Austria, Czech Republic, Slovakia, Slovenia, Hungary, Poland

**Southern Europe:** Greece, Croatia, Romania, Bulgaria, Malta, Cyprus

#### **EU27 in Energy Analysis:**
In our project, EU27 data represents the **total energy consumption** and **energy mix** of these 27 countries. EU27 is more advanced than the USA in **renewable energy** and **low-carbon** issues.

### 🎯 Main Objectives
- Comparative analysis of EU27 and USA energy policies
- Examination of nuclear energy usage trends
- Analysis of renewable energy development
- Evaluation of low-carbon transition processes

## 📊 Analysis Results (2024)

| Energy Source | EU27 | USA | Difference |
|---------------|------|-----|------------|
| **Nuclear Energy** | 10.1% | 7.6% | EU27 +2.5% |
| **Renewable Energy** | 22.3% | 12.1% | EU27 +10.2% |
| **Low Carbon (Total)** | 32.4% | 19.7% | EU27 +12.7% |
| **Fossil Fuel** | 67.6% | 80.3% | EU27 -12.7% |

### 🔍 Trend Analysis (2015-2024)

#### EU27
- **Nuclear**: 11.8% → 10.1% (▼ -1.7%)
- **Renewable**: 14.2% → 22.3% (▲ +8.1%)

#### USA
- **Nuclear**: 8.3% → 7.6% (▼ -0.7%)
- **Renewable**: 7.2% → 12.1% (▲ +4.9%)

## 🚀 Installation

### Requirements
- Python 3.8+
- pip (Python package manager)
- Git

### Step-by-Step Installation

```bash
# 1. Clone the project
git clone https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-.git
cd energy-nuclear-renewable-analysis-

# 2. Create and activate virtual environment
make install

# 3. Download data
make data

# 4. Process data
make process
```

## 📁 Project Structure

```
energy-nuclear-renewable-analysis-/
├── 📊 data/                    # Data files
│   ├── raw/                   # Raw data downloaded from OWID
│   └── processed/             # Processed data
├── 📝 notebooks/              # Jupyter notebooks
│   └── shale_gas_triple_analysis.ipynb  # Triple comparison analysis
├── 🔧 scripts/                # Python scripts
│   ├── download_data.py       # Data download script
│   ├── process_data.py        # Data processing script
│   ├── shale_gas_analysis.py  # Comprehensive shale gas analysis
│   ├── simple_shale_gas_analysis.py  # Simple shale gas analysis
│   └── triple_comparison_analysis.py  # Triple comparison analysis
├── 📈 reports/                # Analysis reports and graphs
│   ├── comprehensive_energy_analysis.png  # Comprehensive energy analysis
│   ├── energy_analysis.png    # Energy analysis
│   ├── triple_comparison_analysis.png  # Triple comparison
│   ├── shale_gas_impact.png   # Shale gas impact
│   ├── shale_gas_analysis.png # Shale gas analysis
│   └── simple_gas_analysis.png # Simple gas analysis
├── 📋 requirements.txt        # Python dependencies
├── ⚙️ Makefile                # Automated processes
└── 📖 README.md               # This file
```

## 🛠️ Usage

### Basic Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Data update
make data          # Download new data from OWID
make process       # Process data and prepare for analysis

# Start Jupyter Lab
make notebook

# Report generation
make report        # Create HTML report

# Shale gas analysis
python scripts/shale_gas_analysis.py          # Comprehensive shale gas analysis
python scripts/triple_comparison_analysis.py  # Triple comparison analysis
```

### Manual Data Download

```bash
# Data download only
python scripts/download_data.py

# Data processing only
python scripts/process_data.py
```

## 📊 Data Sources

### Our World in Data (OWID)
- **Energy Data**: [energy-data](https://github.com/owid/energy-data)
- **CO2 Data**: [co2-data](https://github.com/owid/co2-data)
- **Main Site**: [ourworldindata.org/energy](https://ourworldindata.org/energy)

### Data Quality
- ✅ **University of Oxford** project
- ✅ **Open source** methodology
- ✅ **Current data** (1900-2024)
- ✅ **International standards**
- ✅ **Used in academic research**

## 🔬 Analysis Methodology

### Data Processing Process
1. **Raw Data Download**: Automatic download from OWID GitHub repositories
2. **Data Cleaning**: Removal of missing values and inconsistencies
3. **Data Transformation**: Creating comparative dataset for EU27 and USA
4. **Analysis**: Time series analysis and trend calculations

### Technologies Used
- **Pandas**: Data manipulation and analysis
- **Matplotlib/Seaborn**: Visualization
- **NumPy**: Numerical calculations
- **Jupyter**: Interactive analysis

## 📈 Results and Comments

### EU27 Advantages
- **Renewable energy leadership** (22.3%)
- **Faster low-carbon transition** (32.4%)
- **Strong policy support** and targets

### USA Status
- **Renewable energy potential** exists
- **Conservative approach** to nuclear energy
- **Need for consistent policy** at federal level

### Policy Recommendations
1. **EU27**: Lifetime extension of existing nuclear reactors
2. **USA**: Next-generation nuclear technologies and renewable infrastructure
3. **Both regions**: Aggressive policies for 2050 carbon neutral targets

## ⛽ Shale Gas Analysis

### 🔍 Triple Comparison: Nuclear, Renewable, and Shale Gas

This project now also includes **shale gas** analysis. Natural gas data from the OWID dataset has been used to analyze shale gas impact.

#### 📊 Shale Gas Analysis Results

| Analysis Type | Description |
|---------------|-------------|
| **Shale Gas Revolution (2008)** | Beginning of shale gas production in USA |
| **Pre-2008 vs Post-2008** | Comparison before and after shale gas |
| **EU27 vs USA Gas Trends** | Comparison of natural gas usage trends |

#### 📈 New Notebook: `shale_gas_triple_analysis.ipynb`

**Content:**
- 🌍 **Nuclear Energy Trend**: EU27 vs USA (1990-2024)
- 🌱 **Renewable Energy Development**: Paris Agreement impact
- ⛽ **Natural Gas (Shale Gas Proxy)**: Shale Gas Revolution impact
- 📊 **2024 Energy Mix**: Triple comparison
- 📋 **Statistical Summary**: Detailed analysis results

**Features:**
- ✅ **Bilingual**: English and Turkish explanations
- ✅ **Visualization**: 4 different chart types
- ✅ **Interactive**: Jupyter Notebook format
- ✅ **Data-Driven**: With real OWID data

#### 🛠️ New Scripts

1. **`scripts/shale_gas_analysis.py`**: Comprehensive shale gas analysis
2. **`scripts/simple_shale_gas_analysis.py`**: Simple shale gas analysis
3. **`scripts/triple_comparison_analysis.py`**: Triple comparison analysis

#### 📊 New Reports

- `reports/triple_comparison_analysis.png`: Triple comparison chart
- `reports/shale_gas_impact.png`: Shale gas impact analysis
- `reports/shale_gas_analysis.png`: Comprehensive shale gas analysis
- `reports/simple_gas_analysis.png`: Simple gas analysis

### 🎯 Purpose of Shale Gas Analysis

1. **Understanding the impact** of USA Shale Gas Revolution on energy mix
2. **Analyzing differences** in natural gas usage between EU27 and USA
3. **Making triple comparison** of Nuclear, Renewable, and Gas energy sources
4. **Evaluating the impact** of energy policies on different fuel types

## 🤝 Contributing

This project is open source! We welcome your contributions:

1. **Fork** the project
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 👥 Author

**Zeynep Ruveyda** - [GitHub](https://github.com/ZeynepRuveyda)

## 🙏 Acknowledgments

- **Our World in Data** team for datasets
- **University of Oxford** for OWID project
- **Open source community**

## 📞 Contact

- **GitHub Issues**: [Repo Issues](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-/issues)
- **GitHub Discussions**: [Repo Discussions](https://github.com/ZeynepRuveyda/energy-nuclear-renewable-analysis-/discussions)

---

⭐ **Don't forget to star this project if you liked it!** ⭐

*Last update: August 2025*
