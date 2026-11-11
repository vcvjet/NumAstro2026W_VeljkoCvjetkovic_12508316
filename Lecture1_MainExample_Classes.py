"""
The same programme as MainExample, but with classes. 
The programme uses a dictionary to load the parameters from a
text file called config.txt
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy  
from pathlib import Path


class ArrayClass:
    """
    This class encapsulates array creation, saving/loading, and plotting.
    Options that the class is getting from the text file:
    1) array_size: int (length of 1D array)
    2) output_dir: folder where it saves the data and figures 
    3) array_filename: name of the .txt file to save array data
    4) figure_filename: name of the .png file to save the figure
    """

    def __init__(self, config_path: str):
        # Parse config from text file
        self.config = self._load_config(config_path)

        self.output_dir = Path(self.config.get("output_dir", "outputs")) # can also use the os module functionality for that
        self.output_dir.mkdir(parents=True, exist_ok=True) # and for this

        self.array_fname = self.output_dir / self.config.get("array_filename", "array_data.txt")
        self.figure_fname = self.output_dir / self.config.get("figure_filename", "Figure.png")

        self.array1 = None
        self.reshaped = None

    @staticmethod
    def _load_config(path: str) -> dict:
        """Reads simple key=value lines from a text config file."""
        config = {}
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = [x.strip() for x in line.split("=", 1)]
                    # Try to convert to int if possible; use "try" to handle the exceptions
                    try: 
                        value = int(value)
                    except ValueError:
                        pass
                    config[key] = value
        return config

    # --- Array and file operations ---
    @staticmethod
    def save_array(fname: Path, array: np.ndarray):
        np.savetxt(fname, array, delimiter=" ", fmt="%.2f")

    @staticmethod
    def load_array(fname: Path) -> np.ndarray:
        return np.loadtxt(fname, delimiter=" ")

    # --- Core logic ---
    def create_arrays(self):
        size = self.config.get("array_size", 5)
        print(f"Creating arrays of size {size}...")

        self.array1 = np.arange(1, size + 1)
        print("Original 1D Array:", self.array1)

        array2 = np.array([[1, 2, 3], [4, 5, 6]])
        print("2D Array:\n", array2)

        self.reshaped = array2.reshape(3, 2)
        print("Reshaped Array:\n", self.reshaped)

        multiplied = self.array1 * 2
        print("Array multiplied by 2:", multiplied)

        return self.array1, self.reshaped

    def plot_data(self, x, y):
        fig, ax = plt.subplots()
        ax.plot(x, y, marker="o", color="b", label="Line plot")
        ax.set_title("Simple Line Plot")
        ax.set_xlabel("Our X-axis")
        ax.set_ylabel("Our Y-axis")
        ax.legend()
        ax.grid(True)

        plt.savefig(self.figure_fname)
        print(f"Figure saved to {self.figure_fname.resolve()}")
        plt.show()

    def run(self):
        array1, reshaped = self.create_arrays()

        # Save and load array
        self.save_array(self.array_fname, reshaped)
        print(f"Array saved to {self.array_fname.resolve()}")

        loaded = self.load_array(self.array_fname)
        print("Loaded Array from file:\n", loaded)

        # Plot example data
        x = np.linspace(0, 10, 50)
        y = np.sin(x)
        self.plot_data(x, y)


# --- Main Execution ---
if __name__ == "__main__":
    CONFIG_PATH = "config.txt"
    NewRun = ArrayClass(CONFIG_PATH)
    NewRun.run()

