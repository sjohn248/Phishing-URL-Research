websites = {'google':0, 'twitter':0, 'yahoo':0, 'instagram':0, 'wiki':0, 'linkedin':0, 'microsoft':0, 
            'youtube':0, 'zoom':0, 'amazon':0, 'discord':0, 'twitch':0, 'paypal':0, 'tiktok':0, 'ebay':0}


def getStats(lines, filename, websites):
    totalCount = 0
    for line in lines:
        line = line.lower()
        for website in websites:
            if website in line:
                websites[website] = websites[website] + 1
                if website == 'wiki':
                    print(line)
        totalCount = totalCount + 1
    openPhish.close()
    file = open(filename, 'w')
    for website in websites:
        file.write(f"{website} occurs {websites[website]} times of {totalCount} urls\n")
    file.close()
    websites = websites.fromkeys(websites,0)

openPhish = open('openphish_url_and_timestamp.csv', 'r')
lines = openPhish.readlines()
getStats(lines, 'openphishPopWebsiteOccurance.txt', websites)
openPhish.close()

phishTank = open('phishtank_url_and_timestamp.csv', 'r')
lines = phishTank.readlines()
getStats(lines, 'phishtankPopWebsiteOccurance.txt', websites)
phishTank.close()


