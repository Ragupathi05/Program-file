low='abcdefghijklmnopqrstuvwxyz'
up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str1=input("Enter the string: ")
low_count=0
up_count=0
for i in str1:
    if i in low:
        low_count+=1
    elif i in up:
        up_count+=1
print("Lower Case:",low_count)
print("Upper Case:",up_count)
