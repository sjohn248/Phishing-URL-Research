file1 = open('openphish_occurances.csv', 'r')

file3 = open('openphishDuplicates.csv', 'w')

print("running")
lines = file1.readlines()
lineCount = len(lines)
duplicates = []

for index in range(lineCount):
    url1 = lines[index].split(',')
    try:
        if int(url1[1].strip('\n')) > 96:
            file3.write(f"{url1[0]}, {url1[1]}")
    except:
        pass
file3.close()