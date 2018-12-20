#String, 
print("GiraffeAcademy")
print("Giraffe\nAcademy") #new line
print("Giraffe\"Academy") #mask quotation mark

phrase = "Donkey Kong"
print(phrase + " is cool")

print(phrase.lower()) #lower case
print(phrase.upper()) #upper case
print(phrase.upper().isupper()) #if upper case return true

print(len(phrase)) #length of string
print(phrase[0]) #first letter of string
print(phrase[3]) #4. letter of string

#index function
print(phrase.index("K")) #position of capital "K"
print(phrase.index("on"))

#replace
print(phrase.replace("Kong", "SomeText"))
