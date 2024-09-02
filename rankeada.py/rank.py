# interface inicial
nome = input("Nos informe seu nome:")
gender = input(f"Olá {nome} com qual genero voce se indentifica? M ou F: ")
if gender == 'M':
    print( "Ola",nome, "seja bem vindo")
elif gender == "F":
    print("Ola", nome, "seja bem vinda")
else:
    print("_")

categoriasPossiveis = ['Categoria Ferro', 'Categoria Bronze','Categoria prata','Categoria Ouro','Categoria Diamante','Categoria Lendario','Categoria Imortal' ]
print(f'Heroi cadastrado, vamos te mostrar as categorias Possiveis Abaixo:')
for categoria in categoriasPossiveis:
    print(categoria)

vitorias = int(input("Quantas vitorias voce obteve?: "))
derrotas = int(input("Quanta derrotas voce teve?: "))
subtrair = (vitorias-derrotas)
if subtrair <=10: 
 print(f"Parabens {nome} voce foi promovida a categoria Ferro")
elif subtrair >=11 and subtrair <=20: 
 print(f"Parabens {nome} voce foi promovida a categoria bronze")
elif subtrair >=21 and subtrair <=50 :
 print(f"Parabens {nome} voce foi promovida a categoria Prata")
elif subtrair >=51 and subtrair <=80:
 print(f"Parabens {nome} voce foi promovida a categoria Ouro")
elif subtrair >=81 and subtrair <=90:
 print(f"Parabens {nome} voce foi promovida a Categoria Diamante")
elif subtrair >=91 and subtrair <=100:
 print(f"Parabens {nome} voce foi promovida a Categoria Lendaria")
elif subtrair >= 101:
 print(f"Parabens {nome} voce foi promovida a categoria Imortal")
  



