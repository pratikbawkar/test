

def add_values(value1, value2):
    """
    This is the multiline string to descript what this is function is doing

    Adding two values
    when two numerical values are provided this function
    calculate the sum of the two values and return the
    result

    Parameters
    ----------
    value1: float
        First value
    value2: float
        Second value

    
    Returns
    -----------
    float   
        the sum of value1 and value2
    """
    return value1 + value2


def average_three_values(value1, value2, value3):
    return (value1 + value2 + value3)/3



print(add_values(12.45, 45.67))

print(average_three_values(4,5,6))

help(add_values)