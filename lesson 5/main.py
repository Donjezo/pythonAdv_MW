def sayHello():
    print("hello")


sayHello()

def greet_person(name):
    print("pershendetje, " , name)



greet_person("Geat")
greet_person("Gert")
greet_person("Resa")
greet_person("Adonisi")



def prezantimi(emri,mbiemri):
    print("Pershendetje une jam: ", emri," dhe mbiemri im eshte :",mbiemri)


def prezantimi2(emri,mbiemri):
    print(f"Pershendetje une jam {emri} dhe mbiemri im eshte {mbiemri} ")

prezantimi("donjeta","zogaj")
prezantimi2("Resa","miftari")

print("-------------------------")


def add(numer1,number2):
    return  numer1+number2

print(add(2,2))

def zbritja(x,y):
    rezultati = x-y
    return  rezultati


print(zbritja(9,2))