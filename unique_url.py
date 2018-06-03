file_path = 'outputfile-BDM_Boston.txt'

with open(file_path) as f:
    profile_link = f.readlines()

unique_link = []

for i in profile_link:
    if i not in unique_link:
        unique_link.append(i)

text_file = open("outputfile-BDM_Boston.txt", "w")

for i in unique_link:
    text_file.write(i)

text_file.close()


print len(unique_link)
print len(profile_link)

