#exercicio3
preço=24.95
desconto=0.4 
primeiro_envio=3 
demais_envios=0.75

preço_real=preço*desconto
custo_do_primeiro_livro=preço_real+primeiro_envio
custo_dos_demais=(preço_real*demais_envios)*59

custo_total=custo_do_primeiro_livro+custo_dos_demais
print('O custo total para a compra de 60 livros é de ',custo_total,'reais')