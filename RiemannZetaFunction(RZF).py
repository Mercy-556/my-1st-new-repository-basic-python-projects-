"""This script demostrates the Riemann zeta function for real numbers only"""

import matplotlib.pyplot as plt


def plot_function(x, y): # The ploot function
    plt.plot(
        x,
        y,
        color = "blue",
        linewidth = 2
    )

    # the plot design
    plt.title("The Fibunacci Serie")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid(True)
    
    return plt.show()


def zeta_function(upper_bound, variable): # the function definition
    series = []

    for counter in range(1, upper_bound + 1):
        zeta = 1/counter**variable
        series.append(round(zeta,2))

    return series


try:
    upper_bound = int(input(f"Enter the upper limit sum: "))
    variable = float(input(f"Enter the variable: "))
except ValueError:
    print(f"Invalid input!")
else:
    y = zeta_function(upper_bound, variable)
    x = [x for x in range(len(y))]
    plot_function(x, y)
