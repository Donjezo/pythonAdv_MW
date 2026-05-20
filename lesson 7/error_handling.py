try:
    rezultati = 10/0
except ZeroDivisionError:
    print("Opps nuk mundesh me pjestu me 0 ")
else:
    print("pjestimi eshte realizuar me suskes")
finally:
    print("ke mrri deri te line 8")


frutat = {
    "mollat":5,
    "banane":7,
    "portokalla":3
}

try:
    print(frutat["dredhezat"])
except KeyError:
    print("the key does not ezist in the directory")

text="this is not a number"

try:
    text_to_int= int(text)
except Exception as e:
    print("ka ndodh nje error", e)
finally:
    print("hej ke mrri deri te line 26")