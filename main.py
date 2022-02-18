from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import (Color,Line,Ellipse)
from random import random
from kivy.uix.widget import Widget

#Config.set("graphics","resizable","0")
#Config.set("graphics","width","640")
#Config.set("graphics","height","480")



class PainterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(),random(),random(),1)
            rad = 30
            Ellipse(pos = (touch.x - rad/2,touch.y- rad/2),size = (rad,rad))
            touch.ud["line"] = Line(points = (touch.x,touch.y),width = 15)


    def on_touch_move(self, touch):
        touch.ud["line"].points += (touch.x,touch.y)

class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text = "Clear",on_press = self.clear_canvas,size = (100,50)))
        parent.add_widget(Button(text="Save", on_press=self.save, size=(100, 50),pos = (0,50)))
        parent.add_widget(Button(text="Screen", on_press=self.screen, size=(100, 50), pos=(0, 100)))
        return parent
    def clear_canvas(self,instance):
        self.painter.canvas.clear()

    def save (self,instance):
        self.painter.size = (Window.size[0],Window.size[1])
        self.painter.export_to_png("image.png")
    def screen (self,instance):
        Window.screenshot("screen.png")






#def build(self):
        #bl = BoxLayout(orientation = "vertical",padding = [160,120],spacing = 12)
        #bl.add_widget(Button(text="Малювати",font_size = 20,on_press = self.play,background_color = [.10,1,.19,1],background_normal = ""))
        #bl.add_widget(Button(text="Рекорди",font_size = 20,on_press = self.record,background_color = [.10,1,.19,1],background_normal = ""))
        #bl.add_widget(Button(text="Інші ігри",font_size = 20,on_press = self.game,background_color = [.10,1,.19,1],background_normal = ""))
        #bl.add_widget(Button(text="Зворотній зв'язок",font_size = 20,on_press = self.we,background_color = [.10,1,.19,1],background_normal = ""))
        #return bl

if __name__ == "__main__":
    PaintApp().run()
