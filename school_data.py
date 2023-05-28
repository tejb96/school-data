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
all_years_list = [year_2013, year_2014, year_2015, year_2016, year_2017,
                     year_2018, year_2019, year_2020, year_2021, year_2022]

school_dictionary = {
    'Centennial High School': '1224',
    'Robert Thirsk School': '1679',
    'Louise Dean School': '9626',
    'Queen Elizabeth High School': '9806',
    'Forest Lawn High School': '9813',
    'Crescent Heights High School': '9815',
    'Western Canada High School': '9816',
    'Central Memorial High School': '9823',
    'James Fowler High School': '9825',
    'Ernest Manning High School': '9826',
    'William Aberhart High School': '9829',
    'National Sport School': '9830',
    'Henry Wise Wood High School': '9836',
    'Bowness High School': '9847',
    'Lord Beaverbrook High School': '9850',
    'Jack James High School': '9856',
    'Sir Winston Churchill High School': '9857',
    'Dr. E. P. Scarlett High School': '9858'
}

code_list = ['1224', '1679', '9626', '9806', '9813', '9815', '9816', '9823', '9825', '9826', '9829', '9830', '9836', '9847', '9850', '9856', '9857', '9858']


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
    
def check_name_code(name_code):
    """
    Check if the input is a valid school name or code.

    Args:
        name_code (str): The user input representing the school name or code.

    Returns:
        str: The corresponding school code if the input is a valid name,
             or the school name if the input is a valid code.

    Raises:
        ValueError: If the input is neither a valid name nor a valid code.
    """
    # Check if the input matches a school name
    if name_code in school_dictionary:
        school_code = school_dictionary[name_code]
        print("School name:", name_code + ",", "School code:", school_code)
        return school_code
    
    # Check if the input matches a school code
    for name, code in school_dictionary.items():
        if code == name_code:
            school_name =  name
            print("School name:", school_name + ",", "School code:", name_code)
            return name_code
    

    # If the input is neither a valid name nor a valid code, raise an error
    raise ValueError("You must enter a valid school name or code.")

def stage2_calculations(code_entered,three_dimensional_arr):
    """
    Perform stage 2 calculations and print statistics based on the given school code and data array.

    Args:
        code_entered (str): The school code entered by the user.
        three_dimensional_arr (numpy.ndarray): The three-dimensional data array.

    Returns:
        None
    """
    # Find the index of the given school code in the global variable code_list
    index = code_list.index(code_entered) 

    # Extract the subarray for the given school code
    subarray_view = three_dimensional_arr[:,index,:]

    # Calculate mean enrollment for each grade
    mean_values = np.nanmean(subarray_view, axis = 0)
    mean_values = mean_values.astype(int)

    # Calculate maximum and minimum enrollments for a single grade
    max_enrollment = np.nanmax(subarray_view)
    min_enrollment = np.nanmin(subarray_view)

    # Calculate total enrollment for each year
    total_enrolled_yearly= np.nansum(subarray_view, axis =1)
    total_enrolled_yearly = total_enrolled_yearly.astype(int)

    # Calculate the total enrollment over 10 years
    total_enrolled = np.nansum(subarray_view)

    # Calculate the mean total enrollment over 10 years
    mean_total_enrolled = np.nanmean(total_enrolled_yearly)

    # Print the calculated statistics
    print("Mean enrollment for grade 10:", mean_values[0])
    print("Mean enrollment for grade 11:", mean_values[1])
    print("Mean enrollment for grade 12:", mean_values[2])
    print("Highest enrollment for a single grade:", max_enrollment.astype(int))
    print("Lowest enrollment for a single grade:", min_enrollment.astype(int))

    for i, year in enumerate(range(2013, 2023)):
        print(f"Total enrollment for {year}:", total_enrolled_yearly[i])

    print("Total ten year enrollment:", total_enrolled.astype(int))
    print("Mean total enrollment over 10 years:", mean_total_enrolled.astype(int))

     # Calculate the median for all enrollments over 500
    flattened_array = subarray_view.flatten() # Flatten the subarray to consider all enrollments
    filtered_array = flattened_array[flattened_array > 500] # Filter the flattened array to include only values over 500
    if filtered_array.size == 0:
        print("No enrollments over 500.")
              
    else:
        median_enrollment = np.nanmedian(filtered_array)
        print("For all enrollments over 500, the median was:", median_enrollment.astype(int))


def stage3_calculations():
    """
    Perform various calculations and print general statistics based on the given data for stage 3 in main().

    Args:
        None

    Returns:
        None
    """
    # Calculations are done using the global variable all_years_lists
    mean_2013 = np.mean(all_years_list[0])
    print("Mean enrollment in 2013:", mean_2013.astype(int))

    mean_2022 = np.nanmean(all_years_list[-1])
    print("Mean enrollment in 2022:", mean_2022.astype(int))

    total_2022 = np.nansum(all_years_list[-1])
    print("Total class of 2022:", total_2022.astype(int))

    max_enrollment = np.nanmax(all_years_list)
    print("Highest enrollment for a single grade:", max_enrollment.astype(int))

    min_enrollment = np.nanmin(all_years_list)
    print("Lowest enrollment for a single grade:", min_enrollment.astype(int))

def main():
    print("ENSF 592 School Enrollment Statistics")

    # Print Stage 1 requirements here

    # Creates a 3d array of the list
    three_dimensional_arr = create_3d_array(all_years_list) 
    # Reshapes the array in the form of (years, schools, grades)
    three_dimensional_arr = three_dimensional_arr.reshape(10,20,3) 
    print("Shape of full data array:", three_dimensional_arr.shape)
    print("Dimensions of full data array:",three_dimensional_arr.ndim)  

    # Prompt for user input  

    name_code = input("Please enter the high school name or school code:")  
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    try:
        school_code1 = check_name_code(name_code) # Assigns school code                 
        stage2_calculations(school_code1, three_dimensional_arr) # Calls stage2_calculations
        
     

    # Print Stage 3 requirements here
        print("\n***General Statistics for All Schools***\n")

        stage3_calculations()

    except ValueError as value_err:
        print(str(value_err))  
if __name__ == '__main__':
    main()

