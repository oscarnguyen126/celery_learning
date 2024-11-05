from tasks import divide

# Call the task with a division by zero
result = divide.delay(10, 0)

# Get the result, without propagating the exception
result_value = result.get(propagate=False)

# Check if the task failed
if result.failed():
    if isinstance(result_value, ZeroDivisionError):
        print("Handled ZeroDivisionError: cannot divide by zero")
    else:
        print(f"Handled an unexpected error: {result_value}")
else:
    print(f"Task succeeded: {result_value}")

# result.get(propagate=False) will not raise the ZeroDivisionError.
# result.failed() will return True, indicating that the task failed.
# result_value will contain the exception raised during the task execution (ZeroDivisionError in this case).
