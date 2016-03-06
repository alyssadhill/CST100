# ask user what height of trapezoid is and store the number
height = input("Enter the height of the trapezoid: ")

# ask user what length of the bottom base of trapezoid is and store the number
bottom_base = input("Enter the length of the bottom base of the trapezoid: ")

# ask user what length of the top base of trapezoid is and store the number
top_base = input("Enter the length of the top base of the trapezoid: ")

# turn strings into integer (reassigning variables)
height = int(height)
bottom_base = int(bottom_base)
top_base = int(top_base)

# Formula for area of trapezoid with variables
Area = 1/2 * (bottom_base + top_base) * height

# Telling user what the output number is and showing user the answer
print("The area of the trapezoid is: ", Area)
