import os

# Get the value of an environment variable
user_home = os.getenv("HOME")
print("User's Home Directory:", user_home)

# Set an environment variable (not recommended for system-wide changes)
os.environ["MY_VARIABLE"] = "my_value"
