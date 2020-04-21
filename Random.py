from random import randrange
import os
import time

os.system('clear') or None
os.system('cls') or None

def banner():
    print('''
    ____  ___    _   ______  ____  __  ___
   / __ \/   |  / | / / __ \/ __ \/  |/  /
  / /_/ / /| | /  |/ / / / / / / / /|_/ / 
 / _, _/ ___ |/ /|  / /_/ / /_/ / /  / /  
/_/ |_/_/  |_/_/ |_/_____/\____/_/  /_/   
                                          
''')
    print("Desenvolvedor: Lucas Fernando  GitHub: https://github.com/574RXD")

def jogo():
    print("Loading [   ]")
    time.sleep(0.3)
    print("Loading [-  ]")
    time.sleep(0.3)
    print("Loading [-- ]")
    time.sleep(0.3)
    print("Loading [---]")
    time.sleep(0.3)
    
    clear_time()
    
    print("\033[31m" + "JOGO INICIADO!"+"\033[0;0m")
    print('')
    print("\033[32m" + "~ VOCÊ TEM 5 CHUTES ;) ~"+"\033[0;0m")
    gerando = randrange(0, 25)
    chances = 0
    
    while chances < 5:
        print('')
        chute = int(input("Chute um valor: "))
        
        if chute > gerando:
            print(">>>CHUTE MUITO ALTO<<<")
            print("--------------------")
            chances = chances + 1
        elif chute < gerando:
            print(">>>CHUTE MUITO BAIXO<<<")
            print("--------------------")
            chances = chances + 1
        elif chute == gerando:
            print("\033[32m" + "PARABÉNS VOCÊ ACERTOU :)"+"\033[0;0m")
            time.sleep(1.0)
            clear_time()
            banner()
            main()
        else:
            print("ERRO!")


def jogo_2():
    N1 = int(input(">>>QUANTO MAIOR, MAIS DIFICIL DE ACERTAR<<<\nDigite um número: "))
    gerando_2 = randrange(0, N1)
    
    clear_time()
    
    print("\033[31m" + "JOGO INICIADO!"+"\033[0;0m")
    
    while True:
        chute = int(input("Chute um valor: "))
        
        if chute > gerando_2:
            print(">>>CHUTE MUITO ALTO<<<")
        elif chute < gerando_2:
            print(">>>CHUTE MUITO BAIXO<<<")
        elif chute == gerando_2:
            print("\033[32m" + "PARABÉNS VOCÊ ACERTOU :)"+"\033[0;0m")
            time.sleep(1.0)
            break
        else:
            print("ERRO!")

def clear_time():
    os.system('clear') or None
    os.system('cls') or None
    time.sleep(0.5)

def main():
    try:
        print('')
        print("1-START GAME\n2-DIFICULDADE\n0-SAIR")
        print('')
        menu = input("/Escolha: ")


        if menu == '1':
            try:
                jogo()
                clear_time()
                print("\033[31m" + "GAME OVER :("+"\033[0;0m")
                time.sleep(1.0)
                clear_time()
                banner()
                main()
            except ValueError:
                print("\033[31m" + ">>>APENAS NÙMEROS ESPERTINHO :)" + "\033[0;0m")
                main()
            except KeyboardInterrupt:
                exit()
            except Exception as error:
                print(">>>ALGUM ERRO OCORREU")
                print(error)
        elif menu == '2':
            try:
                jogo_2()
                clear_time()
                banner()
                main()
            except ValueError:
                print("\033[31m" + ">>>APENAS NÙMEROS ESPERTINHO :)" + "\033[0;0m")
                main()
            except KeyboardInterrupt:
                exit()
            except Exception as error:
                print(">>>ALGUM ERRO OCORREU")
                print(error)
        elif menu == '0':
            try:
                print("\033[31m" + ">>>JOGO SENDO FECHADO" + "\033[0;0m")
                time.sleep(0.5)
                exit()
            except KeyboardInterrupt:
                exit()
        else:
            print("OPÇÃO INVÁLIDA!")
            main()
    except KeyboardInterrupt:
        exit()

banner()
main()
    



