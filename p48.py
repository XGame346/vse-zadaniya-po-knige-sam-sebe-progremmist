class Animal:
    def __init__(self):
        self.name="Дружок"
friend=Animal()
same_friend=friend
print(friend is same_friend)

another_friend=Animal()
print(friend is another_friend)


#Ответ автора
def compare(obj1, obj2):
    class Animal:
    def __init__(self):
        self.name="Дружок"
friend=Animal()
same_friend=friend
print(friend is same_friend)

another_friend=Animal()
print(friend is another_friend)


#Ответ автора
def compare(obj1, obj2):
    return obj1 is obj2

print(compare("а", "б"))
