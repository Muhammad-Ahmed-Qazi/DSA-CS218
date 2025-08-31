# Write a Python script to concatenate following dictionaries to create a new one. Find the
# addresses of the three dictionaries and the concatenated dictionary as well. Note you’re your
# observations. Can you find the address of individual key-value pair?
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
# dic4 = dic1 + dic2 + dic3  # This will raise an error in Python
# Correct way to concatenate dictionaries in Python 3.9+
dic4 = dic1 | dic2 | dic3

# Print addresses of the dictionaries
print("Address of dic1:", id(dic1))
print("Address of dic2:", id(dic2))
print("Address of dic3:", id(dic3))
print("Address of concatenated dic4:", id(dic4), end='\n\n')

# Print addresses of individual key-value pairs in dic4
for key in dic4:
    print(f"Address of key-value pair ({key}: {dic4[key]}):", id((key, dic4[key])))

