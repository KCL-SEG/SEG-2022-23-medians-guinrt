"""Median calculator."""
import math

def findMedian(numbers):
	sorted_list = sorted(numbers)
	if len(sorted_list) == 1:
		return sorted_list[0]
	if len(sorted_list) % 2 != 0:
		m = sorted_list[math.ceil((len(sorted_list)/2)) - 1]
		return m
	else:
		m1 = sorted_list[math.floor((len(sorted_list)/2)) - 1]
		m2 = sorted_list[math.ceil((len(sorted_list)/2)) - 1]
		return (m1 + m2) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(findMedian(numbers))
