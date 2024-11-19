print("Pense em um número de 1 a 10!")
print("---"*20)
num1 = input("Seu número é maior ou igual 5?")

if num1 == "sim":
    num_do_cinco = input("Seu número é 5?")
    if num_do_cinco == "sim":
        print("Seu número é 5!")
    elif num_do_cinco == "nao" or num_do_cinco == "não":   
        num2 = input("É par?")
        if num2 == "sim":
    
            num3 = input("É 6?")
            if num3 == "sim":
                print("Seu núemro é 6!")
            elif num3 == "nao" or num3 == "não":
                num4 = input("Seu número têm dois dígitos?")
                if num4 == "sim":
                    print("Seu número é 10!")
                elif num4 == "nao" or num4 == "não":
                    print("Seu número é 8!")
        if num2 == "nao" or num2 == "não":
        
            num5 = input("Seu número é 7?")
            if num5 == "sim":
                print("Seu número é 7!")
            elif num5 == "nao" or num5 == "não":
                print("Seu número é 9!")
if num1 == "nao" or num1 == "não":
    num6 = input("Seu número é 1?")

    if num6 == "sim":
        print("Seu número é 1!")
    elif num6 =="nao" or num6 == "não":
        num7 = input("Seu número é par?")
        if num7 == "nao" or num7 == "não":
            print("Seu número é 3!")
        elif num7 == "sim":
            num8 = input("Seu número é o dobro de 2?")
            if num8 == "sim":
                print("HaHa, acerteiseu número é 4!")
            elif num8 == "nao" or num8 == "não":
                print("Seu número é 2!")


         
