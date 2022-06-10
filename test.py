# def number(num):
    
#     num=0
#     if number % 2==0 and number <10:
#         print("Number is even and less than 10")
        
#     elif number % 2==0 and number>10:
#          print("Number is even and greater than 10")
#     else:
#         print("Your number is odd")
#     print(number(num))        

# this_dict={"ochwada":24,"Siara":23,"Dallas":30}
# print(this_dict)






dog={"name":"morty","color":"black","breed":"Chiwawa","legs":4,"age":"4years"}
print(dog)

student ={"first_name":"Siara","last_name":"Anota","gender":"female","age":21,"marital_status":"married","skills":["python","kotlin","Js"],"country":"Kenya","city":"Nairobi","address":"Riruta"}
print(len(student))#get length
print(student["skills"]) #get values in skills
# print(student.values("skills"))


student=list(student.keys())
print(student) #dictionary to list


# student["skills"] = "singing"
# print(student)#to add to a value



print(list(student))
#dictionary to values


#convert into a tuple
student ={"first_name":"Siara","last_name":"Anota","gender":"female","age":21,"marital_status":"married","skills":["python","kotlin","Js"],"country":"Kenya","city":"Nairobi","address":"Riruta"}
student.pop("first_name")
print(student) #remove one of the values


student ={"first_name":"Siara","last_name":"Anota","gender":"female","age":21,"marital_status":"married","skills":["python","kotlin","Js"],"country":"Kenya","city":"Nairobi","address":"Riruta"}
student["fruit"] = "kiwi"
print(student)

#how to change a dict to a list
student ={"first_name":"Siara","last_name":"Anota","gender":"female","age":21,"marital_status":"married","skills":["python","kotlin","Js"],"country":"Kenya","city":"Nairobi","address":"Riruta"}
print(student.items())


