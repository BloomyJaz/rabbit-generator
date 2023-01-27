import time

# Initialize the number of rabbits
rabbits = 1

# Start an infinite loop
while True:
    # Multiply the current number of rabbits by 2
    rabbits *= 2
    # Print the current number of rabbits
    print("There are now", rabbits, "rabbits.")
    # Check if the number of rabbits is greater than or equal to 666
    if rabbits >= 666:
        # If the number of rabbits is greater than or equal to 666, exit the loop
        break
    # Wait for 1 second before continuing the loop
    time.sleep(1)

# Print message after the loop has finished  
print("")
print("Run, the rabbits are coming")
print("")
print("There isn't much time left for you")
time.sleep(5)