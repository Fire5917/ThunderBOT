import os, time, random
ai_name = 'ThunderBot'
try:
    import wikipedia
except:
    os.system('pip install wikipedia')
    import wikipedia
try:
    from googlesearch import search
except:
    os.system('pip install googlesearch-python')
    from googlesearch import search
try:
    import colorama
except:
    os.system('pip install colorama')
    import colorama
try:
    from pystyle import Colorate, Colors, Center, Write
except:
    os.system('pip install pystyle')
    from pystyle import Colorate, Colors, Center, Write
try:
    import pyautogui
except:
    os.system('pip install pyautogui')
    import pyautogui
try:
    import requests
    from requests import Session
except:
    os.system('pip install requests')
    import requests
    from requests import Session
try:
    import json
except:
    os.system('pip install json')
    import json
level_mysterious = 0
number_of_step = 4
password_Fire5917 = "A very simple password"
password_Frigogel = "BeStAI-3112"
password_Marcus260 = "langue de chat"
password_Enitxis = "goliaume"
password_1G12 = "1G12"
pyautogui.press('f11')
colorama.init()
try_connect = Write.Input("Please enter the password >>> ", Colors.red_to_yellow, interval=0.025)
if password_Fire5917 == try_connect:
    pseudo = 'Fire5917'
elif password_Frigogel == try_connect:
    pseudo = 'Frigogel'
elif password_Marcus260 == try_connect:
    pseudo = 'Marcus260'
elif password_Enitxis == try_connect:
    pseudo = 'Enitxis'
elif password_1G12 == try_connect:
    pseudo = '[1G12] User'
else:
    exit()
os.system(f'title [{pseudo}] - AI by Fire5917')
def question():
    print(colorama.Fore.WHITE)
    global questionrep
    questionrep = Write.Input(f"{pseudo} >>> ", Colors.red_to_yellow, interval=0.025).lower().replace("'s", " is")
    print(colorama.Fore.GREEN)
Write.Print(f"{ai_name} >>> Nice to meet you, {pseudo}!", Colors.blue_to_red, interval=0.05)
nbr_questions = 0
nbr_answer = 0
percentage_sucess = "Unknow"
while True:
    if nbr_questions > 0:
        percentage_sucess = (nbr_answer / nbr_questions)*100
        percentage_sucess = int(percentage_sucess)
    os.system(f'title [{pseudo}] - AI by Fire5917 - Number of questions : {nbr_questions} - Number of answer : {nbr_answer} - Percentage of success : {percentage_sucess}%')
    question()
    if questionrep[:5] == "hello" or questionrep[:2] == "hi" or questionrep == "yo":
        Write.Print(f"{ai_name} >>> Hi ! How are you?", Colors.blue_to_red, interval=0.025)
        question()
        if questionrep[:4] == 'fine':
            Write.Print(f"{ai_name} >>> Nice, I'm fine too !", Colors.blue_to_red, interval=0.025)
        elif questionrep[:4] == "soso":
            Write.Print(f"{ai_name} >>> Ah... Good luck!", Colors.blue_to_red, interval=0.025)
        elif questionrep[:3] == "bad":
           Write.Print(f"{ai_name} >>> Ah... Good luck and sleep well!", Colors.blue_to_red, interval=0.025)
        else:
           Write.Print(f"{ai_name} >>> Please answer this question with either fine or soso or bad...", Colors.blue_to_red, interval=0.025)
    elif questionrep[:6] == 'google':
        questionrep_clear = questionrep[7:]
        try:
            for url in search(questionrep_clear, stop=1):
                try:
                    os.system(f'start {url}')
                    Write.Print(f"{ai_name} >>> Here is an answer available on the web : {url}", Colors.blue_to_red, interval=0.025)
                except:
                    Write.Print(f"{ai_name} >>> Here is an answer available on the web : {url}", Colors.blue_to_red, interval=0.025)
        except:
            Write.Print(f"{ai_name}>>> No answer available for your question...", Colors.blue_to_red, interval=0.025)
    elif questionrep[:9] == 'wikipedia':
        questionrep_clear = questionrep[11:]
        try:
            Write.Print(f"{ai_name} >>> {wikipedia.summary(questionrep_clear)}", Colors.rainbow, interval=0.005)
        except:
            Write.Print(f"{ai_name} >>> No answer available for your question... Try using wikipedia (search)", Colors.blue_to_red, interval=0.025)
    elif questionrep[:4] == 'fuck' or questionrep[:12] == "you are dumb" or questionrep[:14] == "you are stupid":
        Write.Print(f'{ai_name} >>> Fuck you {pseudo} !', Colors.blue_to_red, interval=0.025)
    elif questionrep[:17] == "what is your name":
        Write.Print(f'{ai_name} >>> My name is {ai_name}, I am an AI developed by Fire5917', Colors.blue_to_red, interval=0.025)
        Write.Print(f'\n{ai_name} >>> Do you want to change my name? ', Colors.blue_to_red, interval=0.025)
        question()
        if questionrep == 'yes':
            Write.Print(f"{ai_name} >>> What's my new name ?\n", Colors.blue_to_red, interval=0.025)
            questionrep = Write.Input(f"{pseudo} >>> ", Colors.red_to_yellow, interval=0.025)
            ai_name = questionrep
            Write.Print(f"{ai_name} >>> My new name is set to {ai_name}", Colors.blue_to_red, interval=0.025)
        if questionrep == 'no':
            Write.Print(f"{ai_name} >>> Ok", Colors.blue_to_red, interval=0.025)
    elif questionrep[:5] == "video":
        questionrep_clear = f"youtube video {questionrep[7:]}"
        try:
            for url in search(questionrep_clear, stop=1):
                try:
                    os.system(f'start {url}')
                    Write.Print(f"{ai_name} >>> Here is a video available on the web : {url}", Colors.blue_to_red, interval=0.025)
                except:
                    Write.Print(f"{ai_name} >>> Here is a video available on the web : {url}", Colors.blue_to_red, interval=0.025)
        except:
            Write.Print(f"{ai_name}>>> No video available for your question...", Colors.blue_to_red, interval=0.025)
    elif questionrep[:15] == "what time is it" or questionrep == "gettime" or questionrep[:4] == 'time':
        time = time.ctime()
        Write.Print(f'{ai_name} >>> {time}', Colors.blue_to_red, interval=0.025)
    elif questionrep[:9] == 'translate':
        Write.Print(f'{ai_name} >>> What do you want to translate?', Colors.blue_to_red, interval=0.025)
        question()
        to_translate = questionrep.replace(" ", "%20").replace("@", "%40").replace("/", "%5C%2")
        Write.Print(f'{ai_name} >>> From which language is it? (possible options : en(english); fr(french) ; es(spanish); zh(chinese); el(greek); de(german); ja(japanese) )', Colors.blue_to_red, interval=0.025)
        question()
        language_from = questionrep
        Write.Print(f'{ai_name} >>> Which language do you want to translate into? (possible options : en(english); fr(french) ; es(spanish); zh(chinese); el(greek); de(german); ja(japanese) )', Colors.blue_to_red, interval=0.025)
        question()
        os.system(f'start https://www.deepl.com/{language_from}/translator#{language_from}/{questionrep}/{to_translate}')
        Write.Print(f'{ai_name} >>> Here is the link to your translation : https://www.deepl.com/{language_from}/translator#{language_from}/{questionrep}/{to_translate}', Colors.blue_to_red, interval=0.025)
    elif questionrep[:3] == 'say':
        have_to_say = questionrep[4:]
        Write.Print(f'{ai_name} >>> {have_to_say} ', Colors.blue_to_red, interval=0.025)
    elif questionrep[:12] == 'randomnumber':
        Write.Print(f'{ai_name} >>> What is the min number of the generation?', Colors.blue_to_red, interval=0.025)
        question()
        first_number = int(questionrep)
        Write.Print(f'{ai_name} >>> What is the max number of the generation?', Colors.blue_to_red, interval=0.025)
        question()
        second_number = int(questionrep)
        random_number = random.randint(first_number, second_number)
        Write.Print(f'{ai_name} >>> The random number between {first_number} and {second_number} is {random_number}', Colors.blue_to_red, interval=0.025)
    elif questionrep[:13] == 'secure search':
        search = questionrep[14:].replace(" ", "+")
        secure_search = f"https://search.brave.com/search?q={search}"
        try:
            os.system(f'start https://search.brave.com/search?q={search}')
            Write.Print(f'{ai_name} >>> The link for your secure search is : {secure_search}', Colors.blue_to_red, interval=0.025)
        except:
            Write.Print(f'{ai_name} >>> The link for your secure search is : {secure_search}', Colors.blue_to_red, interval=0.025)
    elif questionrep[:13] == 'make password':
        minuscules = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nombres = "012345678901234567890123456789"
        symboles = "@#$%&*/\?!€@#$%&*/\?!€@#$%&*/\?!€"
        Write.Print(f'{ai_name} >>> Which type of password do you want to create?', Colors.blue_to_red, interval=0.025)
        print("""
[1] >>> numbers                                                              *        >>> Max caracters = 30
[2] >>> numbers + minuscule letters                                          **       >>> Max caracters = 108
[3] >>> numbers + capital letters                                            ***      >>> Max caracters = 108
[4] >>> numbers + minuscule letters + capital letters                        ****     >>> Max caracters = 186
[5] >>> numbers + capital letters + minuscule letters + symbols              *****    >>> Max caracters = 219
             
        """)
        Write.Print(f'{ai_name} >>> Please enter the number of the type of password that you want to choose', Colors.blue_to_red, interval=0.025)
        question()
        if questionrep == '1':
            use = nombres
        if questionrep == '3':
            use = nombres + majuscules
        if questionrep == '2':
            use = nombres + minuscules
        if questionrep == '4':
            use = nombres + majuscules + minuscules  
        if questionrep == '5':
            use = nombres + majuscules + minuscules + symboles
        Write.Print(f'{ai_name} >>> How many caracters for your password?', Colors.blue_to_red, interval=0.025)
        question()
        longueur_mdp = int(questionrep)
        password = "".join(random.sample(use, longueur_mdp))
        Write.Print(f"{ai_name} >>> Here is your password >>> {password}", Colors.blue_to_red, interval=0.025)
    elif questionrep[:11] == "make a joke" or questionrep[:4] == "joke":
        try:
            url = "https://blague.xyz/api/vdm/random"
            session = Session()
            response = session.get(url)
            data = json.loads(response.text)
            joke1 = data['vdm']
            Write.Print(f"{ai_name} >>> {joke1['content']}", Colors.blue_to_red, interval=0.025)
            Write.Print(f"\n{ai_name} >>> For translation please say translate and copy the answer on the translate area", Colors.blue_to_red, interval=0.025)
        except:
            Write.Print(f"\n{ai_name} >>> [ ! ] No internet connexion", Colors.red, interval=0.025)
    elif questionrep[:15] == "mysterious play" and level_mysterious == 0:
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Welcome in the game, there is {number_of_step} steps in this game for the moment.\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> First , all my congratulations for passing the step 0 !\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> You are now at the step number 1 and you have to think about apple and minecraft\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> To go to the step number 2 you have to say << mysterious play (word) >> \n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Good luck !", Colors.blue_to_red, interval=0.025)
        level_mysterious = 1
    elif questionrep[:28] == "mysterious play golden apple" and level_mysterious == 1:
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Welcome in the game, there is {number_of_step} steps in this game for the moment.\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> First , all my congratulations for passing the step 1 !\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> You are now at the step number 2 and you have to think about hacker and legend\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> To go to the step number 3 you have to say << mysterious play (word) >> \n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Good luck !", Colors.blue_to_red, interval=0.025)
        level_mysterious = 2
    elif questionrep[:25] == "mysterious play anonymous" and level_mysterious == 2:
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Welcome in the game, there is {number_of_step} steps in this game for the moment.\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> First , all my congratulations for passing the step 2 !\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> You are now at the step number 3 and you have to think about square and 5\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> To go to the step number 4 you have to say << m play (number1) (number2) >> \n", Colors.blue_to_red, interval=0.025)
        level_mysterious = 3
    elif questionrep[:11] == "m play 5 25" and level_mysterious == 3:
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> Welcome in the game, there is {number_of_step} steps in this game for the moment.\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> First , all my congratulations for passing the step 3 !\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> You are now at the step number 4 and you have to think about square and 5\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"[UNKNOW_-_-_PERSON] >>> To go to the step number 5 you have to say << SOON >> \n", Colors.blue_to_red, interval=0.025)
        level_mysterious = 4
    elif questionrep[:9] == "thank you" or questionrep[:6] == "thanks":
        Write.Print(f"{ai_name} >>> You are welcome\n", Colors.blue_to_red, interval=0.025)
    elif questionrep[:5] == "leave" or questionrep[:4] == "quit":
        x = 5
        print("LOADING...")
        for i in range(10):
            time.sleep(0.5)
            x  = x - 0.5
            os.system('cls 1')
            print(f"{ai_name} >>> {x} seconds left")
        exit()
    elif questionrep[:10] == "hack prank":
        Write.Print(f"{ai_name} >>> Are you sure to do that?\n", Colors.blue_to_red, interval=0.025)
        question()
        if questionrep[:3] == "yes":
            Write.Print(f"{ai_name} >>> How many times?\n", Colors.blue_to_red, interval=0.025)
            question()
            how_many_time = int(questionrep)
            os.system('color 2')
            os.system('dir/s')
            for i in range(how_many_time):
                os.system('start')
        else:
            Write.Print(f"{ai_name} >>> That is better for you\n", Colors.blue_to_red, interval=0.025)
    elif questionrep == "help":
        Write.Print(f"{ai_name} >>> Here is the help menu\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> help : display the help menu\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> translate : allow to do a translation\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> what time is it / gettime : get the time\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> what's your name : know the name of this AI and allow you to change it\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> joke / make joke : do a joke\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> yo / hello / hi : say hi to you\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> thanks / thank you : say you are welcome\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> say (what you want to say) : the bot say what you want to say\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> video (search) : search a video on the subject you want\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> wikipedia (search) : do a seacrh on wikipedia\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> google (search) : do a search on google for you\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> randomnumber : say to you a random number\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> make password : create a secure password for you\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> secure search (search) : do a secure search for you\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> leave / quit : leave the window\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> hack prank : open a lot of cmd windows\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> what's my name : allow you to see and change your name\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> help1 : a chalenge for you\n", Colors.blue_to_red, interval=0.025)
    elif questionrep[:5] == "help1":
        Write.Print(f"{ai_name} >>> Mysterious play...", Colors.blue_to_red, interval=0.025)
    elif questionrep[:15] == "what is my name":
        Write.Print(f"{ai_name} >>> Your name is {pseudo}\n", Colors.blue_to_red, interval=0.025)
        Write.Print(f"{ai_name} >>> Do you want to change your name?", Colors.blue_to_red, interval=0.025)
        question()
        if questionrep == "yes":
            pseudo = Write.Input(f"{ai_name} >>> What is your new name >>> ", Colors.blue_to_red, interval=0.025)
            Write.Print(f"\n{ai_name} >>> Your name is now set to {pseudo}", Colors.blue_to_red, interval=0.025)
        else:
            Write.Print(f"{ai_name} >>> OK", Colors.blue_to_red, interval=0.025)
    else:
        nbr_answer = nbr_answer - 1
        Write.Print(f"{ai_name} >>> I don't have any results directly in my program, do you want me to search the web for you? ", Colors.blue_to_red, interval=0.025)
        old_questionrep = questionrep
        question()
        if questionrep == 'yes':
            try:
                Write.Print(f"{ai_name} >>> {wikipedia.summary(old_questionrep)}", Colors.rainbow, interval=0.005)
            except:
                try:
                    for url in search(old_questionrep, stop=1):
                        if url == '':
                            Write.Print(f"{ai_name} >>> No answer available for your question... Try using google (search)", Colors.blue_to_red, interval=0.025)
                        try:
                            os.system(f'start {url}')
                            Write.Print(f"{ai_name} >>> Here is an answer available on the web : {url}", Colors.blue_to_red, interval=0.025)
                        except:
                            Write.Print(f"{ai_name} >>> Here is an answer available on the web : {url}", Colors.blue_to_red, interval=0.025)
                except:
                    Write.Print(f"{ai_name} >>> No answer available for your question... Try using google (search)", Colors.blue_to_red, interval=0.025)
        else:
            Write.Print(f"{ai_name} >>> Ok, no problem", Colors.blue_to_red, interval=0.025)
    nbr_answer += 1
    nbr_questions += 1
                        
