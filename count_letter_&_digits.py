let='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dig='0123456789'
str1=input("Enter the string: ")
let_count=0
dig_count=0
for i in str1:
    if i in let:
        let_count+=1
    elif i in dig:
        dig_count+=1

print("Letters:",let_count)
print("Digits:",dig_count)
