import flet as ft

calc = ''


def main(page: ft.Page):
    page.title = 'Сalculator'
    page.window_width = 300
    page.window_height = 330
    t = ft.TextField(value='', color='white', width=266, border_color='DEEPPURPLE600', text_align=ft.TextAlign.RIGHT)
    page.add(t)


    def krapka(e):
        global calc
        calc += '.'
        t.value = calc
        page.update()


    def clear(e):
        t.value = ''
        page.update()


    def n1(e):
        global calc
        calc += '1'
        t.value += calc
        page.update()


    def n2(e):
        global calc
        calc += '2'
        t.value = calc
        page.update()


    def n3(e):
        global calc
        calc += '3'
        t.value = calc
        page.update()


    def n4(e):
        global calc
        calc += '4'
        t.value = calc
        page.update()


    def n5(e):
        global calc
        calc += '5'
        t.value = calc
        page.update()


    def n6(e):
        global calc
        calc += '6'
        t.value = calc
        page.update()


    def n7(e):
        global calc
        calc += '7'
        t.value = calc
        page.update()


    def n8(e):
        global calc
        calc += '8'
        t.value = calc
        page.update()


    def n9(e):
        global calc
        calc += '9'
        t.value = calc
        page.update()


    def n0(e):
        global calc
        calc += '0'
        t.value = calc
        page.update()


    def plus(e):
        global calc
        calc += '+'
        t.value = calc
        page.update()


    def minus(e):
        global calc
        calc += '-'
        t.value = calc
        page.update()


    def division(e):
        global calc
        calc += '/'
        t.value = calc
        page.update()


    def mult(e):
        global calc
        calc += '*'
        t.value = calc
        page.update()


    def step(e):
        global calc
        calc += '**2'
        t.value += '²'
        page.update()


    def new(e):
        page.window_width = 400
        t.width = 400
        page.update()

    def new2(e):
        page.window_width = 300
        t.width = 266
        page.update()


    def pi(e):
        global calc
        calc += '3.14'
        t.value = calc
        page.update()


    def e(e):
        global calc
        calc += '2.71'
        t.value = calc
        page.update()


    def sqrt(e):
        global calc
        calc += '**0.5'
        t.value = '√'
        page.update()


    def back(e):
        global calc
        if len(calc) > 0:
            calc = calc[:-1]
            t.value = calc
            page.update()

        else:
            print('eror')


    def change_them(e):
        page.theme_mode = 'dark' if page.theme_mode == 'light' else 'light'
        page.update()


    def result(e):
        global calc
        if '/0' in t.value:
            t.value = 'ERROR'
            page.update()
            calc = ''
        else:
            if len(t.value) > 0:
                t.value = round(eval(t.value), 4)
                page.update()
                calc = ''

            if len(calc) > 0:
                calc = eval(calc)
                t.value = round(calc, 4)
                page.update()
                calc = ''


    page.add(ft.Row([
        ft.ElevatedButton('↪️', on_click=new, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('x²', on_click=step, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('C', on_click=clear, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('⬅️', on_click=back, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('↩️', on_click=new2, bgcolor='DEEPPURPLE600', width=90),

    ]))


    page.add(ft.Row([ft.ElevatedButton('1', on_click=n1, bgcolor='INDIGO600'),
                     ft.ElevatedButton('2', on_click=n2, bgcolor='INDIGO600'),
                     ft.ElevatedButton('3', on_click=n3, bgcolor='INDIGO600'),
                     ft.ElevatedButton('+', on_click=plus, bgcolor='DEEPPURPLE600', width=70),
                     ft.ElevatedButton('π', on_click=pi, bgcolor='DEEPPURPLE600', width=90),
                    ]))

    page.add(ft.Row([
                     ft.ElevatedButton('4', on_click=n4, bgcolor='INDIGO600'),
                     ft.ElevatedButton('5', on_click=n5, bgcolor='INDIGO600'),
                     ft.ElevatedButton('6', on_click=n6, bgcolor='INDIGO600'),
                     ft.ElevatedButton('-', on_click=minus, bgcolor='DEEPPURPLE600', width=70),
                     ft.ElevatedButton('e', on_click=e, bgcolor='DEEPPURPLE600', width=90)
                     ]))
    page.add(ft.Row([
                     ft.ElevatedButton('7', on_click=n7, bgcolor='INDIGO600'),
                     ft.ElevatedButton('8', on_click=n8, bgcolor='INDIGO600'),
                     ft.ElevatedButton('9', on_click=n9, bgcolor='INDIGO600'),
                     ft.ElevatedButton('/', on_click=division, bgcolor='DEEPPURPLE600', width=70),
                     ft.ElevatedButton('√', on_click=sqrt, bgcolor='DEEPPURPLE600', width=90),

                ]))

    page.add(ft.Row([
        ft.ElevatedButton('*', on_click=mult, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('0', on_click=n0, bgcolor='INDIGO600'),
        ft.ElevatedButton('.', on_click=krapka, bgcolor='DEEPPURPLE600'),
        ft.ElevatedButton('=', on_click=result, bgcolor='DEEPPURPLE600', width=70),
        ft.IconButton(ft.icons.SUNNY, on_click=change_them, bgcolor='DEEPPURPLE600', width=90),
    ]))


    page.update()
if __name__ == '__main__':
    ft.app(target=main)