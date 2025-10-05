def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Invalid number.")
        return None
    else:
        return result


