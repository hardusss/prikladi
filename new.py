import flet as ft
import random



sqrt = '**0.5'
diya = ['+', '-', '*', '/', sqrt]
equation = []
eq = ''
res = ''
def main(page: ft.Page):

   page.window_resizable = False
   page.bgcolor = 'indigo300'
   page.window_width = 450
   page.window_height = 350
   t = ft.Text('Enter result', size=30, font_family='SimSun')
   page.update()

   def lvl1(e):
       global random_length , eq, res
       page.clean()
       random_length = random.randint(2, 4)
       x = 0
       while x != random_length:
           x += 1
           random_num = random.randint(1, 200)
           random_diya = random.choice(diya)
           random_num = str(random_num)
           equation.append(random_num)
           equation.append(random_diya)
       for i in equation:
           eq += str(i)
       if eq.endswith('-') or eq.endswith('+') or eq.endswith('*') or eq.endswith('/'):
           res = eq[:-1]
       eq_text = ft.Text(value=res, size=33)
       inputResult = ft.TextField(label='Enter result', border_color='white')
       page.add(ft.Row([
           eq_text

       ], alignment=ft.MainAxisAlignment.CENTER
       ))
       def result(e):
           global res
           if inputResult.value == eval(res):
               inputResult.border_color = 'green'
           else:
               inputResult.border_color = 'red'
           page.update()

       page.add(ft.Row([
           inputResult,
           ft.ElevatedButton(text='Done', bgcolor='white', color='indigo400', width=105, height=50, on_click=result)
       ]))

       page.update()
   page.add(ft.Row([


   ]))
   page.add(ft.Row([
       ft.ElevatedButton('Level Easy',on_click = lvl1, width=150, height=45, color='green300', bgcolor='grey900')
   ]))
   page.add(ft.Row([
       ft.ElevatedButton('Level Normal', width=150, height=45, color='yellow200', bgcolor='grey900')
   ]))
   page.add(ft.Row([
       ft.ElevatedButton('Level Hard', width=150, height=45, color='red300', bgcolor='grey900')
   ]))


   page.add(ft.Row([
       t
   ]))


if __name__ == '__main__':
   ft.app(target=main)
