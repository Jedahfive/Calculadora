n1= int(input("digite um numero "))
n2= int(input("digite outro numero "))

operacao= input("Qual operacao voce quer? ")
match operacao:
    case "soma":
        soma= n1+n2
        print(soma)
    case "subtracao":
        subtracao= abs(n1-n2)
        print(subtracao)
    case "multiplicacao":
        multiplicacao= n1*n2
        print(multiplicacao)
    case "divisao":
        divisao= n1/n2
        print(divisao)
