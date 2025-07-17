# Statistics for Class 10 CBSE 📊

A comprehensive Python-based learning resource for Class 10 CBSE Statistics concepts. This repository provides practical implementations of statistical measures (Mean, Median, and Mode) with clear examples and formatted output tables.

## 📖 About This Repository

This repository is designed to help Class 10 CBSE students understand statistics through programming. Instead of just theoretical formulas, you can see how statistical calculations work with real code and data examples.

### 🎯 Learning Objectives
- Understand practical applications of statistical measures
- Learn to calculate Mean, Median, and Mode for grouped data
- Visualize data in formatted tables
- Bridge the gap between mathematical theory and practical implementation

## 📂 Repository Structure

```
Statistics-for-class-10-CBSE/
├── README.md
└── stats/
    ├── mean/
    │   └── direct method.py    # Mean calculation using direct method
    ├── median.py               # Median calculation for grouped data
    └── mode.py                 # Mode calculation for grouped data
```

## 📚 Statistical Concepts Covered

### 1. **Mean (Arithmetic Average)**
- **File**: `stats/mean/direct method.py`
- **Method**: Direct Method for grouped data
- **Formula**: Mean = Σ(xi × fi) / Σfi
- **Features**: 
  - Calculates class marks (xi) automatically
  - Shows step-by-step calculation with xi×fi values
  - Formatted table output with pipe format

### 2. **Median (Middle Value)**
- **File**: `stats/median.py`
- **Method**: For grouped frequency distribution
- **Formula**: Median = l + [(n/2 - cf)/f] × h
- **Features**:
  - Automatic cumulative frequency calculation
  - Identifies median class
  - Shows all intermediate values used in calculation

### 3. **Mode (Most Frequent Value)**
- **File**: `stats/mode.py`
- **Method**: For grouped frequency distribution
- **Formula**: Mode = l + [(f1-f0)/(2f1-f0-f2)] × h
- **Features**:
  - Identifies modal class automatically
  - Extracts and displays all formula components
  - Clear step-by-step calculation

## 🚀 Quick Start

### Prerequisites
Make sure you have Python installed on your system.

### Installation

Install required dependencies:

```bash
pip install tabulate numpy
```

### Running the Examples

1. **Calculate Mean:**
   ```bash
   python "stats/mean/direct method.py"
   ```

2. **Calculate Median:**
   ```bash
   python stats/median.py
   ```

3. **Calculate Mode:**
   ```bash
   python stats/mode.py
   ```

## 💡 Sample Output

### Mean Calculation Output:
```
| Interval   |   Frequency |   class mark |   Summation(XiFi) |
|:-----------|------------:|-------------:|------------------:|
| 0-10       |         105 |            5 |               525 |
| 10-20      |         222 |           15 |              3330 |
| 20-30      |         220 |           25 |              5500 |
...
The mean of the data is: 31.49
```

### Median Calculation Output:
```
+----------+-----------+----------------------+
| Interval | Frequency | Cumulative Frequency |
+----------+-----------+----------------------+
|  20-30   |     5     |          5           |
|  30-40   |    15     |          20          |
|  40-50   |    25     |          45          |
...
So, Median = 50.0
```

## 🔧 Code Features

- **User-friendly table formatting** using the `tabulate` library
- **Automatic calculations** with step-by-step breakdowns
- **Sample data included** for immediate testing
- **CBSE curriculum aligned** formulas and methods
- **Clear variable naming** for educational purposes

## 📝 Important Notes

- All data should be in **inclusive class intervals** (e.g., 10-20 includes both 10 and 20)
- The code uses standard CBSE Class 10 statistical formulas
- Sample data is provided in each file for demonstration

## 🤝 Contributing

Feel free to contribute by:
- Adding more statistical methods (assumed mean, step deviation)
- Improving code documentation
- Adding more examples
- Reporting bugs or suggesting improvements

## 📞 Support

If you encounter any issues or have suggestions:
- Open an issue in this repository
- Check that all dependencies are properly installed
- Ensure your data follows the required format (inclusive intervals)

---

**Happy Learning! 🎓📊**

*This repository is specifically designed for CBSE Class 10 students to make statistics more accessible and engaging through practical programming examples.*