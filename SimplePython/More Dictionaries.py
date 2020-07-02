# creates a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonvile'}
# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities["OR"])

# print some states
print('-'*10)
print("michigan's abbreviation us: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

