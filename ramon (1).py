bestSeller = str(input("O livro é best seller? Responda com sim ou não:"))
lancadoHa2Anos = str(input(" O livro foi lançado há mais de 2 anos? Responda com sim ou não:"))
quantlivros = int(input("Quantos livros quer comprar?:"))
precoLivro = float(input("Qual o preço de cada livro?:"))
desconto = 0

if lancadoHa2Anos == "sim" or bestSeller == "sim":
    desconto += 20
    if quantlivros > 3 :
        desconto += 5
        precofinal = precoLivro * (1 - desconto/100) * quantlivros
        print(f"0 preco final  desconto é de R$: {precofinal: .2f}. ")
    else:
        print("Sem desconto")

