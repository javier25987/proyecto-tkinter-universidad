'''# ======================================================================== warning window

class caution(tk.Tk):
    def __init__(self):
        global alfa, beta, force_f, rect_alfa, rect_beta, rect_f

        super().__init__()

        width_screen = self.winfo_screenwidth()
        height_screen = self.winfo_screenheight()

        required_width = self.winfo_reqwidth() + 120
        required_height = self.winfo_reqheight()

        x = (width_screen - required_width) // 2
        y = (height_screen - required_height) // 2

        self.geometry(f'{required_width}x{required_height}+{x}+{y}')
        self.title('предупреждение')

        s_rect = '0123456789.-'

        mensage = '
параметры неправильные, должно 
быть исправлено следующее:
'

        if rect_alfa == '':
            mensage += f'   α° является пустым.\n'
        else:
            if '-' in rect_alfa:
                if rect_alfa.count('-') > 1 or rect_alfa[0] != '-':
                    mensage += f'   в α° неправильно использован знак минус(-)\n'
            if '.' in rect_alfa:
                if rect_alfa.count('.') > 1:
                    mensage += f'   в α° использовано больше одной точки(.)\n'
            for i in rect_alfa:
                if i not in s_rect:
                    mensage += f'   в α° использован недопустимый символ({i})\n'
                    break
        
        if rect_beta == '':
            mensage += f'   β° является пустым.\n'
        else:
            if '-' in rect_beta:
                if rect_beta.count('-') > 1 or rect_beta[0] != '-':
                    mensage += f'   el simbolo - en β° no es correcto\n'
            if '.' in rect_beta:
                if rect_beta.count('.') > 1:
                    mensage += f'   el simbolo . en β° no es correcto\n'
            for i in rect_beta:
                if i not in s_rect:
                    mensage += f'    hay simbolos extra;os en beta\n'
                    break
        
        if rect_f == '':
            mensage += f'   F является пустым.\n'
        else:
            if '-' in rect_f:
                if rect_f.count('-') > 1 or rect_f[0] != '-':
                    mensage += f'   el simbolo - en F no es correcto\n'
            if '.' in rect_f:
                if rect_f.count('.') > 1:
                    mensage += f'   el simbolo . en F no es correcto\n'
            for i in rect_f:
                if i not in s_rect:
                    mensage += f'    hay simbolos extra;os en F\n'
                    break

        if rectify(rect_alfa) and rectify(rect_beta):
            if not 0 < alfa < 180:
                mensage += f'    0 < α° < 90°.\n'

            if alfa == 90:
                if not 0 < beta < 90:
                    mensage += f'   0 < β° < 90°.\n'
            else:
                if not 0 < beta < alfa:
                    mensage += f'   0 < β° < α°\n'

        if rectify(rect_f):
            if force_f < 0:
                mensage += f'   F > 0\n'
            
        mensage += 'пожалуйста, введите параметры снова.'

        tkm.showwarning(message=mensage,title='предупреждение', font='calibri 13')

        self.label = tk.Label(self, text=mensage, font='calibri 13')
        self.label.pack()

        self.button = tk.Button(self, text='закрыть', command=self.destroy, font='calibri 13')
        self.button.pack()
'''