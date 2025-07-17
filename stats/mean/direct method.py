"""
Mean Calculation using Direct Method for Grouped Data
====================================================

Formula: Mean = Σ(xi × fi) / Σfi
Where:
- xi = class mark (midpoint of each interval)
- fi = frequency of each class
- Σ = summation symbol

CBSE Class 10 Statistics - Chapter: Statistics
"""

from tabulate import tabulate

# Sample data: Class intervals and their frequencies
interval = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70']
frequency = [105,222,220,138,102,113,100]

# Initialize lists for calculations
xi = []      # Class marks (midpoints)
xifi = []    # Product of class mark and frequency

# Calculate class marks and xi*fi for each interval
for i in range(len(frequency)):
    # Class mark = (lower limit + upper limit) / 2
    class_mark = (int(interval[i].split('-')[0]) + int(interval[i].split('-')[1])) / 2
    xi.append(class_mark)
    # Calculate xi * fi
    xifi.append(class_mark * frequency[i])

# Create formatted table showing all calculations
final = list(zip(interval, frequency, xi, xifi))
print("MEAN CALCULATION - DIRECT METHOD")
print("=" * 40)
print(tabulate(final, headers=['Interval','Frequency','Class Mark (xi)','xi × fi'], tablefmt='pipe'))

# Calculate mean using the formula
mean = sum(xifi) / sum(frequency)
print(f"\nCalculation:")
print(f"Mean = Σ(xi × fi) / Σfi")
print(f"Mean = {sum(xifi)} / {sum(frequency)}")
print(f"Mean = {mean:.2f}")
print(f"\nThe mean of the data is: {mean:.2f}")