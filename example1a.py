#identify and retrieve the specific Pythagorean Triplet(s) present in a given list of numbers

def get_pythagorean_triplets(nums):
    # Create an empty list to store the Pythagorean Triplets
    triplets = []

    # Create a set to store the squares of the numbers
    squares = set()

    # Calculate the squares of the numbers and add them to the set
    for num in nums:
        squares.add(num * num)

    # Iterate through all pairs of numbers from the list
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # Calculate the sum of the squares of the two numbers
            square_sum = nums[i] * nums[i] + nums[j] * nums[j]
            
            # Check if the sum of squares exists in the set
            if square_sum in squares:
                # If it does, add the triplet (a, b, c) to the list of triplets
                triplet = (nums[i], nums[j], int(square_sum ** 0.5))
                triplets.append(triplet)

    # Return the list of Pythagorean Triplets
    return triplets
