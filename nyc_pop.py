

#==================================================
# IMPORTANT NOTE
#
# When finished, this lab should generate a web page.
# Each of the functions are meant to make that process
# easier. When you are testing this code in Thonny, you
# should use print statements to make sure it is working.
#
# When it is time to generate your web page, you should
# comment out all your testing print statements.
#
# This file, and the data directory along with its contents,
# should be in your public_html/py/ folder so that it can load
# in a web browser at: http://homer.stuy.edu/~USERNAME/py/nyc_pop.py
#==================================================

#This is the data source we will be using
pop_file = open('data/nyc_pop.csv', encoding='utf-8')
text = pop_file.read().strip()

#==================================================
# Problem 0
#
# You should notice that the file contains population data for
# The boroughs of NYC from 1790 - 2010. It is formatted such that
# Each line represents one year, and contains a series of numbers
# separated by ','. This is a common way of representing data in
# plain text, since it is easily accessible in programming. The
# file type is called 'comma separated value' or 'csv'.
#
# Often, the first line of a .csv file will contain the headers
# that describe what each value represents.
#
# Write a function that will take a string representing the text
# of a file that looks similar to 'nyc_pop.csv' and returns a list
# that contains only the headers.
def get_headers(s):
    g = []
    return g


pop_headers = get_headers(text)
# Should print
# ['Year', 'Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
#print(pop_headers)

# End Problem 0
#==================================================

#==================================================
# Problem 1
#
# Write a function that will take a string representing the text
# of file that looks similar to 'nyc_pop.csv' and returns a list of
# lists.
# Each sublist should represent a line from the file.
# Each element in a sublist should represent one value.
# The list should not contain the headers.
def get_data(s):
    data = []

    return data


pop_data = get_data(text)
# Should print:
# [['1790', '33131', '4549', '6159', '1781', '3827', '49447'], ['1800', '60515', '5740', '6642', '1755', '4563', '79215'],
# There will be more sublists after that.
#print(pop_data)

# End Problem 1
#==================================================

#==================================================
# Problem 2
#
# Write a function that will take a list of lists similar to pop_data,
# where every element is a string, and creates a dictionary where the
# the keys are the years, as strings, and the values are the lists of
# population numbers for the given year, as numbers. Note that the
# key is also at index 0 in a given list.
#
# The first list is: ['1790', '33131', '4549', '6159', '1781', '3827']
# As a dictionary entry, it would look like this:
# {'1790': [33131, 4549, 6159, 1781, 3827]}
#
def make_year_dict(data):
    year_d = {}

    return year_d

pop_dict = make_year_dict(pop_data)
#print(pop_dict)

# End Problem 2
#==================================================

#==================================================
# Problem 3

# The data in each value of pop_dict represents borough information,
# but that is currently not clear.
#
# Write a function that takes a dictionary created by make_year_dict,
# and a list of headers.
# Ths function should modify each value in the paramater dictionary to
# be dictionaries where the keys are headers from the provided header list
# and the values are the corresponding numbers from the existing value list.
#
# For example, the first year entry is currently:
# {'1790': [33131, 4549, 6159, 1781, 3827],
# After this function runs, it should be:
# {'1790': {'Bronx': 1781, 'Brooklyn': 4549, 'Manhattan': 33131, 'Queens': 6159,'Staten Island': 3827},
#
# Note the header list contains 'Year', but that does not have a corresponding
# value in the value lists.

def combine_dict(year_dict, headers):
    for entry in year_dict:
        new_dict = {}

        year_dict[entry] = new_dict

combine_dict(pop_dict, pop_headers)
#print(pop_dict)

# End Problem 3
#==================================================

#==================================================
# Problem 4

# Write a function that will take as a parameter a dictionary
# created by make_year_dict and then modified by combine_dict.
# It should add a new entry to each year dictionary with a key of
# 'total' and a value that is the total population of all 5 boroughs.

def add_totals(d):
    for year in d:
        total = 0

        year_data['total'] = total

add_totals(pop_dict)
#print(pop_dict)

# End Problem 4
#==================================================

#==================================================
# Problem 5

# Write a function that takes as a paramater a dictionary
# created by make_year_dict and then modified by combine_dict,
# then modified by add_totals.
# The function should generate an html unorderd list where each
# item is a year followed by the total population for that year.

def make_total_list(d):
    html = ''

    return html

total_list = make_total_list(pop_dict)
#print(total_list)

# End Problem 5
#==================================================

#==================================================
# Problem 6

# Write a function that takes two paramters, the first a list
# that is the output of get_headers and the second a dictionary
# created by make_year_dict and then modified by combine_dict,
# then modified by add_totals.
# The function should generate an html table representing the
# data in the dictionary.
# The header row of the table should start with 'Year', then
# each borough, adn finally, 'Total'.
# Each row of the table should contain the year and the associated
# population values for that year.

def make_table(headers, d):
    html = ''

    return html

table = make_table(pop_headers, pop_dict)
#print(table)

# End Problem 6
#==================================================


#==================================================
# Problem 7

# Write a function that will use the functions above,
# the variable pop_dict, and the file template.html
# To generate a fully valid html file.
# The function should take as a paramater a dictionary,
# then read in the contents of template.html.
#
# template.html contains the basic valid html for a website,
# along with placeholder text (i.e. PAGE_TITLE)
#
# This function should return a string of html with all the
# placeholder text replaced by text/html generated from this
# program. You will provide the page title and headings,
# and you should use make_total_list and make_table to
# generate the list and table.

def generate_html(headers, d):
    html = ''

    return html

webpage = generate_html(pop_headers, pop_dict)
print(webpage)

# Once you have the correct output. Do whatever is necessary
# to make this a working python dynamic web page. As a reminder
# This file, and the data directory along with its contents,
# should be in your public_html/py/ folder so that it can load
# in a web browser at: http://homer.stuy.edu/~USERNAME/py/nyc_pop.py

# End Problem 7
#==================================================
