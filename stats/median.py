"""
Median Calculation for Grouped Frequency Distribution
===================================================

Formula: Median = l + [(n/2 - cf)/f] × h
Where:
- l = lower boundary of median class
- n = total number of observations
- cf = cumulative frequency before median class
- f = frequency of median class
- h = class width

CBSE Class 10 Statistics - Chapter: Statistics
"""

from tabulate import tabulate
import numpy as np

# Sample data: Class intervals and their frequencies
interval = ['20-30','30-40','40-50','50-60','60-70','70-80','80-90']
frequency = [5,15,25,20,7,8,10]

# Calculate cumulative frequency
cf = []
def cumulative(frequency, cf):
    """Calculate cumulative frequency step by step"""
    running_total = 0
    for i in range(len(frequency)):
        running_total = running_total + frequency[i]
        cf.append(running_total)

cumulative(frequency, cf)

# Create table with frequency and cumulative frequency
final = list(zip(interval, frequency, cf))

# Find median class
n = np.sum(frequency)  # Total observations
median_class_found = False

for i in range(len(frequency)):
    if (cf[i] > n/2) and (not median_class_found):
        # This is the median class
        newf = frequency[i]  # frequency of median class
        newcf = cf[i-1] if i > 0 else 0  # cumulative frequency before median class
        l = int(interval[i].split('-')[0])  # lower boundary of median class
        h = int(interval[i].split('-')[1]) - int(interval[i].split('-')[0])  # class width
        median_class_found = True

# Display the frequency distribution table
print("MEDIAN CALCULATION - GROUPED DATA")
print("=" * 40)
print(tabulate(final, headers=['Interval','Frequency','Cumulative Frequency'], tablefmt='pretty'))

# Show the calculation details
print(f"\nCalculation Details:")
print(f"Total observations (n) = {n}")
print(f"n/2 = {n/2}")
print(f"Median class: {interval[i]} (cf = {cf[i]} > {n/2})")
print(f"l (lower boundary) = {l}")
print(f"cf (cumulative frequency before median class) = {newcf}")
print(f"f (frequency of median class) = {newf}")
print(f"h (class width) = {h}")

# Calculate median using the formula
median = l + (h * (n/2 - newcf) / newf)
print(f"\nFormula: Median = l + [(n/2 - cf)/f] × h")
print(f"Median = {l} + [({n/2} - {newcf})/{newf}] × {h}")
print(f"Median = {l} + [{n/2 - newcf}/{newf}] × {h}")
print(f"Median = {l} + {(n/2 - newcf)/newf:.2f} × {h}")
print(f"Median = {median}")


