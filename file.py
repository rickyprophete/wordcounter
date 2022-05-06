
validwords = {"JAVA": 0, "C++": 0, "GIT": 0, "GITHUB": 0, "GIT/GITHUB": 0, "JAVASCRIPT": 0, "C#": 0, "C": 0,
              "PYTHON": 0, "SQL": 0, "JQUERY": 0, "EXCEL": 0, "GO": 0, "ALGORITHMS": 0, "FLEXIBLE": 0, "R": 0,
              "DATA": 0,
              "LEARNING": 0, "MACHINE": 0, "DEVOPS": 0, "4": 0, "2": 0, "CSS": 0, "SWIFT": 0, "HTML": 0}

wordfile = open("C:\\Users\\Ricky Prophete\\CPlusPlusPrograms\\WordCounter\\jobs.csv", "r+")


if not wordfile.readable():
    print("That did not work")
lines = [" "]

while len(lines)>=1:
    lines = wordfile.read()
    lines = lines.upper()
    print(lines)

    for i in validwords:
        for j in lines:
            if i in j:
                validwords[i] += 1


print(validwords)

wordfile.close()
