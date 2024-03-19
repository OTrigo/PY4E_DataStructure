file_name = input("Enter file name: ")
file_handler = open(file_name)
allValues = 0
countingLines = 0
for line in file_handler:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    countingLines+=1
    valueInLine = line[line.find(":")+1:].strip()
    allValues += float(valueInLine)
print("Average spam confidence:", allValues/countingLines)
