# going off of my school's grading scale:
# 90 - 100 is 4.0 unweighted, 5.0 weighted
# 80 - 90 is 3.0 unweighted, 4.0 weighted
# 70 - 80 is 2.0 unweighted, 3.0 weighted
# 60 - 70 is 1.0 unweighted/weighted
# 0 - 60 is 0.0 unweighted/weighted

print("Hello, this is a GPA calculator. \n")

# gets number of classes, makes sure it is a positive integer
while True:
    try:
        numClasses = int(input("How many classes would you like to enter? "))
        break
    except ValueError:
        print("Please enter an integer: ")
while numClasses <= 0:
    if numClasses < 0:
        print("Please enter a positive number: ")
        numClasses = int(input("How many classes would you like to enter? "))
    else:
        print("How can you have 0 classes?")
        numClasses = int(input("How many classes would you like to enter? "))

# defines a list of grades
gradeList = []

# iterates through number of classes, getting grades and whether it is weighted or not
for i in range(numClasses):
    print("\nClass #" + str(i+1))
    while True:
        try:
            grade = int(input("Enter your grade in percent: "))
            break
        except ValueError:
            print("Please enter an integer: ")
    while grade < 0 or grade > 100:
        if grade < 0:
            print("Please enter a positive number: ")
        else:
            print("Please enter a grade in between 0 - 100")
        grade = int(input("Enter your grade in percent: "))
    isWeighted = input("Is it weighted? (yes/no): ").lower()
    while isWeighted != "yes" and isWeighted != "no":
        print("Please give a yes or no response: ")
        isWeighted = input("Is it weighted? (yes/no)").lower()
    # makes isWeighted into a boolean
    if isWeighted == "yes":
        isWeighted = True
    else:
        isWeighted = False
    # appends grade and isWeighted to gradeList as a tuple
    gradeList.append((grade, isWeighted))


def calculate(grades):
    unweighted_sum = 0
    weighted_sum = 0
    for gradePair in grades:
        if gradePair[1]:
            if gradePair[0] < 60:
                pass
            elif gradePair[0] < 70:
                unweighted_sum += 1
                weighted_sum += 1
            elif gradePair[0] < 80:
                unweighted_sum += 2
                weighted_sum += 3
            elif gradePair[0] < 90:
                unweighted_sum += 3
                weighted_sum += 4
            else:
                unweighted_sum += 4
                weighted_sum += 5
        else:
            if gradePair[0] < 60:
                pass
            elif gradePair[0] < 70:
                unweighted_sum += 1
                weighted_sum += 1
            elif gradePair[0] < 80:
                unweighted_sum += 2
                weighted_sum += 2
            elif gradePair[0] < 90:
                unweighted_sum += 3
                weighted_sum += 3
            else:
                unweighted_sum += 4
                weighted_sum += 4
    unweighted = round(unweighted_sum/len(gradeList), 2)
    weighted = round(weighted_sum/len(gradeList), 2)
    return unweighted, weighted


typeGPA = input("\nDo you want your GPA unweighted, weighted, or both? ").lower()
while typeGPA != "unweighted" and typeGPA != "weighted" and typeGPA != "both":
    print('Please enter "unweighted", "weighted", or "both": ')
    typeGPA = input("Do you want your GPA unweighted, weighted, or both? ").lower()

if typeGPA == "unweighted":
    print("Your unweighted GPA is " + str(calculate(gradeList)[0]) + ".")
elif typeGPA == "weighted":
    print("Your weighted GPA is " + str(calculate(gradeList)[1]) + ".")
else:
    print("Your unweighted GPA is " + str(calculate(gradeList)[0])
          + ", and your weighted GPA is " + str(calculate(gradeList)[1]) + ".")
