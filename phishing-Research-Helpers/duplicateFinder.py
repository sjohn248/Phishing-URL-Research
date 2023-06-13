file1 = open('openphish_occurances.csv', 'r')

#file2 = open('Shared.csv', 'w')

print("running")
lines1 = file1.readlines()

phishTankList = []
duplicates = []

count = 0
for line1 in lines1:
    
    line1 = line1.rstrip()
    count = line1[-1:]

    #print(count)
    if count != "48":
        print(line1)
        print(count)
    

