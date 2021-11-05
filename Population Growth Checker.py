#Michael Hart

"""
This program implements a function growth_check(growth_pct) that takes as an argument a floating point number and
makes use of the data in the file pop_est_2010_2018.csvPreview the document.
The file has the populations of various US geographies from 2010 to 2018.
The function will calculate the percent growth between each consecutive year for each geography
(there is one geography, mostly US states, per line in the file).
After running it will print out all the names of the geographies for which there was at least one year where growth was
equal or greater than the percent passed to the function through the growth_pct variable, together with the years in
which that growth occurred.
The years will be printed in ascending order.

growth_check(1.8) should result in the following output:

Colorado: 2015
District of Columbia: 2011, 2012, 2013, 2014, 2015
Florida: 2015, 2016
Idaho: 2016, 2017, 2018
Nevada: 2017, 2018
North Dakota: 2012, 2013, 2014, 2015
Oregon: 2016
Texas: 2014, 2015
Utah: 2016, 2017, 2018
Washington: 2016

"""


# This function takes a floating point number as an argument and makes use of  data in the file pop_est_2010_2018.csv.
def growth_check(growth_pct):
    
    # Open the file file pop_est_2010_2018.csv.
    pop_file = open("pop_est_2010_2018.csv")
    
    # Read the lines of the file.
    pop_file_content = pop_file.readlines()
    
    # Close the file.
    pop_file.close()
    
    # Create a metadata line to hold the country name and the years 2010-2018.
    metadata_items = ["country", 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    
    # Create an empty dictionary pop_dict to hold the states as keys and the 
    # percent growth between consecutive years between 2010 and 2018 as values.
    pop_dict = {}    
    
    # Split the pop_file_content into sub-lists.
    for line_index in pop_file_content:
        
        # Create a dictionary to hold the years as keys with the population as values.
        pop_by_year_dict = {}        
        
        # Split each line into a list for each state.
        state_row = line_index.split(",")
        
        # Set the current state as the first index in state_row.
        current_state = state_row[0]
        
        # Add each element from the metadata_items as a key to the pop_dict
        # with the corresponding index of the state_row as the value.
        for index in range(1, len(metadata_items)):
            pop_by_year_dict[metadata_items[index]] = eval(state_row[index])
        
        # Add the pop_by_year_dict to the pop_dict.
        pop_dict[current_state] = pop_by_year_dict

    # Go through each state key in pop_dict.
    for state in pop_dict:
        
        # Create a string statement to hold the state and years that should be printed.
        state_and_years = str(state) + ": "
        
        # Go through the years 2011-2018 to calculate the percent change between years.
        for curr_year in range(2011, 2019):
            
            # Set prev_year as (curr_year -1).
            prev_year = (curr_year - 1)
            
            # Set the current year population.
            curr_year_pop = pop_dict[state][curr_year]
            
            # Set the previous year population.
            prev_year_pop = pop_dict[state][prev_year]
            
            # Calculate the percent change.
            pct_change = ((curr_year_pop - prev_year_pop)/prev_year_pop) * 100
            
            # If the percent change is greater or equal to the growth_pct, concatenate the year to the state_and_years.
            if pct_change >= growth_pct:
                state_and_years += str(curr_year) + ", "
        
        # Print the state with the years, if a year was added.
        if state_and_years != str(state) + ": ":
            print(state_and_years)