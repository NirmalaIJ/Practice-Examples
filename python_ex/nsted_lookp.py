##install from pypi using pip:
##
##pip install nested-lookup
##or install from source using:
##
##git clone ssh://git@git.unturf.com:2222/python/nested-lookup.git
##cd nested-lookup
##pip install .

from nested_lookup import nested_lookup
my_dcit = {"user":[{"name":"ad",
                   "skills":"python"
                    },
                   {"name":"adfd",
                   "skills":"python"
                       }],
           "details":["Asd",456]}
'''
print(nested_lookup("skills",my_dcit))



from nested_lookup import nested_update
print(nested_update(my_dcit, key='skills', value=' python test'))   #3returns dcit with value=' python test'
print(my_dcit)  # returns original dict

from nested_lookup import nested_delete
print(nested_delete(my_dcit, 'details'))

'''

def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found

print(get_recursively(my_dcit,"skills"))


#modifying above to get names of employees
def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = {}

    for key, value in search_dict.items():

        if key == field and value == "python":
            fields_found['name'] = search_dict['name']

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                print("SDF", result)
##                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        pass
##                        fields_found.append(another_result)

    return fields_found

print(get_recursively(my_dcit,"skills"))
