from time import sleep
import pyautogui
import random

class Screen_bot:

    commentaires = ['Super contenu', 'Tres beau post', 'J\'aime beaucoup ton post']
    pyautogui.FAILSAFE = False

    def like_post(nb_post):

        sleep(5)
        pyautogui.moveTo(x=0, y=0)

        sleep(2)
        pyautogui.moveTo(x=1059, y=475)

        for i in range(nb_post) :

            sleep(2)
            pyautogui.doubleClick()
            sleep(2)
            pyautogui.scroll(-50)
    
    def comment(self, nb_post):

        sleep(5)
        pyautogui.moveTo(x=0, y=0)

        sleep(2)
        pyautogui.moveTo(x=1059, y=475)

        sleep(2)
        pyautogui.click()

        for i in range(nb_post):

            sleep(2)
            pyautogui.moveTo(x=1580, y=1001)
            pyautogui.click()
            sleep(2)
            pyautogui.write(self.commentaires[random.randint(0, len(self.commentaires)-1)], interval=0.25)
            pyautogui.hotkey('enter')
            
            sleep(2)
            pyautogui.moveTo(x=1335, y=571)
            pyautogui.click()

    def search_by_hashtag(self, hashtag, nb_post):

        sleep(5)
        pyautogui.moveTo(x=0, y=0)

        # SEARCH
        pyautogui.moveTo(x=870, y=131)
        pyautogui.click()
        sleep(2)
        pyautogui.write(hashtag, interval=0.25)
        pyautogui.hotkey('enter')

        sleep(5)
        pyautogui.moveTo(x=894, y=421)
        pyautogui.click()

        # LIKE & COMMENT
        for i in range(nb_post):

            sleep(2)
            pyautogui.moveTo(x=673, y=514)
            pyautogui.doubleClick()

            sleep(2)
            pyautogui.moveTo(x=1580, y=1001)
            pyautogui.click()

            sleep(2)
            pyautogui.write(self.commentaires[random.randint(0, len(self.commentaires)-1)], interval=0.25)
            pyautogui.hotkey('enter')

            sleep(2)
            pyautogui.moveTo(x=1335, y=571)
            pyautogui.click()
        

while True :

    print('1 : Like des posts')
    print('2 : Commente des posts')
    print('3 : Like et Commente par une recherche ')
    print('4 : Quitter')

    rep = int(input('Choix : '))

    if rep == 1 :

        nombre = int(input('Entrer le nombre de post a liker : '))
        Screen_bot.like_post(nombre)
    
    elif rep == 2 :

        nombre = int(input('Entrer le nombre de post a commenter : '))
        Screen_bot.comment(Screen_bot, nombre)

    elif rep == 3 :

        hashtag = input('Entrer le tag : ')
        nombre = int(input('Entrer le nombre de post a liker et commenter : '))

        Screen_bot.search_by_hashtag(Screen_bot, hashtag, nombre)
    
    elif rep == 4 :

        break

    else :

        print("Veuillez choisir une option")