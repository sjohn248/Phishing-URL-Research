file1 = open('gsb_4Byte_Hash_and_Time.csv', 'r')
file2 = open('phishTankURLHash.csv', 'r')
file3 = open('openphishURLHash.csv', 'r')

file4 = open('gsbShared.csv', 'w')

print("running")
lines1 = file1.readlines()
lines2 = file2.readlines()
lines3 = file3.readlines()


gsbList = []
phishTankList = []
openPhishList = []
count = 0
for line1 in lines1:
    url1 = line1.split(',')
    gsbList.append(url1[0])
for line2 in lines2:
    url2 = line2.split(',')
    phishTankList.append(url2[0])

for line3 in lines3:
    url3 = line3.split(',')
    openPhishList.append(url3[0])

gsbAndPhishTank = set(gsbList).intersection(phishTankList)
print(gsbAndPhishTank)
file4.write(str(set(openPhishList).intersection(gsbAndPhishTank)))
print("DONE")
file4.close()