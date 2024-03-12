# ======================================================================================= necessary libraries
import tkinter as tk
import turtle as tr
import math

# ====================================================================================================== bugs
'''
se necesita redimencionar imagenes
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

    return r, teta

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

    def error(self):
        error = caution()
        error.mainloop()

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
                forcer, t_ta = solve_problem(alfa, beta, force_f)
                condition_1 = (round(forcer, ndigits=1) == round(force_r, ndigits=1))
                condition_2 = (round(t_ta, ndigits=1) == round(teta, ndigits=1))
                if  condition_1 and condition_2:
                    self.destroy()
                    congra_v = congra()
                    congra_v.mainloop()
                else:
                    self.destroy()
                    expl1 = expl_1()
                    expl1.mainloop()
            elif count_1 == 3:
                force_r, teta = solve_problem(alfa, beta, force_f)
                self.destroy()
                expl1 = expl_1()
                expl1.mainloop()
            else:
               error = caution()
               error.mainloop()
        else:
            error = caution()
            error.mainloop()
# ========================================================================================= window definition

# ======================================================================== primary window

class firsh_window(tk.Tk, Functions):
    def __init__(self):
        super().__init__()

        self.w_h_screen()

        self.title('главное окно')

        self.img = tk.PhotoImage(file='imagen.png')
        self.label1 = tk.Label(self, image=self.img)
        self.label1.pack()

        self.button = tk.Button(self, text='меню', command=self.go_menu)
        self.button.pack()

# ================================================================================== menu

class menu(tk.Tk, Functions):
    def __init__(self):
        global alfa, beta, teta, force_f, force_r
        
        super().__init__()

        self.w_h_screen()

        self.title('меню')

        self.marco_1 = tk.Frame(self)

        self.marco_a_1 = tk.Frame(self.marco_1)

        self.input_alfa = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_alfa.place(rely=0, relx=0.133, relwidth=0.08, relheight=1)

        self.l_alfa = tk.Label(self.marco_a_1, text=f'{chr(945)}{chr(176)}=', font='calibri 25')
        self.l_alfa.place(rely=0, relx=0.088, relheight=1, relwidth=0.044)

        self.input_beta = tk.Entry(self.marco_a_1, font='calibri 20')
        self.input_beta.place(rely=0, relx=0.302, relwidth=0.08, relheight=1)

        self.l_beta = tk.Label(self.marco_a_1, text=f'{chr(946)}{chr(176)}=', font='calibri 25')
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

        self.l_teta = tk.Label(self.marco_a_1, text=f'{chr(952)}{chr(176)}=', font='calibri 25')
        self.l_teta.place(rely=0, relx=0.791, relheight=1, relwidth=0.044)

        self.marco_1.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        self.marco_a_1.place(rely=0.45, relx=0, relwidth=1, relheight=0.259)

        self.marco_2 = tk.Frame(self)

        self.marco_a_2 = tk.Frame(self.marco_2)

        self.button_ro = tk.Button(self.marco_a_2, text='условие', command=self.root, font='calibri 18')
        self.button_ro.place(rely=0, relx=0.473, relheight=1)

        self.button_p = tk.Button(self.marco_2, text='prueva boton', command=self.step_1)
        #self.button_p.pack()

        self.button_f = tk.Button(self.marco_2, text='felcitar', command=self.congratulate)
        #self.button_f.pack()

        self.button_ca = tk.Button(self.marco_a_2, text='вычислять', command=self.calculate, font='calibri 18')
        self.button_ca.place(rely=0, relx=0.8, relheight=1)

        self.button_ce = tk.Button(self.marco_a_2, text='закрыть', command=self.close_all, font='calibri 18')
        self.button_ce.place(rely=0, relx=0.1, relheight=1)

        self.marco_2.place(rely=0.2, relx=0, relheight=0.2, relwidth=1)

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

        self.titulo = tk.Label(self.marco_1, text='1. вычислять силы', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.marco_2.place(relx=0,rely=0.111, relwidth=1, relheight=0.712)

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

        self.titulo = tk.Label(self.marco_1, text='2. вычислять момент', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

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

        self.marco_1 = tk.Frame(self)

        self.titulo = tk.Label(self.marco_1, text='3. вычислять R и θ', font='calibri 23')
        self.titulo.place(relx=0.05, rely=0.333)

        self.marco_1.place(relx=0,rely=0, relwidth=1, relheight=0.111)

        self.marco_2 = tk.Frame(self)

        self.button_m = tk.Button(self.marco_2, text='посмотреть рисунок', command=self.draw, font='calibri 18')
        self.button_m.place(rely=0.5, relx=0.43)

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

# ======================================================================== warning window

class caution(tk.Tk):
    def __init__(self):
        global alfa, beta, force_f, rect_alfa, rect_beta, rect_f

        super().__init__()

        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()

        width_window = 320
        height_window = 310

        x = (width_screen - width_window) // 2
        y = (height_screen - height_window) // 2

        self.geometry(f'{width_window}x{height_window}+{x}+{y}')
        self.title('предупреждение')

        #mensaje += f'   пробел R является пустым.\n'
        #mensaje += f'   пробел {chr(952)}{chr(176)} является пустым.\n'

        s_rect = '0123456789.-'

        mensaje = '''
параметры неправильные, следующие 
настройки должны быть выполнены:
'''

        if rect_alfa == '':
            mensaje += f'   пробел {chr(945)}{chr(176)} является пустым.\n'
        else:
            for i in rect_alfa:
                if i not in s_rect:
                    mensaje += f'    hay simbolos extra;os en alfa\n'
                    break
        
        if rect_beta == '':
            mensaje += f'   пробел {chr(946)}{chr(176)} является пустым.\n'
        else:
            for i in rect_beta:
                if i not in s_rect:
                    mensaje += f'    hay simbolos extra;os en beta\n'
                    break
        
        if rect_f == '':
            mensaje += f'   пробел F является пустым.\n'
        else:
            for i in rect_f:
                if i not in s_rect:
                    mensaje += f'    hay simbolos extra;os en f\n'
                    break

        if rectify(rect_alfa) and rectify(rect_beta):
            if not 0 < alfa < 180:
                mensaje += f'   0 < {chr(945)}{chr(176)} < 90.\n'

            if alfa == 90:
                if not 0 < beta < 90:
                    mensaje += f'   0 < {chr(946)}{chr(176)} < 90.\n'
            else:
                if not 0 < beta < alfa:
                    mensaje += f'   0 < {chr(946)}{chr(176)} < {chr(945)}{chr(176)}'

        if rectify(rect_f):
            if force_f < 0:
                mensaje += f'   F > 0\n'
            
        mensaje += 'пожалуйста, вновь ввести параметры.'

        self.label = tk.Label(self, text=mensaje, font='calibri 13')
        self.label.pack()

        self.button = tk.Button(self, text='закрыть', command=self.destroy, font='calibri 13')
        self.button.pack()
        #self.button.place(relx=0.394, rely=0.85)

# ============================================================================================ warning window

root = firsh_window()
root.mainloop()