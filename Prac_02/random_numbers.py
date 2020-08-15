import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""What did you see on line 1?
Ans: random numbers from 5 to 20 
What was the smallest number you could have seen, what was the largest?
5 was smallest and 20 was the largest
What did you see on line 2?
Ans: odd numbers from 3 to 9
What was the smallest number you could have seen, what was the largest?
Ans: 3 is the smallest and 9 is the largest
Could line 2 have produced a 4?
Ans: Line 2 cannot produce a 4 as an even
What did you see on line 3?
Ans: Floating numbers from 2.4 to 5.5
What was the smallest number you could have seen, what was the largest?
Ans: Smallest is 2.4999.... and largest was 5.49999
"""

# Code produce random number from 1 to 100 inclusive:
print(random.randint(1, 100))
