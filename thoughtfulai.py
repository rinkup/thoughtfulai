def is_bulky(width, height, length):
    """
    Determines if the package is bulky.
    
    Parameters:
    width (int): Width of the package in cm.
    height (int): Height of the package in cm.
    length (int): Length of the package in cm.

    Returns:
    bool: True if the package is bulky, False otherwise.
    """
    volume = width * height * length
    return (
        volume >= 1000000
        or width >= 150 
        or height >= 150 
        or length >= 150
    )


def is_heavy(mass):
    """
    Determines if the package is heavy.
    
    Parameters:
    mass (int): Mass of the package in kg.

    Returns:
    bool: True if the package is heavy, False otherwise.
    """
    return mass >= 20


def sort(width, height, length, mass):
    """
    Function to sort packages into STANDARD, SPECIAL, or REJECTED stacks based on
    their dimensions and mass.
    
    Parameters:
    width (int): Width of the package in cm.
    height (int): Height of the package in cm.
    length (int): Length of the package in cm.
    mass (int): Mass of the package in kg.

    Returns:
    str: The stack where the package should go: 'STANDARD', 'SPECIAL', or 'REJECTED'.
    """
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    # Decision logic
    if bulky and heavy:
        return "REJECTED"  # Both bulky and heavy
    elif bulky or heavy:
        return "SPECIAL"  # Either bulky or heavy
    else:
        return "STANDARD"  # Neither bulky nor heavy


# Example usage:
print(sort(100, 100, 99, 10))  # Neither bulky nor heavy
print(sort(200, 50, 20, 10))    # Bulky but not heavy
print(sort(50, 50, 50, 25))     # Heavy but not bulky
print(sort(200, 200, 200, 25)) # Both bulky and heavy
print(sort(150, 150, 150, 20)) # Edge case: both conditions just met