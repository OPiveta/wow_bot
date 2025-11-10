import pyautogui  
import time
import comunicao_arduino
import keyboard
import threading
import os

regiao_skill = (1700, 900, 400, 300)
regiao_target_olhar = (1600, 900, 350, 350)

rodando_bot_2 = False 

lock_bot_2 = threading.Lock()


def target_monstro():
    return pyautogui.locateCenterOnScreen("img\imag_target2.PNG", confidence=0.8, region=regiao_target_olhar)


def bot_2():
    
    print("         Bot 2 INICIADO.")
    time.sleep(0.3)
    while True:
        if rodando_bot_2:
            try:
                monstro = target_monstro()
                if monstro is not None:

                   # localizar_nether = pyautogui.locateCenterOnScreen("img/arcane_orb.PNG", confidence=0.8, region=regiao_skill)
                    localizar_ice_barrier= pyautogui.locateCenterOnScreen("img/toch_of.png", confidence=0.8, region=regiao_skill)


                    if localizar_ice_barrier:
                        comunicao_arduino.arduino.write(b'f8\n')
                        print("Skill: Touch of the Magi")
                        time.sleep(0.3)
                    
                    # elif localizar_nether :
                    #     comunicao_arduino.arduino.write(b'f7\n')
                    #     print("Skill: Arcane Orb")

                    

                    else:
                        print("Target encontrado, mas nenhuma skill detectada.")

                else:
                    print("Sem target ou monstro morto.")
                    time.sleep(0.2)

            except Exception as e:
                print(f"Erro detectado: {e}")
            
            time.sleep(1)


#Início e parada do Bot 2
def iniciar_bot_2():
    global rodando_bot_2
    with lock_bot_2:
        if not rodando_bot_2:
            rodando_bot_2 = True
            import threading
            threading.Thread(target=bot_2).start()


def kill_now():
    """Para tudo e mata o processo."""
    global rodando_bot_1, rodando_bot_2
    rodando_bot_1 = False
    rodando_bot_2 = False
    print("🛑 PgUp pressionado: encerrando imediatamente o processo.")
    os._exit(0)  # hard kill
    
keyboard.add_hotkey('insert', iniciar_bot_2)
keyboard.add_hotkey('pgup', kill_now)
print("   ")
print("        INSERT = Iniciar Bot 2           ")
print("        PGGUP = Parar Bot 2              ")
print("   ")
print("Pressione 'Insert' para iniciar Bot 2, 'Delete' para parar.")
print("PGUP = Parar tudo e matar o processo")

keyboard.wait()