from random import randint

#10x10 figur, med 6 muligheder 
def setup():
    size(500,500)
def draw():
    pass

def keyPressed():
    if key == '1':
       background(255)
       for i in range(0,10):
        for j in range(0,10):
            r = randint(1,6)
            if r == 1:
                strokeWeight(2);
                stroke(0,100,200)
                line(5+25*i,5+25*j,5+25*i,20+25*j)
                line(5+25*i,20+25*j,20+25*i,20+25*j)
            if r == 2:
                stroke(100,100,200)
                line(5+25*i,20+25*j,20+25*i,20+25*j)
                line(20+25*i,0+25*j,20+25*i,5+25*j)
            if r == 3:
                stroke(100,0,200)
                line(5+25*i,20+25*j,5+25*i,5+25*j)
                line(5+25*i,5+25*j,20+25*i,5+25*j)    
            if r == 4:
                stroke(200,100,300)
                line(5+25*i,5+25*j,20+25*i,5+25*j)
                line(20+25*i,5+25*j,20+25*i,20+25*j)        
            if r == 5:
                stroke(100,100,200)
                line(5+25*i,5+25*j,20+25*i,5+25*j)
                line(5+25*i,20+25*j,20+25*i,20+25*j)    
            if r == 6:
                stroke(100,100,300)
                line(5+25*i,5+25*j,5+25*i,20+25*j)
                line(20+25*i,5+25*j,20+25*i,20+25*j)   

#Med loops kører den inderste først, indtil den ikke kan mere og så tjekker den anden loop,
#kører det ignnem og rundt indtil begge lopps er opfyldt og så afslutter den 
