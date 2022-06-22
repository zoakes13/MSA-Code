# Stats Calculator

You are to create a program called stats_calculator.py that reads a series of integer numbers from a file and determines and displays the following:

 - Name of the file.
 - Sum of the numbers.
 - Count of how many numbers are in the file.
 - Average of the numbers. The average is the sum of the numbers divided by how many there are.
 - Maximum value.
 - Minimum value.
 - Range of the values. The range is the maximum value minus the minimum value.
 - Median of the numbers.
 - Mode of the numbers.

The output from the program is to display the information described above using the following strings preceding the values. There is to be a space between the colon and the value.

>
    File name:
    Sum:
    Count:
    Average:
    Maximum:
    Minimum:
    Range:
    Median:
    Mode:
>

## Mode and Median

**Example 1**

> Numbers: 6, 6, 7, 8, 10, 11, 15, 15, 17, 17, 17

There are 11 numbers in this example. This means that the median is the middle value. The middle value is at (11+1)/2 = 6. The 11 is at the 6th position and is therefore the median. Note that to calculate the position of the middle value add 1 to the quantity of numbers and divide by 2.

The mode is 17 because it occurs the most frequently. The number 17 occurs three times. The numbers 15 and 6 occur two times. All the other numbers occur one time.

**Example 2**

> Numbers: 5, 5, 6, 7, 8, 9, 9, 10, 10, 11

There are 10 numbers in this example. Because there are an even count of numbers, the median is the average of the two numbers around the middle. The middle position is (10+1)/2 = 5.5. The numbers at position 5 and position 6 need to be averaged. The number 8 is at position 5 and the number 9 is at position 6. The average of 8 and 9 is (8+9)/2 = 17/2 = 8.5. The list of numbers has three modes: 5, 9, and 10. These three numbers occur two times. The other numbers occur one time.
