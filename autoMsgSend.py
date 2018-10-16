import pyautogui as auto
from pynput import keyboard
import time
import random
import emoji

msgList = [
    "Nothing can make me so happy neither the cold shower nor the winter morning as your sparkling smile…so keep smiling always. Good Morning dear!!",
    "Night has gone taking the darkness away from you…now the sun is brightening your day so wake up and accept the opportunities given by the sun. Gud Mng Buddy!!",
    "I don’t want to wake up, don’t want to the work all i want is to texting you all the day my friend. What can be more pleasurable than it. Good Morning .. have a nice day!!",
    "Having morning coffee..watching sunrise in the morning brings me a lot of happiness but there is lack of a little thing; you are not here with me. Good Morning friend!!",
    "We are living in a colourful world. Yellow color of sun, green grass and blue sky fills our life with colors. May your day as colourful as the nature. Good Morning Dear!!",
    "Without sun people can’t imagine life on the planet but i can’t imagine my life without you, my friend. Gud Mng..have a great day!!",
    "I was waiting for the morning..and the time has come now. Good Morning, Wake up my friend. Get ready and come immediately… i’m waiting.",
    "Money is not the real wealth. It can’t buy love and friendship. So i don’t run for money in the morning but i wish you a good morning to buy the precious love from you, my friend.",
    "Everybody feel embarrassed sometimes but i never because i have a very supportive and caring friend. Do you know..who is this?? My friend – YOU. Good Morning!!",
    "It’s morning now..so wake up buddy and go to the new place, new destination and new heights of your life. Good Morning!!",
    "A very good morning to very good friend. May your day fill your life with all the happiness of this world. Good Morning Buddy!!",
    "A perfect day is not the on which starts with coffee or tea but the perfect is that which starts with you. Good Morning dear friend!!",
    "Every new morning is a new beginning of life. Forget the past and live the present. Good Morning friend… have a nice day.",
    "You should regret your past…every new day should be an another opportunity to make that mistake right. Good Morning friend!!",
    "Today’s morning i thought the special person of my life and you strike to my mind. The warm sunrising is beautiful but our friendship is more beautiful. Good morning friend!!",
    "Yesterday can never be like today and tomorrow will not be like today..so live today forgetting everything of past and future. Good Morning!!",
    "Happiness is the gift for those who think positive and good thoughts in morning. Wake up it’s morning…gud mng dear!!",
    "When morning air blows over your face..just feel it someone far away is missing you. Good Morning!!",
    "Open your eyes and feel the morning air…feel the chirping birds and thanks all that beautiful things around you..especially thanks to our friendship. Good Morning!!",
    "A true friend is precious gift from god that worths more than gold. What can be better time to wish friend than early morning?? Good Morning!!",
    "Never let worries put down because i’m always with you all my efforts dear friend. Good Morning!!",
    "A good friend like you is more than a bless. It’s morning wake up and start a new day with a new hope. Good Morning!!",
    "Relationships are based on the expectations and responsibility but friendships are based on smiles and laughter. Good Morning dear!!",
    "I can imagine the end of the world but i can’t imagine the end of our friendship. Good Morning friend!!",
    "Whether there is any problem but if a friend like you is with me then i can overcome any obsttacle coming in my life journey. Good Morning dear friend!!",
    "To the first and the very special friend i’m sending this good morning wish for the beautiful morning and the rest of the day. GOod Morning !!",
    "There is nothing better than to get up in the morning knowing that there is a person who love in a way that you do. Good Morning!!",
    "Me and you may be the morning persons, if morning happened at Noon. Good Morning dear!!",
    "Good thoughts precede good deeds. Good deeds precede success. Good Morning friend!!",
    "Every new morning makes a new day and every new day have a chance to change your life. Good Morning!!",
    "Good Morning dude!! Wake up and share your lovely smile with the world.",
    "Holding a poor hand gives us much more happiness than that of holding a good hand. Good Morning!!",
    "Never get disappointed of how bad your life is going on… always wake up with a good smile and thank to god that you have one. Good Morning!!",
    "Every morning i wake up with happiness because i know i’ll see you. Good Morning!!",
    "A cute smile, lighten day and hope everything will be okay for you today. Good Morning!!",
    "Every morning you have two options to choose..one to continue with your dreams other to get up and work hard to make them real. Good Morning!!",
    "All the mornings are like blank canvas and it is your job to color the beautiful scene in your canvas. Good Morning!!",
    "Great attitude is like a perfect cup of coffee- don’t start your day without it. Good Morning!!",
    "Doesn’t matter how bad the things are..we may at least happy when you wake up in the morning. Good Morning dear!!",
    "Prayer is the key of morning and bolt of the evening. Good Morning!!",
    "When you wake up in the morning first say to yourself what you would be and then do what you have to do to get it. Good Morning!!",
    "Once you replace the bad thoughts with the good ones the results will automatically be positive. Good Morning!!",
    "Life always offers a second chance…it’s called tomorrow. Good Morning!!",
    "Only those who risk going too far can possibly find out how far one can go. Good Morning!!",
    "You live only once but if you live right then one is enough. Good Morning!!",
    "Always remember that troubles will come to your way every next day of your life but you should not afraid friends like me will always stay there for you. Good Morning!!",
    "Dreamers like you don’t need inspirational good morning messages but a big alarm bell and friends like me to wake you up. Good Morning!!",
    "Good morning buddy..have a nice day. If your day really pass nicely then remember to thanks me in evening.",
    "No matter how busy our lives are but you still remembered first by me when i get up in the morning. Good Morning!!",
    "I don’t need coffee in the morning but our friendship is my caffeine which i need always. Good Morning!!",
    "i’m not sure that you will have an awesome day but i can guarantee that you will in a company of loving friends like me.Good Morning!!",
    "Today’s forecast for all those who are reading this message..today will be awesome for you. Good Morning!!",
    "Friendship is what makes life worth living. Good morning.",
    "This is the third time your alarm bell is ringing..wake up buddy and enjoy the sweet morning. Good Morning!!",
    "My mom always teaches me to start the day with a good thought..that’s why i always begin my day thinking about the friends like you. Good Morning!!",
    "Everyday may not be good but there is something good in everyday. Good Morning!!",
    "To forgive is the most beautiful form of love and in return we will get unexpected peace and happiness. Good Morning!!",
    "If you speak when you are angry then you will make the best speech you will ever regret. Good Morning!!",
    "People do not notice what we do for them untill we stop doing it.. Good Morning!!",
    "You may not perfect in many things but many things can’tbe perfect without you. Good Morning friend!!"
    ]

def clickMouseOnGivenPos(x,y):
    print('Mouse')
    auto.click(x, y)


def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()

def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    
'''569 pages'''
'''Do in parts, like from 0 to 12 once then 12 to 36'''
for i in range(0, 1):#749
    sleepTime = random.randrange(0, 1000)/1000
    msgInd = random.randrange(0, 60)
    time.sleep(sleepTime)#wait random time
    auto.typewrite(msgList[msgInd])
    auto.press('enter')
