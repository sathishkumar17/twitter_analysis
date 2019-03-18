import collections


Read_File = "C:/Users/sathi/PycharmProjects/twitter_Analysis/NBA 2019.txt"

# Storing the read file into a Variable - with encoding format - latin-1
with open(Read_File, encoding="latin-1") as De_encode_File1:
    asiacup2018 = De_encode_File1.readlines()

names = {}
count = 0
for dat in asiacup2018:
    file2 = dat.split()
    names[count] = file2[0]
    count = count + 1  # count value to increament list of dictionary
list_names = names.values()

# list_names
# len(list_names)

# counting the number of occurences of each name
count_names = collections.Counter(list_names)

# displaying the new array
# count_names

# Taking the top 10 ans storing in array
a = collections.Counter(count_names).most_common(10)

# for i in range(0,10):
#    print(a[i][0])

outputFile = open(r'Most_tweeted.txt', 'w', encoding="utf-8")
outputFile.write("The top 10users who have tweeted the for the entire timeline: \n", )
for i in range(0, 10):
    outputFile.write("The user " + a[i][0] + " tweeted " + str(a[i][1]) + " times" + "\n")
    outputFile.close