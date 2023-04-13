# Dictionary : Key-Value pairs, Unordered, Mutable

#mydict = {"name":"Max","age":28,"city":"New York"}
#print(mydict)

#mydict2 = dict(name="Mary",age=27, city="Boston")
#print(mydict2)

#mydict["email"] = "something@xyz.com"

#value = mydict["name"]
#print(value)

#del mydict["name"]
#print(mydict)

#if "name" in mydict:
#    print(mydict["name"])

#try:
#    print(mydict["name"])
#except:
#    print("error")

#for key, value in mydict.items():
#    print(key, value)

mydict = {"name":"Max","age":28,"email":"max@xyz.com"}
mydict2 = dict(name="Mary",age=27,city="Boston")

mydict.update(mydict2)
print(mydict)
