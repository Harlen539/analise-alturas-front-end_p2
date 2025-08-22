alturas = []
alturas_masculino = []
contador_feminino = 0

for i in range(1,16):
    altura = float(input(f"Digite a altura da pessoa {i+0} (em centimetros): "))
    genero = input("Digite o gênero (M para masculino, F para feminino): ").strip().upper()
    alturas.append(altura)

    if genero == 'M':
        alturas_masculino.append(altura)
    elif genero == 'F':
        contador_feminino += 1

maior_altura = max(alturas)
menor_altura = min(alturas)

if alturas_masculino:
    media_masculino = sum(alturas_masculino) / len(alturas_masculino)
else:
    media_masculino = 0


print("\n-Resultados-")
print(f"Maior altura do grupo: {maior_altura:.2f} cm")
print(f"Menor altura do grupo: {menor_altura:.2f} cm")
print(f"Média de altura dos homens: {media_masculino:.2f} cm")
print(f"Número de mulheres: {contador_feminino}")
