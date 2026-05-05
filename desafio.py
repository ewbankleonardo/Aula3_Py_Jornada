def entrada_nome():
    correto = False

    while correto==False:
        try:
            nome=input("Digite seu nome")
            if nome.isdigit() or len(nome)==0:
                print("Verifique se os dados digitados são corretos")
            else:
                return nome

        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt as e:
            print("Execuçao abortada")

def salario():
    correto = False
    while correto == False:
        try:
            sal=float(input("Digite o Salário "))

            if sal<=0 or isinstance(sal,float)==False:
                print("Valor inválido, verifique se foi digitado corretamente")
            else:
                correto = True
                return sal
            
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt as e:
            print("Execuçao abortada")

def bon():
    correto = False
    while correto ==False:
        try:
            bonus= float(input("Digite o valor do bonus"))

            if bonus <= 0 or isinstance(bonus,float)==False:
                print("Valide a informaçao digitada")
            else: 
                correto = True
                return bonus
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt as e:
            print("Execuçao abortada")

def main():
    try:
        nome = entrada_nome()
        sal = salario()
        bonus = bon()   
        kpi = 1000 + sal * bonus
        print(f"O bonus de {nome}, que tem salario de R${sal} é de R${kpi}")

    except KeyboardInterrupt as e:
        print(e)


main()