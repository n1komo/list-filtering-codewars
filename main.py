def filter_list(l):
    filtered_list = []  # our new list with integers in the future, blank initialization.
    # this loop checks if the input is integer and if it's actually an integer, pushes it into a new blank list
    for i in l:
        if isinstance(i, int):
            filtered_list.append(i)
    #  print(filtered_list)
    return filtered_list  # returns our new list with only just an integers.


filter_list([1, 2, 'a', 'b'])
filter_list([1, 2, 'a', 'b'])
filter_list([1, 'a', 'b', 0, 15])
filter_list([1, 2, 'aasf', '1', '123', 123])