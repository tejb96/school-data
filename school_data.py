# school_data.py
# AUTHOR NAME Tejpreet Bal
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
single_arrays = [year_2013, year_2014, year_2015, year_2016, year_2017,
                     year_2018, year_2019, year_2020, year_2021, year_2022]


# You may add your own additional classes, functions, variables, etc.
def create_3d_array(years):
    """
    Create a three-dimensional NumPy array by stacking the given years.

    Args:
        years (list): List of NumPy arrays representing each year's data.

    Returns:
        numpy.ndarray: A three-dimensional array representing the stacked data.
    """
    arr = np.stack(years, axis=0)
    return arr 
    


def main():
    print("ENSF 592 School Enrollment Statistics")

    # Print Stage 1 requirements here
    three_dimensional_arr = create_3d_array(single_arrays)
    three_dimensional_arr = three_dimensional_arr.reshape(10,20,3)
    print("Shape of full data array:", three_dimensional_arr.shape)
    print("Dimensions of full data array:",three_dimensional_arr.ndim)
    # Prompt for user input

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

