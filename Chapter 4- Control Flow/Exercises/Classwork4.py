# check the grade
marks = int(input("Enter marks: "))
if (marks > 40):
  print("You have passed the subject")
else:
    print("You have not passed the subject")

    marks = int(input("Enter marks: "))
if (marks > 80 and marks <=90):
  print("You got A+")
elif (marks >70 and marks <=80):
  print("You got A")
elif (marks >60 and marks <=70):
  print("You got B")
elif (marks >50 and marks <=60):
  print("You got C")
elif (marks >40 and marks <=50):
  print("You got D")
else:
  print("You got F")