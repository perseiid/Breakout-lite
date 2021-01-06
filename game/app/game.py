import time
from .objects import *
from .settings import *

class Game():
    def __init__(self, tk, canvas):
        self.tk = tk
        self.canvas = canvas
        self.end_text_size = SIZE_END_TEXT
        self.end_text_color = COLOR_END_TEXT
        self.info_end_score_color = COLOR_END_SCORE
        self.score = Score(canvas, COLOR_SCORE, SIZE_SCORE)
        self.paddle = Paddle(canvas, COLOR_PADDLE, WIDTH_PUDDLE, HEIGHT_PUDDLE, self.score)
        self.ball = Ball(canvas, self.paddle, self.score, COLOR_BALL,SIZE_BALL)

        self.game_started = False

        # Buttons
        self.canvas.bind_all('<KeyPress-Right>', self.paddle.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.paddle.turn_left)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def start_game(self, event):
        self.game_started = True

    # main
    def run(self):
        while not self.ball.hit_bottom:
            if self.game_started:
                self.ball.draw()
                self.paddle.draw()
            self.__update_ui()

        canvas_width = self.canvas.winfo_width()
        self.info_end_score = f'Ваш счёт = {self.score.score}'
        self.canvas.create_text(canvas_width / 2, 120, text='Game over :(', font=('Ubuntu', self.end_text_size), fill=self.end_text_color)
        self.canvas.create_text(canvas_width / 2, 180, text=self.info_end_score, font=('Ubuntu', 20), fill=self.info_end_score_color)
        self.__update_ui()
        time.sleep(3)

    def __update_ui(self):
        self.tk.update_idletasks()
        self.tk.update()
        time.sleep(0.01)