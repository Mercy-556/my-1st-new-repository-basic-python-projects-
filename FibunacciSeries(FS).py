"""The bolow code calculates and plots the fibunacci series"""

import matplotlib.pyplot as plt
    
def plot_function(x, y):
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


def fibunacci_calculator(terms): # the binacci list calculator [1, 2, ...]
    sequence = [1]
    for counter in range(0, terms - 1):
        sequence.append(sequence[counter])
        sequence[counter + 1] += sequence[counter - 1]

    return sequence

try:
    terms = int(input(f"Enter the number of terms: "))
except ValueError:
    print(f"Invalid input!")
else:
    #  Now I will plot the fibunacci series

    y = fibunacci_calculator(terms)
    x = [x for x in range(len(y))]

    plot_function(x, y)



