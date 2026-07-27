try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos problema com os tipos de dados")
except ZeroDivisionError:
    print("Não pode ser dividido por 0")
except KeyboardInterrupt:
    print("Usuário não informou os dados")
except Exception as erro:
    print(erro.__cause__)
else:
    print(f'o resultado é {r}')
finally:
    print("Volte sempre")