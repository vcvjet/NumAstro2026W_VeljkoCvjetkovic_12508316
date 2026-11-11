

# here I usually describe what the script does
# and which functions it contains

# here we import some modules
import numpy as np  # one of the best modules for scientific computing; designed for working with arrays
import matplotlib.pyplot as plt  # a great module for plotting
import scipy # a module for scientific computing, containts more specialized functions than numpy

# you can have it as functions or just put the code in the main part
# other ways to save/load data are pickle, json, csv, etc.
def save_array(fname, array):
    np.savetxt(fname, array, delimiter=' ', fmt='%.2f') # default delimiter is space, format is float with 2 decimal points

# a sister function to np.savetxt
# has many parameters, e.g., you can skip the first row or column, specify the delimiter, etc.
# also see genfromtxt, which is better if you have NANs in your data
def load_array(filename):
    return np.loadtxt(filename, delimiter=' ')

# here we create a few arrays
# note the difference between arrays and lists. Arrays are more efficient for numerical operations
# Lists are more flexible and can contain different types of data
def create_arrays():
    # Create an array from a list
    array1 = np.array([1, 2, 3, 4, 5])
    print("Original Array:", array1)

    # Create a 2D array
    array2 = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D Array:\n", array2)

    # Reshaping the array - note this function, it is very useful
    reshaped = array2.reshape(3, 2)
    print("Reshaped Array:\n", reshaped)

    # Element-wise operations
    multiplied = array1 * 2
    print("Array Multiplied by 2:", multiplied)

    return array1, reshaped

# Plotting the data using fig, ax syntax
# very flexible: you can have multiple subplots, specify the size, choose the colors, etc.
def plot_data(x, y):
    fig, ax = plt.subplots()  # Create a figure and a single set of axes. Here you can specify how many subplots you want
    ax.plot(x, y, marker='o', color='b', label='Line plot')  # Plotting on the axes. You can have ax1.plot, ax2.plot, etc.
    ax.set_title('Simple Line Plot') # self-explanatory
    ax.set_xlabel('Our X-axis')  # self-explanatory
    ax.set_ylabel('Our Y-axis')  # self-explanatory
    ax.legend()  # you can also specify the location and text of the legend
    ax.grid(True)  # Adding gridlines; you can specify the color, linestyle, etc.
    plt.savefig('Figure.png')  # Save the plot as a .png file
    plt.show()  # Display the plot


# Main function to run the script
# When you run this script from the command line,
# the main() function will be executed
# However, if you import this script as a module in another Python file,
# the main() function will not be executed,
# since the if __name__ == '__main__' statement will evaluate to False.
if __name__ == "__main__":
    # create arrays
    array1, reshaped_array = create_arrays()

    save_array('array_data.txt', reshaped_array)
    print("Array saved to array_data.txt")

    loaded_array = load_array('array_data.txt')
    print("Loaded Array from text file:\n", loaded_array)


    x = np.linspace(0, 10, 50)  # Generate 50 points between 0 and 10
    y = np.sin(x)  # Calculate the sine of each point
    plot_data(x, y)




