import random
import string
import time

alphabet = list(string.printable)

def checkString(string, wordList):
    for i in string:
        if i not in wordList:
            return False
    return True

def cinematicModeCheck(answer):
    answer = answer.lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        return "what"


while True:
    target = input("What is the target string: ")
    checking = checkString(target, alphabet)
    if checking:
        break
    else:
        print("Sorry no åäö :(")
while True:
    try:
        tries = int(input("How many generations should undergo: ")) + 1
        break
    except ValueError:
        print("Enter a number please.")
        time.sleep(0.25)
while True:
    cinematic = cinematicModeCheck(input("Would you like cinematic mode [y/n]: "))
    if cinematic != "what":
        break


def listStr(wordlist):
  output = ""
  for i in wordlist:
    output += i
  return output

def randomString(length, charList):
  output = ""
  for i in range(0, length):
    output += random.choice(charList)
  return output
  
def calculateScore(targetStr, attemptStr):
  output = []
  score = 0
  correctIndices = []
  if len(targetStr) != len(attemptStr):
    return output
  else:
    stringLength = len(targetStr)
  addScore = 1 / stringLength
  for i in range(0, stringLength):
    if targetStr[i] == attemptStr[i]:
      score += addScore
      correctIndices.append(i)
  output.append(score)
  output.append(correctIndices)
  return output
  
def randEvolve(attemptStr, wordList, exceptions):
  attemptStr = list(attemptStr)
  for i in range(0, len(attemptStr)):
    if i in exceptions:
      pass
    else:
      newChar = random.choice(wordList)
      attemptStr[i] = newChar
  attemptStr = listStr(attemptStr)
  return attemptStr
      
  
attempt = randomString(len(target), alphabet)
scoreList = calculateScore(attempt, target)
score = scoreList[0]
indices = scoreList[1]
print("Generation 0 (Base):", attempt + ", Score:", str(score))
for i in range(1, tries):
    attempt = randEvolve(attempt, alphabet, indices)
    scoreList = calculateScore(attempt, target)
    score = scoreList[0]
    indices = scoreList[1]
    print("Generation", str(i) + ":", attempt + ", Score:", str(score))
    if cinematic:
        time.sleep(0.02)
    if score >= 0.9999999999999990:
        print("STRING FOUND")
        print("The string is: " + attempt)
        break
else:
    print("The successful string was not found!")
input("Press enter to exit the program... ")
