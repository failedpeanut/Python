'''
- write a function which take 2 numbers as String
("234","567")
- return True if first Number is greater than 2nd
-else return False if 2nd number is less than first
-if both numbers are equal return False
-Numbers can't be negative or empty
- should NOT use int(string) function to convert string to integer
clue:
"3">"2" -> returns True in case of single digit String represented as int
'''


def checkNumbers(num1,num2):
        if len(num1) ==len(num2):
            return perform_check(num1,num2)
        if len(num1) > len(num2):
            return True
        if len(num1)<len(num2):
            return False


def perform_check(num1,num2):
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            return True
    return False





print(checkNumbers("456","123"))
print(checkNumbers("457","456"))
print(checkNumbers("456","456"))
print(checkNumbers("9998","1000"))
print(checkNumbers("0009","008"))


