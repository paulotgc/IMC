import customtkinter as ctk

ctk.set_appearance_mode('dark')

def validar_imc():
    peso = float(campo_peso.get())
    altura = float(campo_altura.get())

    altura_quadrada = altura * altura
    imc = peso / altura_quadrada

    if imc < 18.6:
        #print('IMC: {:.2f}'.format(imc))
        #print('IMC abaixo de 18,5: Abaixo do Peso')
        resultado_imc.configure(text='IMC: {:.2f}, Abaixo de 18.5: Abaixo do peso'.format(imc), text_color='yellow')
    elif imc >= 18.5 and imc < 25:
        #print('IMC: {:.2f}'.format(imc))
        #print('Entre 18,5 e 25: Peso Ideal')
        resultado_imc.configure(text='IMC: {:.2f},  Entre 18,5 e 25: Peso Ideal'.format(imc), text_color='green')
    elif imc >= 25 and imc < 30:
        #print('IMC: {:.2f}'.format(imc))
        #print('25 até 30: Sobrepeso')
        resultado_imc.configure(text='IMC: {:.2f}, 25 até 30: Sobrepeso'.format(imc), text_color='red')
    elif imc >= 30 and imc < 40:
        #print('IMC: {:.2f}'.format(imc))
        #print('30 até 40: Obesidade')
        resultado_imc.configure(text='IMC: {:.2f}, 30 até 40: Obesidade'.format(imc), text_color='red')
    else:
        #print('IMC: {:.2f}'.format(imc))
        #print('Acima de 40: Obesidade Mórbida')
        resultado_imc.configure(text='IMC: {:.2f}, 30 até 40: Obesidade'.format(imc), text_color='red')


janela = ctk.CTk()
janela.title('Calculo IMC')
janela.geometry('300x300')

label_peso = ctk.CTkLabel(janela, text='Peso')
label_peso.pack(pady=5)

campo_peso = ctk.CTkEntry(janela, placeholder_text='Digite seu peso')
campo_peso.pack(pady=5)

label_altura = ctk.CTkLabel(janela, text='Altura')
label_altura.pack(pady=5)

campo_altura = ctk.CTkEntry(janela, placeholder_text='Digite sua altura')
campo_altura.pack(pady=5)

botao_resultado = ctk.CTkButton(janela, text='Resultado', command=validar_imc)
botao_resultado.pack(pady=5)

resultado_imc = ctk.CTkLabel(janela, text='')
resultado_imc.pack(pady=5)

janela.mainloop()
