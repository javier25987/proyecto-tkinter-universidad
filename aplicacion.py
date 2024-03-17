# ======================================================================================= necessary libraries
import tkinter as tk
import turtle as tr
import math
import tkinter.messagebox as tkm

# ====================================================================================================== bugs
'''
apriori no es un bug pero las formulas se ven raritas 
'''
# ==================================================================================== definition of elements

width_window = 1000
height_window = 600

alfa = 0
beta = 0
teta = 0
force_f = 0
force_r = 0

rect_alfa = ''
rect_beta = ''
rect_f = ''

# =================================================================== definition of functions within the code

def solve_problem(alfa, beta, f):
    alfa = math.radians(alfa)
    beta = math.radians(beta)
    fact = math.pi/2
    b_ta = fact + beta

    if alfa == fact:
        phi = math.pi - beta
    else:
        phi = fact + alfa - beta

    if alfa == fact:
        p = (-f)/(2*math.cos(b_ta))
    elif alfa < fact:
        p = (-f*math.cos(fact-alfa))/(2*math.cos(b_ta))
    else:
        p = (-f*math.cos(alfa-fact))/(2*math.cos(b_ta))

    r_x = -p*math.cos(phi)
    r_y = f-(p*math.sin(phi))

    r = round(math.sqrt(r_x**2 + r_y**2), 2)
    teta = round(math.degrees(math.acos(r_y/r)), 2)

    return r, teta, r_x, r_y

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
        
def error_window():
    global alfa, beta, force_f, rect_alfa, rect_beta, rect_f
    s_rect = '0123456789.-'
    count = 0

    mensage = '''
параметры неправильные, должно 
быть исправлено следующее:
'''

    if rect_alfa == '':
        mensage += f'>  α° является пустым.\n'
    else:
        if '-' in rect_alfa:
             if rect_alfa.count('-') > 1 or rect_alfa[0] != '-':
                mensage += f'>  в α° неправильно использован знак минус(-)\n'
        if '.' in rect_alfa:
             if rect_alfa.count('.') > 1:
                mensage += f'>  в α° использовано больше одной точки(.)\n'
        for i in rect_alfa:
            if i not in s_rect:
                mensage += f'>  в α° использован недопустимый символ({i})\n'
                count += 1
                break
        
    if rect_beta == '':
        mensage += f'>  β° является пустым.\n'
    else:
        if '-' in rect_beta:
            if rect_beta.count('-') > 1 or rect_beta[0] != '-':
                mensage += f'>  в β° неправильно использован знак минус(-)\n'
        if '.' in rect_beta:
            if rect_beta.count('.') > 1:
                mensage += f'>  в β° использовано больше одной точки(.)\n'
        for i in rect_beta:
            if i not in s_rect:
                mensage += f'>  в β° использован недопустимый символ({i})\n'
                count += 1
                break
        
    if rect_f == '':
        mensage += f'>  F является пустым.\n'
    else:
        if '-' in rect_f:
           if rect_f.count('-') > 1 or rect_f[0] != '-':
                mensage += f'>  в F неправильно использован знак минус(-)\n'
        if '.' in rect_f:
            if rect_f.count('.') > 1:
                mensage += f'>  в F использовано больше одной точки(.)\n'
        for i in rect_f:
            if i not in s_rect:
                mensage += f'>  в F использован недопустимый символ({i})\n'
                count += 1
                break

    if rectify(rect_alfa) and rectify(rect_beta):
        if not 0 < alfa < 180:
            mensage += f'>   0 < α° < 180°.\n'

        if alfa == 90:
            if not 0 < beta < 90:
                mensage += f'>  0 < β° < 90°.\n'
        else:
            if not 0 < beta < alfa:
                mensage += f'>  0 < β° < α°\n'

    if rectify(rect_f):
        if force_f < 0:
            mensage += f'>  0 < F\n'
    
    if count > 0:
        mensage += f'>  в использовании допустимы только эти символы {s_rect}\n'
            
    mensage += 'пожалуйста, введите параметры снова.'

    tkm.showwarning(message=mensage,title='предупреждение')

class Tortuga():
    def __init__(self):
        self.t = tr.Turtle()

        self.t.screen.mainloop()

class Functions(Tortuga):
    def __init__(self):
        pass

    def draw(self):
        Tortuga()

    def close_all(self):
        self.destroy()

    def go_menu(self):
        self.destroy()
        menu_v = menu()
        menu_v.mainloop()

    def congratulate(self):
        self.destroy()
        congra_v = congra()
        congra_v.mainloop()

    def step_1(self):
        self.destroy()
        expl1 = expl_1()
        expl1.mainloop()

    def step_2(self):
        self.destroy()
        expl2 = expl_2()
        expl2.mainloop()
    
    def step_3(self):
        self.destroy()
        expl3 = expl_3()
        expl3.mainloop()

    def root(self):
        self.destroy()
        root_v = firsh_window()
        root_v.mainloop()

    def zoom_screen(self):
        self.state("zoomed")

    def w_h_screen(self):
        global width_window, height_window

        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()

        x = (width_screen - width_window) // 2
        y = (height_screen - height_window) // 2

        self.geometry(f'{width_window}x{height_window}+{x}+{y}')
    
    def calculate(self):
        global alfa, beta, teta, force_f, force_r, rect_alfa, rect_beta, rect_f

        count_1 = 0
        count_2 = 0
        valuar = False

        rect_alfa = str(self.input_alfa.get())
        
        if rectify(rect_alfa):
            alfa = float(self.input_alfa.get())
            count_1 += 1

        rect_beta = str(self.input_beta.get())

        if rectify(rect_beta):
            beta = float(self.input_beta.get())
            count_1 += 1

        if rectify(str(self.input_teta.get())):
            teta = float(self.input_teta.get())
            count_2 += 1
        else:
            teta = 0

        rect_f = str(self.input_force_f.get())

        if rectify(rect_f):
            force_f = float(self.input_force_f.get())
            count_1 += 1

        if rectify(str(self.input_force_r.get())):
            force_r = float(self.input_force_r.get())
            count_2 += 1
        else:
            force_r = 0

        if alfa == 90:
            if 0 < beta < 90:
                valuar = True
        else:
            if 0 < beta < alfa:
                valuar = True

        if force_f < 0:
            valuar = False

        if not 0 < alfa < 180:
            valuar = False

        if valuar:
            if (count_1 + count_2) == 5:
                forcer, t_ta, _, _ = solve_problem(alfa, beta, force_f)
                condition_1 = (round(forcer, ndigits=2) == round(force_r, ndigits=2))
                condition_2 = (round(t_ta, ndigits=2) == round(teta, ndigits=2))
                if  condition_1 and condition_2:
                    self.destroy()
                    congra_v = congra()
                    congra_v.mainloop()
                else:
                    self.destroy()
                    expl1 = expl_1()
                    expl1.mainloop()
            elif count_1 == 3:
                force_r, teta, _, _ = solve_problem(alfa, beta, force_f)
                self.destroy()
                expl1 = expl_1()
                expl1.mainloop()
            else:
                error_window()
        else:
            error_window()   
# ========================================================================================= window definition

# ======================================================================== primary window

class firsh_window(tk.Tk, Functions):
    def __init__(self):
        super().__init__()

        self.w_h_screen()

        self.title('главное меню')

        self.marco_1 = tk.Frame(self)

        text_problem = '''Однородный стержень AB прикреплен к вертикальной
стене  посредством  шарнира  A и удерживается под 
углом 60° к вертикали при помощи троса BC,
образующего с ним угол 30°. Определить величину 
и направление реакции R шарнира, если известно, 
что вес стержня равен 20 Н.'''

        self.label = tk.Label(self.marco_1, text=text_problem, font='calibri 17')
        self.label.place(relx=0.016, rely=0.1)

        self.button = tk.Button(self.marco_1, text='начать', command=self.go_menu, font='calibri 20')
        self.button.place(relx=0.388, rely=0.5)

        self.marco_1.place(relx=0, rely=0, relheight=1, relwidth=0.555)

        self.marco_2 = tk.Frame(self)

        self.img = tk.PhotoImage(file='imagen_firsh_window.png')
        self.label1 = tk.Label(self.marco_2, image=self.img)
        self.label1.place(relx=0.044, rely=0.04)

        self.marco_2.place(relx=0.555, rely=0, relheight=1, relwidth=0.444)

# ================================================================================== menu

class menu(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('меню')

        self.marco_1 = tk.Frame(self)

        self.marco_a_1 = tk.Frame(self.marco_1)

        self.label_input = tk.Label(self, text='даны параметры', font='calibri 20')
        self.label_input.place(relx=0.085, rely=0.04)

        self.label_get = tk.Label(self, text='ваш ответ', font='calibri 20')
        self.label_get.place(relx=0.625, rely=0.04)

        self.input_alfa = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_alfa.place(rely=0, relx=0.133, relwidth=0.08, relheight=1)

        self.l_alfa = tk.Label(self.marco_a_1, text=f'α°=', font='calibri 25')
        self.l_alfa.place(rely=0, relx=0.088, relheight=1, relwidth=0.044)

        self.input_beta = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_beta.place(rely=0, relx=0.302, relwidth=0.08, relheight=1)

        self.l_beta = tk.Label(self.marco_a_1, text=f'β°=', font='calibri 25')
        self.l_beta.place(rely=0, relx=0.257, relheight=1, relwidth=0.044)

        self.input_force_f = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_force_f.place(rely=0, relx=0.471, relwidth=0.08, relheight=1)

        self.l_f_f = tk.Label(self.marco_a_1, text=f'F=', font='calibri 25')
        self.l_f_f.place(rely=0, relx=0.426, relheight=1, relwidth=0.044)

        self.input_force_r = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_force_r.place(rely=0, relx=0.666, relwidth=0.08, relheight=1)

        self.l_f_r = tk.Label(self.marco_a_1, text=f'R=', font='calibri 25')
        self.l_f_r.place(rely=0, relx=0.622, relheight=1, relwidth=0.044)

        self.input_teta = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_teta.place(rely=0, relx=0.835, relwidth=0.08, relheight=1)

        self.l_teta = tk.Label(self.marco_a_1, text=f'θ°=', font='calibri 25')
        self.l_teta.place(rely=0, relx=0.791, relheight=1, relwidth=0.044)

        self.marco_1.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.marco_a_1.place(rely=0.65, relx=0, relwidth=1, relheight=0.259)

        self.marco_2 = tk.Frame(self)

        self.marco_a_2 = tk.Frame(self.marco_2)

        self.button_ro = tk.Button(self.marco_a_2, text='условие', command=self.root, font='calibri 18')
        self.button_ro.place(rely=0, relx=0.473, relheight=1)

        self.button_ca = tk.Button(self.marco_a_2, text='вычислить', command=self.calculate, font='calibri 18')
        self.button_ca.place(rely=0, relx=0.8, relheight=1)

        self.button_ce = tk.Button(self.marco_a_2, text='закрыть', command=self.close_all, font='calibri 18')
        self.button_ce.place(rely=0, relx=0.1, relheight=1)

        self.marco_2.place(rely=0.25, relx=0, relheight=0.2, relwidth=1)

        self.marco_a_2.place(rely=0.15, relx=0, relheight=0.296, relwidth=1)

        self.marco_3 = tk.Frame(self)

        self.marco_a_3 = tk.Frame(self.marco_3)

        self.img_m = tk.PhotoImage(file='imagen_menu.png')
        self.img_l = tk.Label(self.marco_a_3, image=self.img_m)
        self.img_l.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.marco_3.place(rely=0.4, relx=0, relheight=0.6, relwidth=1)

        self.marco_a_3.place(relx=0.022, rely=0, relheight=0.938, relwidth=0.955)

# ===================================================================== first explanation

class expl_1(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r

        super().__init__()

        self.w_h_screen()

        self.title('шаг_1')

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='1. вычислить силы', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2, bg='white')

        self.marco_2_1.place(relx=0.044, rely=0, relwidth=0.322, relheight=1)

        self.marco_2_2 = tk.Frame(self.marco_2)

        text_1 = '''Чтобы найти R, мы должны построить диаграмму всех сил, чтобы знать,
какие силы необходимы для получения результата.'''

        text_2 = '''мы видим, что R может быть найдено, если мы знаем компоненты Rx и
Ry, поэтому мы приступаем к их получению.'''

        text_3 = '''Теперь мы сталкиваемся с проблемой, что нам неизвестны значения
P и ȹ, поэтому мы приступаем к их поиску, ȹ можно найти с помощью 
диаграммы, а P - с помощью момента в точке A (перейдите к 
следующему шагу).'''

        self.label_1 = tk.Label(self.marco_2_2, text=text_1, font='calibri 13')
        self.label_1.pack()

        eq_1 = f'X: Rₓ + P·cos({chr(966)}) = 0 \nY: Rᵧ - F + P·sin({chr(966)}) = 0'

        self.label_eq_1 = tk.Label(self.marco_2_2, text=eq_1, font='courier 18 italic')
        self.label_eq_1.pack()

        self.label_2 = tk.Label(self.marco_2_2, text=text_2, font='calibri 13')
        self.label_2.pack()

        eq_2 = f'Rₓ = -P·cos({chr(966)}) \nRᵧ = F - P·sin({chr(966)})'

        self.label_eq_2 = tk.Label(self.marco_2_2, text=eq_2, font='courier 18 italic')
        self.label_eq_2.pack()

        self.label_3 = tk.Label(self.marco_2_2, text=text_3, font='calibri 13')
        self.label_3.pack()

        if alfa == 90:
            eq_n = f'{chr(966)} = 180 - β'
        else:
            eq_n = f'{chr(966)} = 90 + α - β'
            
        self.label_eq_n = tk.Label(self.marco_2_2, text=eq_n, font='courier 18 italic')
        self.label_eq_n.pack()

        self.marco_2_2.place(relx=0.377, rely=0, relwidth=0.577, relheight=1)

        self.marco_2.place(relx=0, rely=0.111, relwidth=1, relheight=0.712)

        self.marco_3 = tk.Frame(self)

        self.button = tk.Button(self.marco_3, text='следующий шаг', command=self.step_2, font='calibri 18')
        self.button.place(rely=0.333, relx=0.733, relheight=0.333)

        self.button_m = tk.Button(self.marco_3, text='меню', command=self.go_menu, font='calibri 18')
        self.button_m.place(rely=0.333, relx=0.088, relheight=0.333)

        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ==================================================================== second explanation

class expl_2(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('шаг_2')

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='2. вычислить момент', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2, bg='white')

        self.marco_2_1.place(relx=0.05, rely=0, relheight=1, relwidth=0.5)

        self.marco_2_2 = tk.Frame(self.marco_2)

        text_1 = '''С помощью диаграммы мы можем получить 
момент в точке A.'''

        text_2 = 'Теперь мы можем узнать из M значение P'

        text_3 = ''' Получив значение P, мы можем перейти к 
последнему шагу, которыйзаключается 
в нахождении R и θ.'''

        self.label_1 = tk.Label(self.marco_2_2, text=text_1, font='calibri 13')
        self.label_1.pack()

        if alfa == 90:
            eq_1 = f'Mₐ: 0.5·l·F+l·P·cos(-(90+β)) = 0'
            eq_2 = f'0.5·F + P·cos(90+β) = 0 \nP·cos(90+β) = -0.5·F \nP = -F/(2·cos(90+β))'
        elif alfa < 90:
            eq_1 = f'Mₐ: 0.5·l·F·cos(-δ₆)+l·P·cos(-(90+β)) = 0'
            eq_2 = f'0.5·F·cos(δ₆)+P·cos(90+β) = 0 \nP·cos(90+β) = -0.5·F·cos(δ₆) \nP = (-F·cos(δ₆))/(2·cos(90+β)) \nδ₆ = 90 - α'
        elif alfa > 90:
            eq_1 = f'Mₐ: 0.5·l·F·cos(δ₅)+l·P·cos(-(90+β)) = 0'
            eq_2 = f'0.5·F·cos(δ₅) + P·cos(90+β) = 0 \nP·cos(90+β) = -0.5·F·cos(δ₅) \nP = (-F·cos(δ₅))/(2·cos(90+β)) \nδ₅ = α - 90'

        self.label_eq_1 = tk.Label(self.marco_2_2, text=eq_1, font='courier 15 italic')
        self.label_eq_1.pack()

        self.label_2 = tk.Label(self.marco_2_2, text=text_2, font='calibri 13')
        self.label_2.pack()

        self.label_eq_2 = tk.Label(self.marco_2_2, text=eq_2, font='courier 18 italic')
        self.label_eq_2.pack()

        self.label_3 = tk.Label(self.marco_2_2, text=text_3, font='calibri 13')
        self.label_3.pack()

        self.marco_2_2.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)

        self.marco_2.place(relx=0,rely=0.111, relwidth=1, relheight=0.712)

        self.marco_3 = tk.Frame(self)

        self.button = tk.Button(self.marco_3, text='следующий шаг', command=self.step_3, font='calibri 18')
        self.button.place(rely=0.333, relx=0.733, relheight=0.333)

        self.button = tk.Button(self.marco_3, text='предыдущий шаг', command=self.step_1, font='calibri 18')
        self.button.place(rely=0.333, relx=0.088, relheight=0.333)

        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ==================================================================== second explanation

class expl_3(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('шаг_3')

        r, t_ta, r_x, r_y = solve_problem(alfa, beta, force_f)

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='3. вычислять R и θ', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2)

        text_1 = 'Взяв значения P и ȹ, вспомнив формулы Rx и Ry, заменим их и получим результирующую силу.'

        eq_1 = f'Rₓ = -P·cos({chr(966)}) = {r_x:.2f}      Rᵧ = F - P·sin({chr(966)}) = {r_y:.2f}'

        self.label_1 = tk.Label(self.marco_2_1, text=text_1, font='calibri 13')
        self.label_1.place(relx=0, rely=0)

        self.label_eq_1 = tk.Label(self.marco_2_1, text=eq_1, font='courier 18 italic')
        self.label_eq_1.place(relx=0.097, rely=0.45)

        self.marco_2_1.place(relx=0.055, rely=0, relheight=0.315, relwidth=0.888)

        self.marco_2_2 = tk.Frame(self.marco_2)

        text_2 = 'С помощью теоремы Пифагора и решения θ получаем следующие формулы, в которые можно подставить значения R и θ.'

        eq_2 = f'R² = Rₓ² + Rᵧ² \nR = {r:.2f}'
        eq_3 = f'cos(θ) = Rₓ/R \nθ = arcos(Rₓ/R) = {t_ta:.2f}'

        self.label_2 = tk.Label(self.marco_2_2, text=text_2, font='calibri 13')
        self.label_2.place(relx=0, rely=0)

        self.label_eq_2 = tk.Label(self.marco_2_2, text=eq_2, font='courier 18 italic')
        self.label_eq_2.place(relx=0.1, rely=0.5)

        self.label_eq_3 = tk.Label(self.marco_2_2, text=eq_3, font='courier 18 italic')
        self.label_eq_3.place(relx=0.45, rely=0.5)

        self.marco_2_2.place(relx=0.055, rely=0.341, relheight=0.315, relwidth=0.9)

        self.marco_2_3 = tk.Frame(self.marco_2)

        self.button_m = tk.Button(self.marco_2_3, text='посмотреть рисунок', command=self.draw, font='calibri 18')
        self.button_m.place(relx=0.375, rely=0.3)

        self.marco_2_3.place(relx=0.055, rely=0.682, relheight=0.315, relwidth=0.888)

        self.marco_2.place(relx=0,rely=0.111, relwidth=1, relheight=0.712)

        self.marco_3 = tk.Frame(self)

        self.button = tk.Button(self.marco_3, text='меню', command=self.go_menu, font='calibri 18')
        self.button.place(rely=0.333, relx=0.831, relheight=0.333) 

        self.button = tk.Button(self.marco_3, text='предыдущий шаг', command=self.step_2, font='calibri 18')
        self.button.place(rely=0.333, relx=0.088, relheight=0.333)
        
        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ================================================================= congratulatory window

class congra(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('поздравления')

        self.marco_1 = tk.Frame(self)

        self.label = tk.Label(self, text='Поздравляем. Все параметры верны.', font='calibri 40')
        self.label.place(relx=0.08, rely=0.2)

        self.button_m = tk.Button(self, text='посмотреть рисунок', command=self.draw, font='calibri 18')
        self.button_m.place(rely=0.55, relx=0.388, relheight=0.063)

        self.marco_1.place(relx=0, rely=0, relwidth=1, relheight=0.823)

        self.marco_2 = tk.Frame(self)

        self.button_m = tk.Button(self.marco_2, text='меню', command=self.go_menu, font='calibri 18')
        self.button_m.place(rely=0.333, relx=0.831, relheight=0.333) 

        self.button_ce = tk.Button(self.marco_2, text='закрыть', command=self.close_all, font='calibri 18')
        self.button_ce.place(rely=0.333, relx=0.088, relheight=0.333)
        
        self.marco_2.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)
# ===========================================================================================================

if __name__ == '__main__':
    root = firsh_window()
    root.mainloop()