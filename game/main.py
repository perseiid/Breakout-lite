from tkinter import *
from PIL import Image, ImageTk
import time
import random

# Импортим свои настройки
from app.game import *
from app.objects import *
from app.settings import *
 
# Создаем обьект tkinter
tk = Tk()

# Название приложения
tk.title(GAME_NAME)
# Задаем неизменяемые размеры чтоюы пользователь не изменял размеры
tk.resizable(0,0)
# Поверх всех окон
tk.wm_attributes('-topmost', 1)

# Создаем холст поле игры окно
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0)
# Добавление фона 
bg = ImageTk.PhotoImage(Image.open('app/bg.jpg').resize((WIDTH, HEIGHT)))
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)

# Показываем что все имеет координаты
canvas.pack()
# Обновление для обрисовки
tk.update()

game = Game(tk, canvas)
# Запуск игры
game.run()
