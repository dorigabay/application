import glob
import re


f = open("dorigabay.json","r").read()

lpeople = glob.glob("/mnt/c/Users/Dor/Documents/classes/python/flask/students/*.json")
dict_people = {"rrr":"ggg"}
for i in lpeople:
    dict_people[str(re.search("(.*)\.json",i).group(1))]=i
people_add = ""
for i in dict_people.keys():
    people_add+="\n<a href="+str(i)+">"+dict_people[i]+"</a>"
string="5ytgg"
print(dict_people,people_add)
print(re.match(r".*(t).*",string))