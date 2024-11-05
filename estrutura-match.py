media = 9

match media:
    case media if media < 5:
        print("Você foi reprovado")
    case media if 5 <= media < 7:
        print("Você fará a recuperação")
    case media if media >= 7:
        print("Você foi aprovado")