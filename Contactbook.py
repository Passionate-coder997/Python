print('ContactBook')

r_contact=open("contact_database","r")
w_contact=open("contact_database","a+")
sc=input('Enter the number of contacts you want to add: ')

for j in range(int(sc)):
    if sc==0:
        continue
    name,ph_no=input().split(" ")
    entry=(name+'='+ph_no)
    w_contact.write(entry+"\n")

search=input('Enter the contact to be searched: ')
for line in r_contact.readlines():
    if search in line:
        print(line)