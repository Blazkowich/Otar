import pyqrcode
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class QrGen(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.user = None
        self.button = None
        self.greeting = None
        self.window = None
        self.image = Image(source="#WriteYourFileNameAndPath",
                           allow_stretch=True,
                           keep_ratio=True)

    def build(self):
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(self.image)

        # label widget
        self.greeting = Label(
            text="Input Link Bellow",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(0.5, 0.5)
        )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
            text="Press For Processing",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#00FFCE'
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, url):
        self.greeting.text = self.user.text

        # Generate QR code
        url = pyqrcode.create(self.greeting.text)

        # Create and save the file
        url.svg("QrGen.svg", scale=8)


# run Say Hello App Call
if __name__ == "__main__":
    QrGen().run()
