a = "Hassnain Raza"#Double quotes string 
b = 'Hasnain Raza'#single quotes string 
c = """I am Hassnain
My age is 17
I live in Chowk Sarwar Shaheed"""#Triple quotes string 
print(a)
print(b)
print(c)
#concatenation
name = "Hassnain"
sur_name = "Raza"
complete_name = name +" " + sur_name
print(complete_name)

#indexing and slicing 
print(complete_name[4])
print(complete_name[0:9])
print(complete_name[0:])
print(complete_name[:9])
print(complete_name[:])
print(complete_name[0::2])

#Methods
print(len(complete_name))
print(complete_name.lower())
print(complete_name.title())
print(complete_name.upper())
print(complete_name.find("Raza"))
print(complete_name.count(a))
print(complete_name.replace("Raza","Rana"))




