file1 = open('gsb_4Byte_Hash_and_Time.csv', 'r')
file2 = open('phishtankSharedHash.csv', 'r')

file3 = open('gsbShared.csv', 'w')

print("running")
lines1 = file1.readlines()
lines2 = file2.readlines()

for line1 in lines1:
    url1 = line1.split(',')
    for line2 in lines2:
        url2 = line2.split(',')
        if url1[0] == url2[0]:
            print("added")
            file3.write(line1)
            file3.write('\n')
            break

file3.close()