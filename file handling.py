file= open("Hassnain.txt","r")
data = file.read()
print("Your information is: ",data)

file =open("numbers.txt","r")   
data = file.read() 
data = data.lower()
if "math" in data :
    print("Math is present in the file")

file = open("report.txt","w")
file.write("My name is Rana. My blood group is B.")
file.close()


file=open("report.txt","a")
file.write("I get 973 marks in matric")
file.close()

file = open("report.txt","r")
data = file.read()
print("Your information is: ",data)


