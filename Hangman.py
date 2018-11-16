from turtle import *
from random import randint
import time

sw=800
sh=1200

wordlist = ["abrogate", "blandishment", "partison","trenchant",\
            "mendacious","malice","predicament","new england patriots",\
            "aspersion","maudlin", "pusillanimous", "xylophoage",\
            "abnegation", "bag this bagguet"]

tWriter = Turtle()
tWriter.hideturtle()

tBadLetters= Turtle()
tBadLetters.hideturtle()

s = getscreen()
s.setup(sw,sh)
s.bgcolor("#011d49")

t=getturtle()
t.color("#fffbe8")
t.width(5)
t.hideturtle()
t.speed(0)

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
dispalyWord = ""
secretWord = ""
lettersWrong = ""
lettersRight = ""
fails = 6
fontS = int(sh*0.025)
gameDone = False

def displayText(newText):
    tWriter.color("#f4a442")
    tWriter.clear()
    tWriter.penup()
    tWriter.goto( - int(sw*0.4),- int(sh*0.3) )
    tWriter.write(newText, font = ('Arial', fontS,'bold'))

def displayBadLetters(newText):
    tBadLetters.color("#f4a442")
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto( - int(sw*0.4), int(sh*0.25) )
    tBadLetters.write(newText, font = ('Arial', fontS,'bold'))
    
def chooseWord():
    global secretWord
    secretWord = wordlist[randint(0,len(wordlist) - 1)]
    print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, secretWord, lettersRight
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersRight:
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or typr $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 5:
        drawhead()
    if fails == 4:
        drawtorso()
    if fails == 3:
        drawleftleg()
    if fails == 2:
        drawrightleg()
    if fails == 1:
        drawleftarm()
    if fails == 0:
        drawrightarm()
        
def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the word!!"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess == secretWord:
        displayText("YES! " + secretWord + " is the Word!!")
        gameDone = True
    else:
        displayText("No, " + guess + " is not the word.")
        time.sleep(1)
        displayText(displayWord)
        fails -=1
        updateHangmanPerson()

def playgame():
    global fails, lettersRight, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:
        theGuess = getGuess()
        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("No, " + theGuess + " is too many letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("No, " + theGuess + " is not a letter.")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            #correct
            lettersRight += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess.lower() not in lettersWrong:
            displayText("No, " + theGuess + " is not in the word.")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("not in word: {" +lettersWrong + "}")
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()
        else:
            displayText("No, " + theGuess + " is repeated.")
        if fails <= 0:
            displayBadLetters("No more guesses")
            displayText("You lose. The Word is: " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("You got it!")
            gameDone = True

    
def drawGallows():
    t.penup()
    t.setheading(0)
    t.goto(-int(sw/4), -int(sh/4))
    t.pendown()
    t.forward(int(sw*0.5))
    t.backward(int(sw*0.1))
    t.left(90)
    t.forward(int(sh*0.5))
    t.left(90)
    t.forward(int(sw*0.2))
    t.left(90)
    t.forward(int(sh*0.05))

def drawhead():
    hr = int(sw*0.05)
    t.penup()
    t.goto(t.xcor()-hr, t.ycor()-hr)
    t.pendown()
    t.circle(hr)
    t.penup()
    t.goto(t.xcor()+hr, t.ycor()-hr)
def drawtorso():
    t.penup()
    t.pendown()
    t.forward(int(sh*0.18))
def drawleftleg():
    t.penup()
    t.pendown()
    t.left(30)
    t.forward(150)
def drawrightleg():
    t.penup()
    t.pendown()
    t.backward(150)
    t.right(60)
    t.forward(150)
def drawleftarm():
    t.penup()
    t.pendown()
    t.backward(150)
    t.left(30)
    t.backward(180)
    t.left(60)
    t.forward(80)
def drawrightarm():
    t.penup()
    t.pendown()
    t.backward(80)
    t.right(120)
    t.forward(80)
    


    
drawGallows()
drawhead()
drawtorso()
drawleftleg()
drawrightleg()
drawleftarm()
drawrightarm()


time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in Word: {" + lettersWrong + "}")
playgame()




