peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal, Parabéns!')
elif imc > 25 and imc <= 30:
    print('Você está no sobrepeso, tente diminuir o açúcar')
elif imc > 30 and imc <= 40:
    print('Você está no estado de obesidade procure um nutricionista!')
else:
    print('Você está com obesidade morbida, procure um médico urgente!')