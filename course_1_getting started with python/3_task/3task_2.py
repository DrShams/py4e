score = input("Enter Score: ")
score = float(score)
if score <= 0.0 and score >=1.0:
    print("Please enter correct value number from 0.0 to 1.0")
    quit()
if score >= 0.9:
    score = "a"
elif score >= 0.8:
    score = "B"
elif score >= 0.7:
    score = c
elif score >= 0.6:
    score = "d"
else:
    score = f
print(score)
