# 1. Create a function, `halved` that takes an list of numbers and returns an new list consisting of those numbers, halved.
def halved(lis):
    return [(x/2) for x in lis]
# 2. Create a function, `only_positive`, that takes an list of numbers and returns a new list consisting only of the positive numbers.
def only_positive (lis):
    return [x>0 for x in lis]
# 3. Write a function, `sum`, that takes an list of numbers and returns the sum of those numbers.
def sum1(lis):
    total = 0
    return [total+x for x in lis]
# 4. Create a function called `stripped_strings` that takes an list of strings and returns a new list of the strings with all non-alphanumeric characters removed.
def stripped_strings(lis):
    return [x.isalpha.isnumber for x in lis]
# 5. Create function, `find_special`, that takes an list of words and returns the index of the first occurrence of the word "special". If the word "special" is not present, it should return, `-1`.
def find_special(lis):
    if [ i for i in lis if 'special' in i]:
        return lis[i][0]
    return -1
# 6. Create a function called `valid_contacts`. This function takes an list of `contact` dictionaries (`name` and `phone_number` property, remember?). It should return an list of only `contact` objects that have a `phone_number` that is a 10-digit string.
#       ```python
#       contacts = [
#         {"name": 'Reuben', "phone_number": '9196218777'},
#         {"name": 'Laisha', "phone_number": '0123334766'},
#         {"name": 'Cielo', "phone_number": '764'},
#         {"name": 'Maya', "phone_number": '7653324599'}
#       ]

#       valid_contacts(contacts) == [
#         {name: 'Reuben', "phone_number": '9196218777'},
#         {name: 'Laisha', "phone_number": '0123334766'},
#         {name: 'Maya', "phone_number": '7653324599'}
#       ]
def valid_contacts(lis):
    contact = []
# 7. Create a function, `contact_names`, that takes an list of `contact` objects and returns an list of `contact` `name`s.
#       ```python
#       contacts = [
#         {name: 'Reuben', "phone_number": '9196218777'},
#         {name: 'Laisha', "phone_number": '0123334766'},
#         {name: 'Cielo', "phone_number": '764'},
#         {name: 'Maya', "phone_number": '7653324599'}
#       ]

#       contact_names(contacts) == ['Reuben', 'Laisha', 'Cielo', 'Maya']
#       ```