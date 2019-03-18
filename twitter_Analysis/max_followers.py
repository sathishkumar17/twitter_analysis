import collections
Read_File = "C:/Users/sathi/PycharmProjects/twitter_Analysis/NBA 2019.txt"

#Storing the read file into a Variable - with encoding format - latin-1
with open(Read_File, encoding="latin-1") as De_encode_File1:
    asiacup2018 = De_encode_File1.readlines()

Followers = {}

for dat in asiacup2018:
    file2 = dat.split()
    if file2[0] not in Followers:
        Followers[file2[0]] = int(file2[-2])

Followers

top_People_Followed = collections.Counter(Followers).most_common(10)
top_People_Followed

outputFile = open(r'Maximum_follower.txt', 'w', encoding="utf-8")
outputFile.write("The top 10 users who have maximum followers for the entire timeline: \n",)

for i in range(0, 10):
    outputFile.write(str(i + 1) + ". Username: " + top_People_Followed[i][0] + " -> Number of Followers: " + str(top_People_Followed[i][1]) + "\n\n")
    outputFile.close