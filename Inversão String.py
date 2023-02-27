string = input("Digite a string que deseja inverter: ")

string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("A string invertida é:", string_invertida)
