from cmu_graphics import * 
import random
app.stepsPerSecond=15
startLabel=Label('Use the arrow keys or WASD to move the snake and eat the apples', 200, 40)

gameheight=400
gamewidth=400
spacesize=20
scoreLabel=[Label("Score", 360,360), Label(0, 360, 380)]
bodyparts=3
snakecolor='darkGreen'
foodcolor='red'
direction=''
counter=0

eatapplesound=Sound("https://freesound.org/data/previews/584/584290_3403708-lq.mp3")


### creates the first 3 body parts when the game starts and creates the new body parts when an apple is eaten###

def snake():
    
    
    snake.body= bodyparts
    snake.coordinates=[]
    snake.squares=[]
    #snake.cooardinates is the 
    for i in range(0, bodyparts):
        snake.coordinates.append([0,200])
    
            
    for (x,y) in snake.coordinates:
        square=Rect(x,y, spacesize, spacesize, fill=snakecolor)
        snake.squares.append(square)
    
### creates the food that the snake has to eat.###
def Food():
    #global variable food is the food that the snake has to eat 
    global food
    
    x=random.randint(0,(gamewidth/spacesize)-1)*spacesize
    y=random.randint(0,(gameheight/spacesize)-1)*spacesize
    food= Rect(x,y,spacesize, spacesize, fill=foodcolor)
    food.toBack()
    food.coordinates=[x,y]

# determines if the food spawned behind the snake.
def foodCheck():
    for i in snake.squares:
        x=i.centerX-spacesize/2
        y=i.centerY-spacesize/2
        if food.coordinates[0]==x and food.coordinates[1]==y:
            newx=random.randint(0,(gamewidth/spacesize)-1)*spacesize
            newy=random.randint(0,(gamewidth/spacesize)-1)*spacesize
            food.centerX=newx+spacesize/2
            food.centerY=newy+spacesize/2
            food.coordinates[0]=newx
            food.coordinates[1]=newy
            
            
        
# determines how the snake moves up, down,left, right ###

def next_turn(snake, food):
    global counter
    x,y = snake.coordinates[0]
    if direction=='up':
        y-=spacesize
    if direction=='down':
        y+=spacesize
    if direction =='left':
        x-=spacesize
    if direction =='right':
        x+=spacesize
    
    snake.coordinates.insert(0,(x,y))
   
    
    square = Rect(x,y, spacesize, spacesize, fill=snakecolor)
    square.toBack()
    snake.squares.insert(0,square)
    snake.squares[0].fill='olive'
    snake.squares[1].fill=snakecolor
    if x==food.coordinates[0] and y==food.coordinates[1]:
        counter+=1
    
        food.visible=False
        eatapplesound.play()
        Food()
        
    else:
        del snake.coordinates[-1]
        snake.squares[-1].visible=False
        del snake.squares[-1]
    scoreLabel[1].value=counter
#makes sure that the snake cant go backwards on itself
def onKeyPress(key):
    if key:
        startLabel.visible=False
    
    if key == 'up' or key== 'w':
        changedirection('up')
        
    if key == 'down' or key == 's' :
        changedirection('down')   
    
    if key == 'left' or key == 'a':
        changedirection('left')
    
    if key == 'right' or key=='d':
        changedirection('right')

#the global direction is 

def changedirection(newdirection):
    global direction
    
    if newdirection== 'up':
        if direction!='down':
            direction= newdirection
            
    if newdirection== 'down':
        if direction!='up':
            direction= newdirection
            
    if newdirection== 'left':
        if direction!='right':
            direction= newdirection
            
    if newdirection== 'right':
        if direction!='left':
            direction= newdirection
            
#checks if the snake hits walls or hits itself
def checkcollsions(snake):
    x,y = snake.coordinates[0]
    if (x < 0) or (x>400) : 
        
        game_over()
    if (y < 0) or (y>400):
        
        game_over()
    if scoreLabel[1].value>=1:    
        for bodypart in snake.coordinates[1:]:
            if x==bodypart[0] and y== bodypart[1]:
                game_over()

#game over screen 
def game_over():
    food.visible=False
    
    for i in snake.squares:
        i.visible=False
    
        
    app.background='black'
    Label("GAME OVER!", 200, 190, fill='white', bold=True, size=30, font='caveat')
    Label('Final Score = ' +  str(counter), 200, 230,fill='white', bold=True, size=30, font='caveat' )
    app.stop()
def win():
    food.visible=False
    
    for i in snake.squares:
        i.visible=False
    
    app.background='black'
    Label("YOU WIN!", 200, 190, fill='white', bold=True, size=30, font='caveat')
    Label('Final Score = ' +  str(counter), 200, 230,fill='white', bold=True, size=30, font='caveat' )
    app.stop()
snake()
Food()

def onStep():
    
    next_turn(snake, food)
    checkcollsions(snake)
    foodCheck()
    if counter==97:
        win()
        app.stop()

cmu_graphics.run()





















