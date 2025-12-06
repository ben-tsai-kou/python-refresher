# my_list = [1, 2, 3, 4, 5]

# for x in my_list:
#     print(x)

# test_1
for i in range(10, 0, -2):
    print(i)

# test 2
users = ["Ben", "Alice", "Bob"]

for i, name in enumerate(users, start=1):
    print(f"Rank {i}: {name}")

# test 3
user_scores = {"Ben": 85, "Alice": 90, "Bob": 59}

for name, score in user_scores.items():
    if score < 60:
        print(f"{name} failed with {score}")
