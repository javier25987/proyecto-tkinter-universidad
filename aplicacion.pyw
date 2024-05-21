# ======================================================================================= necessary libraries
import tkinter as tk
import turtle as tr
import math
import tkinter.messagebox as tkm
# ====================================================================================================== bugs
'''
> the formulas have a linear format
'''
# ==================================================================================== definition of elements
width_window = 1000
height_window = 600

width_screen = 0
height_screen = 0

alpha = 60
beta = 30
teta = 60
force_f = 20
force_r = 10

rect_alpha = ''
rect_beta = ''
rect_f = ''

return_value = 0
# =================================================================== definition of functions within the code
def solve_problem(alpha, beta, f):
    alpha = math.radians(alpha)
    beta = math.radians(beta)
    fact = math.pi/2
    b_ta = fact + beta

    if alpha == fact:
        phi = math.pi - beta
    else:
        phi = fact + alpha - beta

    if alpha == fact:
        p = (-f)/(2*math.cos(b_ta))
    elif alpha < fact:
        p = (-f*math.cos(fact-alpha))/(2*math.cos(b_ta))
    else:
        p = (-f*math.cos(alpha-fact))/(2*math.cos(b_ta))

    r_x = -p*math.cos(phi)
    r_y = f-(p*math.sin(phi))

    r = round(math.sqrt(r_x**2 + r_y**2), 2)
    teta = round(math.degrees(math.acos(r_y/r)), 2)

    return r, teta, r_x, r_y

def rectify(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
def error_window():
    global alpha, beta, force_f, rect_alpha, rect_beta, rect_f
    s_rect = '0123456789.-'
    count = 0

    mensage = '''
параметры неправильные, должно 
быть исправлено следующее:
'''

    if rect_alpha == '':
        mensage += f'=>  α° является пустым.\n'
    else:
        if '-' in rect_alpha:
             if rect_alpha.count('-') > 1 or rect_alpha[0] != '-':
                mensage += f'=>  в α° неправильно использован знак минус (-)\n'
        if '.' in rect_alpha:
             if rect_alpha.count('.') > 1:
                mensage += f'=>  в α° использовано больше одной точки (.)\n'
        for i in rect_alpha:
            if i not in s_rect:
                mensage += f'=>  в α° использован недопустимый символ ({i})\n'
                count += 1
                break
        
    if rect_beta == '':
        mensage += f'=>  β° является пустым.\n'
    else:
        if '-' in rect_beta:
            if rect_beta.count('-') > 1 or rect_beta[0] != '-':
                mensage += f'=>  в β° неправильно использован знак минус (-)\n'
        if '.' in rect_beta:
            if rect_beta.count('.') > 1:
                mensage += f'=>  в β° использовано больше одной точки (.)\n'
        for i in rect_beta:
            if i not in s_rect:
                mensage += f'=>  в β° использован недопустимый символ ({i})\n'
                count += 1
                break
        
    if rect_f == '':
        mensage += f'=>  F является пустым.\n'
    else:
        if '-' in rect_f:
           if rect_f.count('-') > 1 or rect_f[0] != '-':
                mensage += f'=>  в F неправильно использован знак минус (-)\n'
        if '.' in rect_f:
            if rect_f.count('.') > 1:
                mensage += f'=>  в F использовано больше одной точки (.)\n'
        for i in rect_f:
            if i not in s_rect:
                mensage += f'=>  в F использован недопустимый символ ({i})\n'
                count += 1
                break

    if rectify(rect_alpha) and rectify(rect_beta):
        if not 0 < alpha < 180:
            mensage += f'=>   0 < α° < 180°.\n'

        if not 0 < beta < alpha:
            mensage += f'=>  0 < β° < α°\n'

    if rectify(rect_f):
        if force_f < 0:
            mensage += f'=>  0 < F\n'
    
    if count > 0:
        mensage += f'=>  в использовании допустимы только эти символы\n {s_rect}\n'
            
    mensage += 'пожалуйста, введите параметры снова.'

    tkm.showwarning(message=mensage, title='предупреждение')

class Functions():
    def __init__(self):
        pass

    def draw(self):
        self.destroy()
        make_draw().mainloop()

    def go_menu(self):
        global return_value
        return_value = 2
        
        self.destroy()
        menu().mainloop()

    def congratulate(self):
        global return_value
        return_value = 1
        
        self.destroy()
        congra().mainloop()

    def step_1(self):
        self.destroy()
        expl_1().mainloop()

    def step_2(self):
        self.destroy()
        expl_2().mainloop()
    
    def step_3(self):
        global return_value
        return_value = 0
        
        self.destroy()
        expl_3().mainloop()

    def root(self):
        self.destroy()
        firsh_window().mainloop()
        
    def go_back_funcion(self):
        global return_value
        
        match return_value:
            case 0:
                self.step_3()
            case 1:
                self.congratulate()
            case 2:
                self.go_menu()
            
        self.destroy()
        
    def close_all(self):
        self.destroy()
    
    def open_draw(self):
        global alpha, beta, force_f, rect_alpha, rect_beta, rect_f

        count = 0
        valuar = False

        rect_alpha = str(self.input_alpha.get())
        
        if rectify(rect_alpha):
            alpha = float(self.input_alpha.get())
            count += 1

        rect_beta = str(self.input_beta.get())

        if rectify(rect_beta):
            beta = float(self.input_beta.get())
            count += 1

        rect_f = str(self.input_force_f.get())

        if rectify(rect_f):
            force_f = float(self.input_force_f.get())
            count += 1
            
        if beta < alpha:
            valuar = True

        if force_f < 0:
            valuar = False

        if not 0 < alpha < 180:
            valuar = False
        
        if valuar:
            if count == 3:
                self.draw()
            else:
                error_window()
        else:
            error_window()
                
    def w_h_screen_firsh(self):
        global width_window, height_window, width_screen, height_screen

        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()

        x = (width_screen - width_window) // 2
        y = (height_screen - height_window) // 2

        self.geometry(f'{width_window}x{height_window}+{x}+{y-40}')

    def w_h_screen(self):
        global width_window, height_window, width_screen, height_screen

        x = (width_screen - width_window) // 2
        y = (height_screen - height_window) // 2

        self.geometry(f'{width_window}x{height_window}+{x}+{y-40}')
    
    def calculate(self):
        global alpha, beta, teta, force_f, force_r, rect_alpha, rect_beta, rect_f

        count_1 = 0
        count_2 = 0
        valuar = False

        rect_alpha = str(self.input_alpha.get())
        
        if rectify(rect_alpha):
            alpha = float(self.input_alpha.get())
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

        if beta < alpha:
            valuar = True

        if force_f < 0:
            valuar = False

        if not 0 < alpha < 180:
            valuar = False

        if valuar:
            if count_1 + count_2 == 5:
                force_r_p, teta_p, _, _ = solve_problem(alpha, beta, force_f)
                condition_1 = round(force_r_p, ndigits=2) == round(force_r, ndigits=2)
                condition_2 = round(teta_p, ndigits=2) == round(teta, ndigits=2)
                if  condition_1 and condition_2:
                    self.congratulate()
                else:
                    self.step_1()
            elif count_1 == 3:
                force_r, teta, _, _ = solve_problem(alpha, beta, force_f)
                self.step_1()
            else:
                error_window()
        else:
            error_window()   
# ========================================================================================= window definition

# ======================================================================== primary window

class firsh_window(tk.Tk, Functions):
    def __init__(self):
        super().__init__()

        self.w_h_screen_firsh()

        self.title('главное меню')

        self.marco_1 = tk.Frame(self)

        text_problem = '''Однородный стержень AB прикреплен к вертикальной
стене  посредством  шарнира  A и удерживается под 
углом 60° к вертикали при помощи троса BC,
образующего с ним угол 30°. Определить величину 
и направление реакции R шарнира, если известно, 
что вес стержня равен 20 Н.'''

        self.label_p = tk.Label(self.marco_1, text='условия задачи:', font='calibri 20')
        self.label_p.place(relx=0.016, rely=0.08)
        
        self.label = tk.Label(self.marco_1, text=text_problem, font='calibri 17')
        self.label.place(relx=0.016, rely=0.16)

        self.button = tk.Button(self.marco_1, text='начать', command=self.go_menu, font='calibri 25')
        self.button.config(cursor='hand2')
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
        global alpha, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('меню')

        self.marco_1 = tk.Frame(self)

        self.marco_a_1 = tk.Frame(self.marco_1)

        self.label_input = tk.Label(self, text='даны параметры', font='calibri 20')
        self.label_input.place(relx=0.085, rely=0.04)

        self.label_get = tk.Label(self, text='ваш ответ', font='calibri 20')
        self.label_get.place(relx=0.625, rely=0.04)
        
        self.circle_1 = tk.Label(self.marco_a_1, text='°', font='calibri 25')
        self.circle_1.place(rely=0, relx=0.203, relheight=1, relwidth=0.044)

        self.input_alpha = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_alpha.insert(0, f'{alpha}')
        self.input_alpha.place(rely=0, relx=0.133, relwidth=0.08, relheight=1)

        self.l_alpha = tk.Label(self.marco_a_1, text=f'α=', font='calibri 25')
        self.l_alpha.place(rely=0, relx=0.088, relheight=1, relwidth=0.044)
        
        self.circle_2 = tk.Label(self.marco_a_1, text='°', font='calibri 25')
        self.circle_2.place(rely=0, relx=0.372, relheight=1, relwidth=0.044)

        self.input_beta = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_beta.insert(0, f'{beta}')
        self.input_beta.place(rely=0, relx=0.302, relwidth=0.08, relheight=1)

        self.l_beta = tk.Label(self.marco_a_1, text=f'β=', font='calibri 25')
        self.l_beta.place(rely=0, relx=0.257, relheight=1, relwidth=0.044)
        
        self.label_h_1 = tk.Label(self.marco_a_1, text='Н', font='calibri 25')
        self.label_h_1.place(rely=0, relx=0.542, relheight=1, relwidth=0.044)

        self.input_force_f = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_force_f.insert(0, f'{force_f}')
        self.input_force_f.place(rely=0, relx=0.471, relwidth=0.08, relheight=1)

        self.l_f_f = tk.Label(self.marco_a_1, text=f'F=', font='calibri 25')
        self.l_f_f.place(rely=0, relx=0.426, relheight=1, relwidth=0.044)
        
        self.label_h_2 = tk.Label(self.marco_a_1, text='Н', font='calibri 25')
        self.label_h_2.place(rely=0, relx=0.738, relheight=1, relwidth=0.044)

        self.input_force_r = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_force_r.place(rely=0, relx=0.666, relwidth=0.08, relheight=1)

        self.l_f_r = tk.Label(self.marco_a_1, text=f'R=', font='calibri 25')
        self.l_f_r.place(rely=0, relx=0.622, relheight=1, relwidth=0.044)
        
        self.circle_3 = tk.Label(self.marco_a_1, text='°', font='calibri 25')
        self.circle_3.place(rely=0, relx=0.905, relheight=1, relwidth=0.044)

        self.input_teta = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_teta.place(rely=0, relx=0.835, relwidth=0.08, relheight=1)

        self.l_teta = tk.Label(self.marco_a_1, text=f'θ=', font='calibri 25')
        self.l_teta.place(rely=0, relx=0.791, relheight=1, relwidth=0.044)

        self.marco_1.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.marco_a_1.place(rely=0.65, relx=0, relwidth=1, relheight=0.259)

        self.marco_2 = tk.Frame(self)

        self.marco_a_2 = tk.Frame(self.marco_2)

        self.button_ro = tk.Button(self.marco_a_2, text='условие', command=self.root, font='calibri 18')
        self.button_ro.config(cursor='hand2')
        self.button_ro.place(rely=0, relx=0.5, relheight=1)

        self.button_ca = tk.Button(self.marco_a_2, text='вычислить', command=self.calculate, font='calibri 18')
        self.button_ca.config(cursor='hand2')
        self.button_ca.place(rely=0, relx=0.8, relheight=1)
        
        self.button_dr = tk.Button(self.marco_a_2, text='рисунок', command=self.open_draw, font='calibri 18')
        self.button_dr.config(cursor='hand2')
        self.button_dr.place(rely=0, relx=0.648, relheight=1)

        self.button_ce = tk.Button(self.marco_a_2, text='закрыть', command=self.close_all, font='calibri 18')
        self.button_ce.config(cursor='hand2')
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
        global alpha, beta, teta, force_f, force_r

        super().__init__()

        self.w_h_screen()

        self.title('шаг_1')

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='1. вычислить силы', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2)

        if alpha == 90:
            self.img_forces = tk.PhotoImage(file='forces_1.png')
        elif alpha < 90:
            self.img_forces = tk.PhotoImage(file='forces_2.png')
        elif alpha > 90:
            self.img_forces = tk.PhotoImage(file='forces_3.png')

        self.label_img_forces = tk.Label(self.marco_2_1, image=self.img_forces)
        self.label_img_forces.pack()

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

        eq_1 = f'X: Rₓ + P·cos({chr(966)}) = 0 \nY: Rᵧ - F + P·sin({chr(966)})=0'

        self.label_eq_1 = tk.Label(self.marco_2_2, text=eq_1, font='courier 18 italic')
        self.label_eq_1.pack()

        self.label_2 = tk.Label(self.marco_2_2, text=text_2, font='calibri 13')
        self.label_2.pack()

        eq_2 = f'Rₓ = -P·cos({chr(966)}) \nRᵧ = F - P·sin({chr(966)})'

        self.label_eq_2 = tk.Label(self.marco_2_2, text=eq_2, font='courier 18 italic')
        self.label_eq_2.pack()

        self.label_3 = tk.Label(self.marco_2_2, text=text_3, font='calibri 13')
        self.label_3.pack()

        if alpha == 90:
            eq_n = f'{chr(966)} = 180 - β'
        else:
            eq_n = f'{chr(966)} = 90 + α - β'
            
        self.label_eq_n = tk.Label(self.marco_2_2, text=eq_n, font='courier 18 italic')
        self.label_eq_n.pack()

        self.marco_2_2.place(relx=0.377, rely=0, relwidth=0.577, relheight=1)

        self.marco_2.place(relx=0, rely=0.111, relwidth=1, relheight=0.712)

        self.marco_3 = tk.Frame(self)

        self.button = tk.Button(self.marco_3, text='следующий шаг', command=self.step_2, font='calibri 18')
        self.button.config(cursor='hand2')
        self.button.place(rely=0.333, relx=0.733, relheight=0.333)

        self.button_m = tk.Button(self.marco_3, text='меню', command=self.go_menu, font='calibri 18')
        self.button_m.config(cursor='hand2')
        self.button_m.place(rely=0.333, relx=0.088, relheight=0.333)

        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ==================================================================== second explanation

class expl_2(tk.Tk, Functions):
    def __init__(self):
        global alpha, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('шаг_2')

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='2. вычислить момент', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2)

        if alpha == 90:
            self.img_moment = tk.PhotoImage(file='moment_1.png')
        elif alpha < 90:
            self.img_moment = tk.PhotoImage(file='moment_2.png')
        elif alpha > 90:
            self.img_moment = tk.PhotoImage(file='moment_3.png')

        self.label_img_moment = tk.Label(self.marco_2_1, image=self.img_moment)
        self.label_img_moment.place(relx=0)

        self.marco_2_1.place(relx=0.05, rely=0, relheight=1, relwidth=0.7)

        self.marco_2_2 = tk.Frame(self.marco_2)

        text_1 = '''С помощью диаграммы мы можем получить 
момент в точке A.'''

        text_2 = 'Теперь мы можем узнать из M значение P'

        text_3 = ''' Получив значение P, мы можем перейти к 
последнему шагу, которыйзаключается 
в нахождении R и θ.'''

        self.label_1 = tk.Label(self.marco_2_2, text=text_1, font='calibri 13')
        self.label_1.pack()

        if alpha == 90:
            eq_1 = f'Mₐ: 0.5·l·F+l·P·cos(-(90+β)) = 0'
            eq_2 = f'0.5·F + P·cos(90+β) = 0 \nP·cos(90+β) = -0.5·F \nP = -F/(2·cos(90+β))'
        elif alpha < 90:
            eq_1 = f'Mₐ: 0.5·l·F·cos(-δ₆)+l·P·cos(-(90+β))=0'
            eq_2 = f'0.5·F·cos(δ₆)+P·cos(90+β) = 0 \nP·cos(90+β) = -0.5·F·cos(δ₆) \nP = (-F·cos(δ₆))/(2·cos(90+β)) \nδ₆ = 90 - α'
        elif alpha > 90:
            eq_1 = f'Mₐ: 0.5·l·F·cos(δ₅)+l·P·cos(-(90+β))=0'
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

        self.button_c = tk.Button(self.marco_3, text='следующий шаг', command=self.step_3, font='calibri 18')
        self.button_c.config(cursor='hand2')
        self.button_c.place(rely=0.333, relx=0.733, relheight=0.333)

        self.button_p = tk.Button(self.marco_3, text='предыдущий шаг', command=self.step_1, font='calibri 18')
        self.button_p.config(cursor='hand2')
        self.button_p.place(rely=0.333, relx=0.088, relheight=0.333)

        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ==================================================================== second explanation

class expl_3(tk.Tk, Functions):
    def __init__(self):
        global alpha, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('шаг_3')

        r, t_ta, r_x, r_y = solve_problem(alpha, beta, force_f)

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='3. вычислять R и θ', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2_1 = tk.Frame(self.marco_2)

        text_1 = 'Взяв значения P и ȹ, вспомнив формулы Rx и Ry, заменим их и получим результирующую силу.'

        eq_1 = f'Rₓ = -P·cos({chr(966)}) = {r_x:.2f}       Rᵧ = F - P·sin({chr(966)}) = {r_y:.2f}'

        self.label_1 = tk.Label(self.marco_2_1, text=text_1, font='calibri 13')
        self.label_1.place(relx=0, rely=0)

        self.label_eq_1 = tk.Label(self.marco_2_1, text=eq_1, font='courier 18 italic')
        self.label_eq_1.place(relx=0.097, rely=0.45)

        self.marco_2_1.place(relx=0.055, rely=0, relheight=0.315, relwidth=0.888)

        self.marco_2_2 = tk.Frame(self.marco_2)

        text_2 = 'С помощью теоремы Пифагора и решения θ получаем следующие формулы, в которые можно подставить значения R и θ.'

        eq_2 = f'R² = Rₓ² + Rᵧ² \nR = {r:.2f}Н'
        eq_3 = f'cos(θ) = Rₓ/R\nθ = arсcos(Rₓ/R)\nθ = {t_ta:.2f}°'

        self.label_2 = tk.Label(self.marco_2_2, text=text_2, font='calibri 13')
        self.label_2.place(relx=0, rely=0)

        self.label_eq_2 = tk.Label(self.marco_2_2, text=eq_2, font='courier 18 italic')
        self.label_eq_2.place(relx=0.1, rely=0.4)

        self.label_eq_3 = tk.Label(self.marco_2_2, text=eq_3, font='courier 18 italic')
        self.label_eq_3.place(relx=0.45, rely=0.4)

        self.marco_2_2.place(relx=0.055, rely=0.341, relheight=0.315, relwidth=0.9)

        self.marco_2_3 = tk.Frame(self.marco_2)

        self.button_r = tk.Button(self.marco_2_3, text='посмотреть рисунок', command=self.draw, font='calibri 18')
        self.button_r.config(cursor='hand2')
        self.button_r.place(relx=0.375, rely=0.3)

        self.marco_2_3.place(relx=0.055, rely=0.682, relheight=0.315, relwidth=0.888)

        self.marco_2.place(relx=0,rely=0.111, relwidth=1, relheight=0.712)

        self.marco_3 = tk.Frame(self)

        self.button_m = tk.Button(self.marco_3, text='меню', command=self.go_menu, font='calibri 18')
        self.button_m.config(cursor='hand2')
        self.button_m.place(rely=0.333, relx=0.831, relheight=0.333) 

        self.button_p = tk.Button(self.marco_3, text='предыдущий шаг', command=self.step_2, font='calibri 18')
        self.button_p.config(cursor='hand2')
        self.button_p.place(rely=0.333, relx=0.088, relheight=0.333)
        
        self.marco_3.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)

# ================================================================= congratulatory window

class congra(tk.Tk, Functions):
    def __init__(self):
        global alpha, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('поздравления')

        self.marco_1 = tk.Frame(self)

        self.label = tk.Label(self, text='Поздравляем. Все параметры верны.', font='calibri 40')
        self.label.place(relx=0.08, rely=0.2)

        self.button_r = tk.Button(self, text='посмотреть рисунок', command=self.draw, font='calibri 18')
        self.button_r.config(cursor='hand2')
        self.button_r.place(rely=0.55, relx=0.388, relheight=0.063)

        self.marco_1.place(relx=0, rely=0, relwidth=1, relheight=0.823)

        self.marco_2 = tk.Frame(self)

        self.button_m = tk.Button(self.marco_2, text='меню', command=self.go_menu, font='calibri 18')
        self.button_m.config(cursor='hand2')
        self.button_m.place(rely=0.333, relx=0.831, relheight=0.333) 
        
        self.button_m = tk.Button(self.marco_2, text='решение', command=self.step_1, font='calibri 18')
        self.button_m.config(cursor='hand2')
        self.button_m.place(rely=0.333, relx=0.47, relheight=0.333) 

        self.button_ce = tk.Button(self.marco_2, text='закрыть', command=self.close_all, font='calibri 18')
        self.button_ce.config(cursor='hand2')
        self.button_ce.place(rely=0.333, relx=0.088, relheight=0.333)
        
        self.marco_2.place(relx=0,rely=0.823, relwidth=1, relheight=0.177)
        
# =========================================================================== draw window

class make_draw(tk.Tk, Functions):
    def __init__(self):
        global alpha, beta, force_f, force_r, teta
        
        super().__init__()
        
        self.w_h_screen()
        
        force_r, teta, _, _ = solve_problem(alpha, beta, force_f)
        
        self.label_alpha = tk.Label(self, text=f'α = {alpha:.2f}°', font='courier 18 italic')
        self.label_alpha.place(relx=0.025, rely=0.05)
        
        self.label_beta = tk.Label(self, text=f'β = {beta:.2f}°', font='courier 18 italic')
        self.label_beta.place(relx=0.025, rely=0.13)
        
        self.label_force_f = tk.Label(self, text=f'сила F = {force_f:.2f}Н', font='courier 18 italic')
        self.label_force_f.place(relx=0.025, rely=0.21)

        self.label_force_r = tk.Label(self, text=f'сила R = {force_r:.2f}Н', font='courier 18 italic')
        self.label_force_r.place(relx=0.025, rely=0.29)
        
        self.label_teta = tk.Label(self, text=f'θ = {teta:.2f}°', font='courier 18 italic')
        self.label_teta.place(relx=0.025, rely=0.37)
        
        self.canva = tk.Canvas(self, width=700, height=590)
        
        def create_tringle(x, y, k=4):
            self.canva.create_line(x, y, x-40, y+20, width=k, fill='black', capstyle=tk.ROUND)
            self.canva.create_line(x-40, y+20, x-40, y-20, width=k, fill='black', capstyle=tk.ROUND)
            self.canva.create_line(x, y, x-40, y-20, width=k, fill='black', capstyle=tk.ROUND)
            
            self.canva.create_line(x-40, y-20, x-48, y-12, width=2, capstyle=tk.ROUND)
            self.canva.create_line(x-40, y-12, x-48, y-4, width=2, capstyle=tk.ROUND)
            self.canva.create_line(x-40, y-4, x-48, y+4, width=2, capstyle=tk.ROUND)
            self.canva.create_line(x-40, y+4, x-48, y+12, width=2, capstyle=tk.ROUND)
            self.canva.create_line(x-40, y+12, x-48, y+20, width=2, capstyle=tk.ROUND)
            
        def create_angle(x, y, a_1, a_2, name, radius=70):  
            x_0, y_0 = x - radius, y - radius
            x_1, y_1 = x + radius, y + radius
            i_angle = a_1 + a_2/2
            radius += 15
            i_angle = math.radians(i_angle)
            x_n, y_n = x + radius*math.cos(i_angle), y - radius*math.sin(i_angle)
            
            self.canva.create_arc(x_0, y_0, x_1, y_1, start=a_1, extent=a_2, width=3)
            self.canva.create_text(x_n, y_n, text=name, font='courier 18 italic')
            
        def create_force(x_0, y_0, x_1, y_1, name):
            x = (x_0 + x_1)/2
            y = (y_0 + y_1)/2
            
            self.canva.create_line(x_0, y_0, x_1, y_1, width=7, fill='red', arrow='last', capstyle=tk.ROUND)
            self.canva.create_text(x + 20, y, text=name, font='courier 18 italic')
            
        alpha_r = math.radians(alpha)
        beta_r = math.radians(beta)
        
        if alpha == 90:
            ym_0 = math.tan(beta_r)
            xm_1 = 1
            ym_1 = 1
            h = 1 + ym_0
        elif alpha < 90:
            ym_0 = math.sin(beta_r)/math.sin(alpha_r-beta_r)
            xm_1 = math.sin(alpha_r)
            ym_1 = 1 - xm_1/math.tan(alpha_r)
            h = 1 + ym_0
        elif alpha > 90:
            ym_0 = math.sin(beta_r)/math.sin(alpha_r-beta_r)
            xm_1 = math.sin(alpha_r)
            ym_1 = 1 + math.sin(alpha_r - math.pi/2)
            
            if alpha - beta < 90:
                h = 1 + ym_0
            else:
                h = math.sin(alpha_r - math.pi/2) + 1
                
        k = 585 / h
        
        ym_0 *= k
        xm_1 *= k
        ym_1 *= k
        
        o_x = 230
        o_y = 620
        k_x = o_x
        k_y = o_y - k
        xm_1 = o_x + xm_1
        ym_1 = o_y - ym_1
        xm_0 = o_x
        ym_0 = o_y - (k + ym_0)
        
        _, _, teta_x, teta_y = solve_problem(alpha, beta, force_f)
        teta_x = teta_x*5 + k_x
        
        teta_y = k_y - teta_y*5
        p_x_f = (k_x + xm_1)/2
        p_y_f = (k_y + ym_1)/2
        
        self.canva.create_line(o_x, o_y, k_x, k_y, width=4, fill='black', dash=(200, 8, 5, 200), capstyle=tk.ROUND)
        self.canva.create_line(k_x, k_y, xm_1 , ym_1, width=4, fill='black', capstyle=tk.ROUND)
        self.canva.create_line(xm_0 , ym_0, xm_1 , ym_1,  width=4, fill='black', capstyle=tk.ROUND)
        self.canva.create_line(k_x, k_y, xm_0 , ym_0,  width=4, fill='black', dash=(200, 8, 5, 200), capstyle=tk.ROUND)
        
        self.canva.create_text(k_x-10, k_y-20, text='A', font='calibri 19')
        self.canva.create_text(xm_1+10 , ym_1, text='B', font='calibri 19')
        self.canva.create_text(xm_0, ym_0-15, text='C', font='calibri 19')
        
        create_tringle(k_x, k_y)
        create_tringle(xm_0, ym_0)
        
        create_angle(k_x, k_y, -90, alpha, 'α')
        
        create_force(p_x_f, p_y_f, p_x_f, p_y_f + (force_f*5), 'F')
        create_force(k_x, k_y, teta_x, teta_y, 'R')
        
        if alpha == 90:
            create_angle(xm_1 , ym_1, 180, -beta, 'β')
        elif alpha > 90:
            create_angle(xm_1 , ym_1, alpha-270, -beta, 'β')
        elif alpha < 90:
            create_angle(xm_1 , ym_1, 90+alpha, -beta, 'β')
            
        self.canva.place(x=290, y=5)
        
        self.buton = tk.Button(self, text='назад', command=self.go_back_funcion, font='calibri 18')
        self.buton.place(relx=0.85, rely=0.85)
        
        self.buton_c = tk.Button(self, text='закрыть',command=self.close_all, font='calibri 18')
        self.buton_c.place(relx=0.04, rely=0.85)
        
# ===========================================================================================================

if __name__ == '__main__':
    firsh_window().mainloop()