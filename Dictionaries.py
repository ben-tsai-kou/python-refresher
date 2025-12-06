# this_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# find key safely
# print(this_dict.get("name"))
raw_users = [
    {"name": "  Ben ", "email": "BEN@Example.com", "is_active": True},
    {"name": "Alice", "email": "alice@example.com", "is_active": False},
    {"name": "bob", "email": "Bob@example.com", "is_active": True},
    {"name": "  ", "email": "no-name@test.com", "is_active": True},
]

clean_data = [
    {
        "name": raw_user["name"].strip().capitalize(),
        "email": raw_user["email"].lower(),
        "is_active": raw_user["is_active"],
    }
    for raw_user in raw_users
    if raw_user["is_active"] and raw_user["name"].strip() != ""
]

print(clean_data)

transactions = [
    {"dept": "Sales", "amount": 100},
    {"dept": "Engineering", "amount": 500},
    {"dept": "Sales", "amount": 200},
    {"dept": "HR", "amount": 50},
    {"dept": "Engineering", "amount": 100},
]

result = {}
# below is okay but...
# for transaction in transactions:
#     dept = transaction["dept"]
#     dept = transaction["amount"]
#     if result.get(dept):
#         result[dept] += dept
#     else:
#         result[dept] = dept
# print(result)

# it is bette to use default value of .get()

for transaction in transactions:
    dept = transaction["dept"]
    amount = transaction["amount"]

    result[dept] = result.get(dept, 0) + amount

print(result)
