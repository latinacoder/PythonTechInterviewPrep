#example 1
#Given a list of numbers, return whether the list contains Pythagorean Triplets (a**2 + b**2 = c**2)
## In other words: can you create a function that checks if a given list of measurements represents a [set] of sides for a right-angled triangle in a construction project?

#Step 1: Iterate through the list and calculate the square of each number
#Step 2: Create a set to store the squares of the numbers. This will ensure each square is stored only once, to avoid duplicates
#Step 3: Iterate through the list again and for each number, iterate through the set of squares. 
#Step 4: Check if the sum of any two distinct squares equals the square of a third number. If so, return True. 
        #Step 5: If not, return False. 



def has_pythagorean_triplets(nums):
    squares = set() #create an empty set to store the squares of numbers

    for num in nums: #iterate through the list of numbers
        squares.add(num * num) #Calculate the square of each number and add it to the set

