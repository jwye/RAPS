#
#http://pydoing.blogspot.tw/2015/06/python-v100-7-python.html

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Demo(BoxLayout):
	def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        self.count=0
        self.orientation='vertical'

        s1='Click Me!'
        self.click=Button(text=s1)
        self.click.on_press=self.do_something
	    self.add_widget(self.click)

	    s2='Something happened...'
	    self.display=Label(text=s2)
	    self.add_widget(self.display)

    def do_something(self):
        s1='You have clicked the button.'
        s2='Click Me Again!'
	    s3='Something happened...'
	    s4='Click Me!'
	    if self.count % 2 == 0:
	        self.display.text=s1
	        self.click.text=s2
	    else:
	        self.display.text=s3
	        self.click.text=s4
	        self.count+=1

class DemoApp(App):
    def build(self):
    return Demo()

if __name__ == '__main__':
    DemoApp().run()
