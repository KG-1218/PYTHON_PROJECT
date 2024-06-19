import keyword
print(keyword.kwlist) #printing all keywords 

print("hello")  #using print 
#sample_file =open('C:\Users\HP\Documents\fuels_book.pdf','w')
#print(7,8,9,10, sep='%' , end='$$', file=sample_file)


#value replaced {} in format
print("hello all {} people ".format(10))   #hello all 10 people
print("hello all {} people ".format("amazing")) #hello all amazing people

#replacing {} with any input value
value=input("enter number of people present") # 5
print("hello all {} people ".format(value)) #hello all 5 people






