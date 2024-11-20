names = ['phil', 'mike', 'tom', 'jerry']
print(names[-1])
print(names[3])
print('tom')
print(names[1].title())
print("Hello, "+names[2].title()+" !")
commuting = ['bike', 'bus', 'car','train']
message = "I'm commuting by " + commuting[2].title()+ '.'
print(message)
guests = []
guests.append('chen')
guests.append('hua')
guests.append('du')
print("Hi, " +guests[-1].title()+" welcome to our party!")
print(guests[0].title() + ' and ' + guests[1].title() + ' and ' + guests[2].title() + ' are invited.')
guests[0] = 'ma'
print("Hi, " +guests[0].title()+':'+"\n welcome to our party!")
guests.insert(0,'li')
guests.insert(2, 'zhang')
print("Hi, we got a bigger table now."+guests[0].title()+" and "+guests[2].title()+ " welcome to our party.")
print(len(guests))
print(guests)
del guests[-2]
poped_guest = guests.pop()
guests.pop()
print(guests)
print(poped_guest.title()+" is not coming.")
guests.remove('li')
guests.pop()
print(guests)
print(poped_guest)