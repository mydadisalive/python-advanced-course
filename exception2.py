try:
    x = 10
    if x > 5:
        raise Exception("x should be less than or equal to 5")
    elif x < 0:
        raise Exception("x should be a non-negative number")
    elif x % 2 == 0:
        raise Exception("x should be an odd number")
except Exception as e:
    print(f"Custom Exception: {e}")
finally:
    print("the end")