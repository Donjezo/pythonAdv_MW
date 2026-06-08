
with open("example.txt","r")as file:
    ##content = file.read()
    file1= file.readline() ## kjo e lexon vetm nje line te kodit

print(file1)

## me lexu shume rreshta njekosisht
with open("example.txt","r")as file:
    lines= file.readlines()
    print(lines)