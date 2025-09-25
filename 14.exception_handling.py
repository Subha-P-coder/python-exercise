def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Division by zero is not allowed.")
    except TypeError:
        print("❌ Error: Both inputs must be numbers.")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("➡️ Division attempt finished (finally block executes always).")

# Test cases
divide_numbers(10, 2)    # normal case
divide_numbers(5, 0)     # zero division
divide_numbers(8, "a")   # type error
