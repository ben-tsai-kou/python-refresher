# nums = [1, 2, 3]
# double = [x * 2 for x in nums]
# print(nums)
# print(double)

users = [
    {"id": 1, "name": "Ben", "age": 30, "role": "admin", "is_active": True},
    {"id": 2, "name": "Alice", "age": 25, "role": "user", "is_active": False},
    {"id": 3, "name": "Bob", "age": 40, "role": "user", "is_active": True},
    {"id": 4, "name": "Carol", "age": 22, "role": "user", "is_active": True},
]


task1 = [f"{user['name']}@company.com" for user in users if user["is_active"]]

print(task1)

task2 = sum([user["age"] for user in users])
print(task2)

task3 = [user for user in users if user["role"] != "admin" and user["age"] > 30]
print(task3)
