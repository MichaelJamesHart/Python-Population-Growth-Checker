# Python-Population-Growth-Checker
 Python script to check which US states experienced population growth.
 
This program implements a function growth_check(growth_pct) that takes as an argument a floating point number and
makes use of the data in the file pop_est_2010_2018.csv.

The file has the populations of various US geographies from 2010 to 2018.

The function will calculate the percent growth between each consecutive year for each geography
(there is one geography, mostly US states, per line in the file).

After running it will print out all the names of the geographies for which there was at least one year where growth was
equal or greater than the percent passed to the function through the growth_pct variable, together with the years in
which that growth occurred. The years will be printed in ascending order.

For example, growth_check(1.8) should result in the following output:

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
