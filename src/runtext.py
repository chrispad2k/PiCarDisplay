import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib')))

import pyximport
pyximport.install()

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time


class RunText():
    def __init__(self, *args, **kwargs):
        options = RGBMatrixOptions()

        options.hardware_mapping = "adafruit-hat"
        options.rows = 32
        options.cols = 64

        self.matrix = RGBMatrix(options = options)

        try:
            print("Press CTRL-C to stop sample")
            self.run()
        except KeyboardInterrupt:
            print("Exiting\n")
            sys.exit(0)

        return True

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/10x20.bdf")
        textColorR = graphics.Color(255, 0, 0)
        textColorG = graphics.Color(0, 255, 0)
        textColorB = graphics.Color(0, 0, 255)
        pos = offscreen_canvas.width
        my_text = "Hallo Tante Dorli! :-)"

        counter = 0
        while True:
            offscreen_canvas.Clear()

            if counter % 60 < 20:
                textColor = textColorR
            elif counter % 60 < 40:
                textColor = textColorG
            elif counter % 60 < 60:
                textColor = textColorB

            counter += 1

            len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.03)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
