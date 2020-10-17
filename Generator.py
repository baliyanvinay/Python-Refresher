import json

# Using json file for states and districts in India file
# Source: https://github.com/sab99r/Indian-States-And-Districts

# Opening json file
f = open('states-and-districts.json')

# Loading data as a Python Dictionary using jason
state_dict = json.load(f)


def district_generator():
    '''
    Yields one state and its districts
    '''
    # type(state_dict['states']) is a list object
    for state in state_dict['states']:
        yield f"State: {state['state']} \nDistricts: {len(state['districts'])} \n{state['districts']}"


# Generator-function returning a generator object
generator_object = district_generator()

# One way to access data from a generator object is to use dunder next
choice = 'Y'
while(choice == 'Y'):
    # Print one state data for each choice
    print(generator_object.__next__())
    choice = input('View details of next state(Y/N):').upper()

# Another way is to use it in a loop
# for state_data in generator_object:
    # print(state_data)
