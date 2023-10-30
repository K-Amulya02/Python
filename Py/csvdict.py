import csv

# software = [["name","verion","status","users"],["Visual Studio","17.0","Production","99000"],["Atom","4.0.7","Beta","8890"],["Eclipse","2.0","Alpha","990"]]
# with open("software.csv","w") as software_csv:
#     writer = csv.writer(software_csv)
#     writer.writerows(software)

#reading files using "DictReader"
with open("software.csv") as sft:
    reader = csv.DictReader(sft)
    for row in reader:
        print(("{} has {} users").format(row["name"],row["users"]))

#Writing a csv file using Dictionaries. 

cast =[{"MaleLead":"Sheldon", "FemaleLead":"Amy", "Show":"Big Bang Theory"},
       {"MaleLead":"Chandler", "FemaleLead":"Monica", "Show":"Friends"},
       {"MaleLead":"Derek", "FemaleLead":"Meredith", "Show":"Grey's Anatomy"}]

keys = ["MaleLead","FemaleLead","Show"]
with open("cast.csv","w") as cast_csv:
    write = csv.DictWriter(cast_csv, fieldnames=keys)
    write.writeheader()
    write.writerows(cast)

with open("cast.csv") as csv_cast:
   reader = csv.DictReader(csv_cast)
   for row in reader:
      print(("{} and {} star in {}").format(row["MaleLead"],row["FemaleLead"],row["Show"]))