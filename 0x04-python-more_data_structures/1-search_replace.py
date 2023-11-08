#!/usr/bin/python3
def search_replace(my_list, search, replace):
    theNew_list = []
    for object in my_list:
        if object == search:
            theNew_list.append(replace)
        else:
            theNew_list.append(object)
    return theNew_list
