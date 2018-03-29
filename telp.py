dict = {'Jane Doe'      : '+27 555 1024','John Smith'       : '+27 555 6254','Bob Stone'    : '+27 555 5689','Anna Cooper'   : '+27 555 3237'}


print ("phone number Bob Stone : ",dict['Bob Stone'])
print ("-------------------------------------------")
print ("All Key   : ")
for key, val in dict.items():
    print (key)
print ("-------------------------------------------")
print ("All Value    : ")
for key, val in dict.items():
    print (val)
print ("-------------------------------------------")
print ("All Dictionary Keys and Value : ")
for key, val in dict.items():
    print (key,val)
