# Criar as opções que serão mostradas ao usuário: String múltipla precisa ser definidar por 3 aspas duplas ou simples
menu = """  
Selecione a operação a ser realizada:
        
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
# Definição das variáveis
    # convenção: definição de variáveis sempre com letra minúscula em estilo serpente (utiliza "_" como espaço entre as palavras)
                # Constante: Sempre com todas as letras maiúsculas, seguindo o mesmo estilo serpente 
                
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

# Utilizar laço de repetição While para executar o bloco até que a opção não seja mais verdadeira

while True:
    
    opcao = input(menu)
    
    if opcao == "1": # Quando uma váriavel recebe um valor atribui-se o sinal de "=" quando precisa ver se o valor é exatamente igual ao input utiiza "=="

        valor = float(input("Informe o valor do depósito ")) # Input: recebe o valor digitado pelo o usuário; float = adiciona as casa decimais ao número
        
        if valor > 0:   # Condição: Se o valor for maior que zero executa o código para armazenar o valor na variável saldo e extrato
           
            saldo += valor  # Atribuição com adição: acrescenta o valor digitado à variável saldo
            extrato += f"Depósito: R$ {valor:.2f}\n" #acrescenta o valor digitado à variável extrato e o novo valor é informado com duas casa decimais (.2f)
           
            print(f"\n Depósito realizado com suscesso no valor de {valor:.2f}")
            
            print(f"\n Seu saldo atual é: R$ {saldo:.2f} ")
        else:
            print("Operação falhou! O valor informado é inválido")  # Se o valor for 0 ou negativo o código acima não é realizado e a mensagem de erro é mostrada
    
    elif opcao == "2":
   
        print(f"\nO seu saldo é R$: {saldo:.2f} ")
        
        print("\nO limite para saque é de R$ 500,00")

        valor = float(input("\nInforme o valor do saque "))
    
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite
    
        excedeu_saques = numero_saques >=LIMITE_SAQUES
    
    
        if excedeu_saldo:
    
         print ("Operação falhou! Você não tem saldo suficiente!")
        
        elif excedeu_limite:
     
         print ("Operação falhou! Valor informado está acima do limite!")
        
        elif excedeu_saques:
    
            print ("Operação falhou! Você atingiu o número diário de saques!")
    
        elif valor > 0:
        
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
            print(f"Saque realizado com sucesso no valor de: R$ {valor:.2f}")
            
            print(f"\n Seu saldo atual é: R$ {saldo:.2f} ")
        
        else:
         
            print("Operação falhou! O valor informado é inválido")
            
    elif opcao == "3":
        print("\n ........ EXTRATO ..........")
        print("Não foram realizadas movimentações." if not extrato else extrato) # o ifnot é para verificar se o extrato está vazio
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("..............................")
        
    elif opcao == "4":
        break #Pára o programa, é a opção da saída

    else:
     print("operação inválida! Por favor, selecione novamente a operação desejada") #caso a opção digitada não está dentro da especificação do menu