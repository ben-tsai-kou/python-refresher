# test 1
def convert_currency(amount: int, rate: float = 30.5) -> float:
    """
    this is a convert currency function with 2 parameters which are amount:int and rate:float.
    it returns a float.
    """
    return amount * rate


print(convert_currency(100))  # expect: 3050.0
print(convert_currency(100, 0.5))  # expect: 50.0


# --------------------------------------------------------
# test 2
def analyze_scores(scores_list: list[int]) -> tuple[int, int, float]:
    high = max(scores_list)
    low = min(scores_list)
    avg = sum(scores_list) / len(scores_list)

    return (high, low, avg)


scores = [100, 50, 75, 80]
high, low, avg = analyze_scores(scores)
print(f"Max: {high}, Min: {low}, Avg: {avg}")


# --------------------------------------------------------
# test 3
def add_student(name, student_list=[]):
    student_list.append(name)
    return student_list


# first time
class_a = add_student("Ben")
print(f"Class A: {class_a}")

# second time
class_b = add_student("Alice")
print(f"Class B: {class_b}")

# which one would be print?
# 1. Class A: ['Ben'], Class B: ['Alice']
# 2. Class A: ['Ben'], Class B: ['Ben', 'Alice']
# 3. Class A: ['Ben'], Class B: ['Alice', 'Ben']
