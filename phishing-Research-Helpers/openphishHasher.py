import hashlib

file1 = open('phishtank_url_and_timestamp.csv', 'r')

file3 = open('phishTankURLHash.csv', 'w')

print("running")
lines1 = file1.readlines()

for line1 in lines1:
    url1 = line1.split(',')
    hash1 = hashlib.sha256(str(url1[0]).encode('utf-8')).hexdigest().upper()
    file3.write(hash1[0]+hash1[1]+hash1[2]+hash1[3]+hash1[4]+hash1[5]+hash1[6]+hash1[7]+','+line1)

file3.close()