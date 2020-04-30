# Program to show various ways to read and
# write data in a file.
import os

# Read Files
filekp = open("kp.txt", "r")
contentskp = filekp.read()
filegp = open("gp.txt", "r")
contentsgp = filegp.read()
fileop = open("output.txt", "w")


# Get Keywords
def get_keywords(filedata):
    # print(filedata)
    keyword_list = []
    linelist = filedata.splitlines()
    # print(linelist)
    keyword_start = (linelist.index("*** Keyword  ***")) + 1
    keyword_end = len(linelist)
    x = range(keyword_start, keyword_end)

    for i in x:
        firstchar = (linelist[i])[:1]
        if firstchar.isspace() or firstchar == '\t':
            pass
        else:
            keyword_list.append(linelist[i])

    return keyword_list


# Get Missing Keywords
def get_missing(list1, list2):
    set1 = set(map(str.strip, list1))
    set2 = set(map(str.strip, list2))
    difflist = list(set2 - set1)
    return difflist


# Get Arranged String
def get_arrangedstr(keywordlst, originalcode):
    oplist = []
    originalcode = originalcode.splitlines()
    # print(originalcode)
    # print(originalcode.index("Read Dictionary And Find Data"))
    for keyw in keywordlst:
        keywordindex = (originalcode.index(keyw))
        oplist.append(originalcode[keywordindex])
        keywordindex = keywordindex + 1
        while originalcode[keywordindex][:1] == "\t":
            #print(originalcode[keywordindex])
            oplist.append(originalcode[keywordindex])
            keywordindex = keywordindex + 1
    return oplist


# Create Output file
def cnvrtlsttofile(list1, fileobj):
    finalstr = ''
    for keydata in list1:
        finalstr = finalstr + "\n" + str(keydata)
    fileobj.write(finalstr)


# Get Keywords
keyword_kp = get_keywords(contentskp)
keyword_gp = get_keywords(contentsgp)
#print(keyword_gp)
# Compare Keywords
missing_keywords = get_missing(keyword_kp, keyword_gp)
print(missing_keywords)

# Get Arranged Output
outputlist = get_arrangedstr(keyword_kp, contentsgp)

# Write Output File

cnvrtlsttofile(outputlist, fileop)
