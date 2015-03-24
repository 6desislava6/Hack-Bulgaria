def iterations_of_nan_expand(expanded):
    lenght = len('Not a ')
    counter = 0
    is_same = expanded[counter * lenght: (counter + 1) * lenght] == 'Not a '
    while len(expanded) > len('Nan') and is_same:
        counter += 1
        expanded = expanded[lenght:]
        is_same = expanded[: lenght] == 'Not a '

    is_false = (counter == 0) or expanded != 'NaN'
    return counter if not is_false else 'False'

print (iterations_of_nan_expand(
    'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print (iterations_of_nan_expand("Show these people!"))
print (iterations_of_nan_expand("Not a NaN"))
print (iterations_of_nan_expand("Not a NaN ьяаьяа "))
