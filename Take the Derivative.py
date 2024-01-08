def derive(coefficient, exponent): 
    new_coefficient = coefficient * exponent
    new_exponent = exponent - 1
    return f"{new_coefficient}x^{new_exponent}" if new_exponent > 0 else str(new_coefficient)