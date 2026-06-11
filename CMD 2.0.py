import os
import time
import keyboard



os.system('title CMD 2.0')
os.system('color 0F')

while True:


    def cls():
        os.system('cls')

    command = input("> ")

    if command == "help":
        print("")
        print("[cls] Стирает весь текст с экрана.")
        print("[CMD /color] Меняет цвет консоли, подробнее в help /color")
        print("[CDC] Очищает кэш днс")
        print("[kill] Убивает процесс.")
        print("[PS] Диспетчер задач.")
        print("")
        
    elif command == "cls":
        cls()
        
    elif command == "CMD /color":
        print("")
        print("[!] Вы не ввели номер цвета. Подробнее в help /color.")

    elif command == "CMD /color 0":
        os.system('color 0F')
        
    elif command == "CMD /color 1":
        os.system('color 1')

    elif command == "CMD /color 2":
        os.system('color 2')
        
    elif command == "CMD /color 3":
        os.system('color 3')
        
    elif command == "help /color":
        print("")
        print("|| Примечание: В отличии от обычного CMD тут меняется только цвет текста")
        print("")
        print("CMD /color 0 возвращает обычный цвет консоли")
        print("CMD /color 1 делает консоль синей")
        print("CMD /color 2 делает консоль зелёной")
        print("CMD /color 3 делает консоль голубой")
        print("")
        
    elif command == "kill":
        print("")
        app = input("Как называется приложение? ")
        os.system(f"Taskkill /f /im {app}")
        print("")
        
    elif command == "PS":
        print("")
        os.system("tasklist")
        print("")
    
    elif command == "quit":
        print("")
        print("[*] Выходим из терминала, удачи!")
        time.sleep(1)
        break
        
    elif command == "CDC":
        print("")
        os.system("ipconfig /flushdns >nul")
        print("")
        print("[!] кэш очищен.")
        print("")
       
        
    else:
        print("")
        print("[?] Команда не распознана, напишите <<help>> для списка всех команд.")
        print("")
        
        