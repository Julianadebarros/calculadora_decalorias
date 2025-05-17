#Variáveis
quantidade_alimentos = int(input("Informe quantos alimentos foram consumidos hoje: "))
total_calorias = 0

for alimento in range(1, quantidade_alimentos + 1, 1):
    calorias = int(input("Informe a quantidade de calorias do {} alimento: ".format(alimento)))
    total_calorias = total_calorias + calorias

print("Total Calorias= {}".format(total_calorias))
