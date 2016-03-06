# Create a function for a user to enter numbers 
def numList():
    # Set values to an empty list
    values = []
    # While loop that allows user to unput numbers until -9999 is entered
    while True:
        # Num is changed from string to interger
        num = int(input("Enter a number (-9999 to end): "))
        # End the loop once they enter -9999
        if num == -9999:
            break
        # Each new input is added to the end of the list
        values.append(num)
    return values

# Create a function to find the average of all the numbers 
def allNumAvg(values): 
    total = 0
    count = 0
    # For loop that finds the total and count to find the average
    for number in values:
        total = total + number
        count = count + 1  
    return total / count

# Create a function to find the average of only the positive numbers 
def posNumAvg(values):
    total = 0
    count = 0
    # For loop lookes for all numbers that are greater than 0
    for number in values:
        if number > 0:
            total = total + number
            count = count + 1  
    return total / count

#Create a function to find average of only the negative numbers
def nonPosAvg(values): 
    total = 0
    count = 0
    # For loop looks for all numbers less than or equal to zero
    for number in values:
        if number <= 0:
            total = total + number
            count = count + 1  
    return total / count

# Set values to numList
values = numList()
print ("The list of all numbers entered is: ")

print(values)

print("The dictionary with averages is: ")
# Create a dictionary with keys to display the averages
print ({"AvgPositive": posNumAvg(values), "AvgNonPos": nonPosAvg(values), "AvgAllNum": allNumAvg(values)})
