'''
def rectify(s):
    rec = '0123456789.-'
    s = s.strip()
    if s == '':
        return False
    while s[0] == '0':
        s = s[1:]
    for i in s:
        if i not in rec:
            return False
    if '-' in s:
        if s.count('-') > 1:
            return False
        if s[0] != '-':
            return False
    if '.' in s:
        if s.count('.') > 1:
            return False
    return True
'''

'''
        if draw_times == 0:
            draw_times += 1
            draw_turtle()
        else:
            text = 'к сожалению, программа может\nпоказать рисунок только один раз'
            tkm.showwarning(message=text, title='извините') 
        '''

'''
def dots_line(t, x):
    x = int(x)
    t.width(5)
    for _ in range(x//20):
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()
    t.forward(x%20)
    
def triangle_draw(t):
    t.width(5)
    t.right(60)
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(120)
    t.forward(40)
    t.right(60)

def force_draw(t, f):
    t.width(4)
    t.pencolor('red')
    t.forward(f)
    t.right(120)
    t.forward(10)
    t.backward(10)
    t.right(120)
    t.forward(10)
    t.backward(10)
    t.left(240)
    t.backward(f)
    t.pencolor('black')

def draw_turtle():
    global alfa, beta, teta, force_f, force_r, draw_times
    force_f *= 3
    force_r *= 3

    final_2 = False

    alfa_r = math.radians(alfa)
    beta_r = math.radians(beta)

    if alfa == 90:
        l_1 = math.tan(beta_r)
        l_2 = 1/math.cos(beta_r)
    else:
        alfa_beta = math.sin(alfa_r-beta_r)
        l_1 = math.sin(beta_r)/alfa_beta
        l_2 = math.sin(math.pi-alfa_r)/alfa_beta

    value = math.cos(math.pi-alfa_r)

    if value > l_1:
        k = 590/(1+value)
        final_2 = True
    else:
        k = 590/(1+l_1) 

    l_1 *= k
    l_2 *= k

    t = tr.Turtle()
    t.speed(0.2)

    t.width(5)
    t.right(90)

    if final_2:
        dots_line(t, 300)
    else:
        t.penup()
        t.forward(300)
        t.pendown()
    
    t.penup()
    t.backward(k)
    t.pendown()
    t.left(alfa)

    t.width(4)
    t.forward(k/2)
    t.right(alfa)
    
    force_draw(t, force_f)

    t.left(alfa)
    t.forward(k/2)
    t.left(180-beta)

    t.width(2)
    t.forward(l_2)
    t.left(180-alfa+beta)

    triangle_draw(t)

    if final_2:
        t.penup()
        t.forward(l_1)
        t.pendown()
    else:
        dots_line(t, l_1)
        
    triangle_draw(t)

    t.left(180-teta)
    
    force_draw(t, force_r)
    
    if final_2:
        t.width(5)
        t.left(teta)
        dots_line(t, value*k)
        t.penup()
        t.forward(50)
    else:
        t.right(180-teta)
        dots_line(t, k)
        t.penup()
        t.forward(50)

    t.screen.mainloop()
    '''