test_case = []

while True:
    n = input()
    test_case.append(n)
    if n == "0":
        break
    
print(test_case)

def pelindrome(numbers):
    result = []
    for i in range(len(numbers) // 2):
        if numbers[i] != numbers[-i - 1]:
            result.append(False)
        else:
            result.append(True)
    return result

for i in range(len(test_case) - 1):
    if False in pelindrome(test_case[i]):
        print("no")
    else:
        print("yes")
        