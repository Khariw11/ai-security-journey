# login_analyzer.py
# Simulates login attempts and monitors CPU usage


import random # imports built in python random number module 
import time # imports built in python time module for timestamp help


# Simulate correct credentials

correct_username = "admin"
correct_password = "koach187"
max_attempts = 3
attempts = 0



# Check credentials using if/else

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ") 

    if username == correct_username and password == correct_password:
        print("Login successful. Welcome, admin!")
        print("\nMonitoring CPU usage (simulated)...")
        for i in range(10):
            usage = random.randint(30, 100)
            if usage > 80:
                print(f"Alert! CPU usage high: {usage}%")
            else:
                print(f"CPU usage is normal: {usage}%")
            time.sleep(1) # wait 1 second between readings 
        break
    else:
        print("Login failed, Incorrect credentials.")
        attempts += 1
if attempts == max_attempts:
    print("Account Locked. Too many failed attempts.")



