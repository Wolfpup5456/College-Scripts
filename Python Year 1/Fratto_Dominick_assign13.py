try:
    file_read = open("grades.txt", "r")
    line = file_read.readline().rstrip()
    input = []
    final = ""

except:
    print("ERROR")
    print("file does not exist in same folder as script")
    print("ERROR")

# puts file's contents into input list
while line != "":
    input.append(line)
    line = file_read.readline().rstrip()

# starts at top of the input list, works its way down until it finds the highest grade
for countdown in range(100, 0, -1):
    countdown = str(countdown)
    grade = [x for x in input if x.endswith(countdown)]
    if grade != []:
        break

gradecount = len(grade)

# makes gradelist a string
grade_str = ""
# if there are multiple highest scores
if gradecount >= 2:
    convert = ";".join(grade)
else:
    convert = grade_str.join(grade)


# splits grade into (name, number), puts back into a list named final
final = convert.split(";")
num_records = len(input)

# if there are multiple highest scores
if gradecount >= 2:
    print("Highest Score:", final[1])
else:
    print("Highest Score:", final[0] + ",", final[1])

# if there are multiple highest scores
if gradecount >= 2:
    print("there were multiple people with the highest grade!", gradecount, "people made the highest grade.")
print("Number of records:", num_records)
