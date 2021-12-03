from flask import Flask, request, render_template,redirect
import re
import json
import glob
import random


app = Flask(__name__)

lpeople = glob.glob("/mnt/c/Users/Dor/Documents/classes/python/flask/students/*.json")
dict_people = {}
for i in lpeople:
    json_open = json.loads(open(i,"r").read())
    dict_people[json_open["name"]] = json_open

@app.route("/")
def main():
    return render_template("main.html",title = "Search Engine")

@app.route("/all")
def list_people():
    people_add = "<ul>"
    for names in dict_people.keys():
        people_add += "\n<li><a href=/someone/"+str(names).replace(" ","_")+">"+str(names)+"</a></li>"
    people_add += "</ul>"
    return render_template("main.html",title = "Search Engine",persone=people_add)

@app.route("/someone/<name>")
def persone(name):
    n = dict_people[name.replace("_"," ")]
    sti = "<h2>"+name.replace("_"," ")+"</h2><ul>"
    for details in n.keys():
        sti += "<li>"+str(details)+": "+str(n[details])+"</li>"
    sti+="</ul><a href=http://localhost:5000/>clear</a>"
    return render_template("main.html",title = "Search Engine", persone=sti)

@app.route("/search_people", methods=['GET'])
def search():
    someone = random.choice(list(dict_people.keys()))
    return redirect("http://localhost:5000/someone/"+str(someone).replace(" ","_"))


@app.route("/search_people", methods=['POST'])
def find():
    name_searched = request.form.get("search").lower()
    people_add = "<ul>"
    at_least_one = False
    for names in dict_people.keys():
        if re.search(r".*"+name_searched+".*",names.lower()):
            people_add += "\n<li><a href=/someone/"+str(names).replace(" ","_")+">"+str(names)+"</a></li>"
            at_least_one = True
    people_add += "</ul>"
    if at_least_one:
        return render_template("main.html",title = "Search Engine", persone=people_add)
    else:
        not_found = "<h4>"+"The Name \""+name_searched+"\" Was Not Found"+"<h4>"
        return render_template("main.html", title=str(name_searched), persone=not_found)


app.run(host='localhost', debug=True)