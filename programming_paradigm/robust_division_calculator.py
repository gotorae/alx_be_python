def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        y = numerator / denominator
    except ZeroDivisionError:
        print("can't divide by zero")
    except ValueError:
        print("not a number")
    else:
        return y


x = safe_divide("er", 2)
print(x)
