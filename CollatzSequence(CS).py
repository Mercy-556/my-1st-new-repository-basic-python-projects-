import matplotlib.pyplot as plt

"""This script calculate the collats sequence using the number user provided"""

bag = [] # This is where the calculated values will be

def plot_function(x, y):
    plt.plot(
        x,
        y,
        color = "blue",
        linewidth = 2
    )

    # the plot design
    plt.title("The Collatz Sequence")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    
    return plt.show()

def sequence_calculator(value):
    if value % 2 == 0:
        value = value // 2
    else:
        value = 3*value + 1
    return value


try:
    number = int(input(f"Enter a number: "))
except ValueError:
    print(f"Invalid input!!!")
else:

    while number != 1:
        number = sequence_calculator(number)
        bag.append(number)
    else:
        bag.append(number)
        y = bag
        x = [x for x in range(len(y))]
        plot_function(x, y)

# --- --- --- --- --- --- --- --- --- --- --- --- ---