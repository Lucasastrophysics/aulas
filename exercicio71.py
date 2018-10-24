#exercício 7.1
import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    t.forward(0)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor(input('insira a cor de fundo '))

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color(input('insira a cor da borda '), input('insira a cor do histograma '))
tess.pensize(3)
arq = open('valores.dat','r') 
xs = arq.readlines()

for a in xs:
    if '#' in a:
       print('os elementos com # serão considerados como comentários')
    else:
       draw_bar(tess, float(a))
