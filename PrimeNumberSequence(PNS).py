import matplotlib.pyplot as plt

# plotting function 
def plot_function(x, y):
    plt.plot(
        x,
        y,
        color = "blue",
        linewidth = 2
    )

    # the plot design
    plt.title("The Prime Number")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    
    return plt.show()

# the prime number function calculator
def prime_calculator(bound): 
    prime = []
    # Loop directly through each number in the range (skipping 1, since it's not prime)
    for number in range(2, bound + 1):
    
        # Check all possible divisors between 2 and number - 1
        for div in range(2, number):
            if number % div == 0:
                break  # Found a factor! Not prime, so break out of the inner loop
            
        else:
            # The 'else' belongs to the 'for' loop, NOT the 'if' statement.
            # It executes ONLY if the inner loop finishes without hitting a 'break'.
            prime.append(number)
    return prime

try:
    bound = int(input(f"Enter the upper range: "))
except ValueError:
    print(f"Invalid input!")
else:
    y = prime_calculator(bound)
    x = [x for x in range(len(y))]

    plot_function(x,y)
    

