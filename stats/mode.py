"""
Mode Calculation for Grouped Frequency Distribution
=================================================

Formula: Mode = l + [(f1-f0)/(2f1-f0-f2)] × h
Where:
- l = lower boundary of modal class
- f1 = frequency of modal class
- f0 = frequency of class before modal class
- f2 = frequency of class after modal class
- h = class width

CBSE Class 10 Statistics - Chapter: Statistics
"""

import numpy as np
from tabulate import tabulate

# Sample data: Class intervals and their frequencies
interval = ['80-85','85-90','90-95','95-100','100-105','105-110','110-115']
frequency = [33,27,85,155,110,45,15]

# Create frequency distribution table
final = zip(interval, frequency)
print("MODE CALCULATION - GROUPED DATA")
print("=" * 40)
print(tabulate(final, headers=['Interval','Frequency'], tablefmt='pretty'))

# Find modal class (class with highest frequency)
modal_class_index = frequency.index(np.max(frequency))

# Extract values for mode calculation
l = int(interval[modal_class_index].split('-')[0])  # Lower boundary of modal class
h = int(interval[modal_class_index].split('-')[1]) - int(interval[modal_class_index].split('-')[0])  # Class width
f1 = frequency[modal_class_index]  # Frequency of modal class
f0 = frequency[modal_class_index-1]  # Frequency of class before modal class
f2 = frequency[modal_class_index+1]  # Frequency of class after modal class

print(f"\nCalculation Details:")
print(f"Modal class: {interval[modal_class_index]} (highest frequency = {f1})")
print(f"l (lower boundary of modal class) = {l}")
print(f"f1 (frequency of modal class) = {f1}")
print(f"f0 (frequency before modal class) = {f0}")
print(f"f2 (frequency after modal class) = {f2}")
print(f"h (class width) = {h}")

# Calculate mode using the formula
# Note: There's a correction in the original formula - it should be l + not (l+h)
mode = l + h * (f1 - f0) / (2*f1 - f0 - f2)

print(f"\nFormula: Mode = l + [(f1-f0)/(2f1-f0-f2)] × h")
print(f"Mode = {l} + [({f1}-{f0})/(2×{f1}-{f0}-{f2})] × {h}")
print(f"Mode = {l} + [{f1-f0}/{2*f1-f0-f2}] × {h}")
print(f"Mode = {l} + {(f1-f0)/(2*f1-f0-f2):.4f} × {h}")
print(f"Mode = {mode:.2f}")
print(f"\nHence, mode is {mode:.2f}")