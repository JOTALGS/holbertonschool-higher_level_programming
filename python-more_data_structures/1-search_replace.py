#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for e in range(len(my_list)):
        new_list.append(my_list[e])
        if new_list[e] == search:
            new_list[e] = replace
    return (new_list)

<<<<<<< HEAD

=======
>>>>>>> 6afeb81535fb769444f280c34e019e5ffa9b8ef8
