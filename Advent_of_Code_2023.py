##----- SAMPLE DATA

"""
sam_data = ['1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet']

file = open('C:/Users/jacob/Documents/JACOB INTO TECH/Advent of Code 2023/day_1_sampledata.txt', 'r')
"""

##------ SAMPLE DATA 2
## In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

from curses import typeahead


sam_file = open('C:/Users/jacob/Documents/JACOB INTO TECH/Advent of Code 2023/day_1_sampledata2.txt', 'r')


##----- LOADING REAL DATA

# file = open('c:/users/jacob/documents/jacob into tech/advent of code 2023/day1_inputdata.txt', 'r')

list_of_nums = []

for line in sam_file:
    nums = []
    words = line.split()
    """
    for character in line:
        if character in ['0','1','2','3','4','5','6','7','8','9']:
            nums.append(character)             ]:
        elif line in ['one','two','three','four','five','six','seven','eight','nine','zero']:
            if character == 'one':
                    nums.append('1')
            elif character == 'two':
                nums.append('2')
            elif character == 'three':
                nums.append('3')
            elif character == 'four':
                nums.append('4')
            elif character == 'five':
                nums.append('5')
            elif character == 'six':
                nums.append('6')
            elif character == 'seven':
                nums.append('7')
            elif character == 'eight':
                nums.append('8')
            elif character == 'nine':
                nums.append('9')
        """
    print(line)
    print(type(line))
    print(words)
    print(type(words))

    list_of_nums.append(nums)


print(list_of_nums)


total_count = 0

for list in list_of_nums:
    sum = int(list[0] + list[-1])
    total_count += sum

print(total_count)
