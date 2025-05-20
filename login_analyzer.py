# login_analyzer.py
# Simulates login attempts and monitors CPU usage


# Sample login attempt simulation
username = input("Enter your username: ")
password = input("Enter your password: ") 

# Simulate correct credentials

correct_username = "admin"
correct_password = "koach187"

# Check credentials using if/else

if username == correct_username and password == correct_password:
    print("Login successful. Welcome, admin!")
else:
    print("Login failed, Incorrect credentials.")

# SIMULATED CPU USAGE VALUES (PERCENTAGES)

cpu_usages = [45, 55, 67, 73, 81, 65, 90, 78]

print("\nmonitoring CPU usage...")
for usage in cpu_usages:
    if usage > 80:
        print(f"Alert! CPU usage high: {usage}%")
    else:
        print(f"CPU usage is normal: {usage}%")