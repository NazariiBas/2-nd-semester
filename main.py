from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.switch import Switch
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner

class MainPage(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        btn1 = Button(text='Button 1')
        btn1.bind(on_press=self.next1)
        btn2 = Button(text='Button 2')
        btn2.bind(on_press=self.next2)
        btn3 = Button(text='Button 3')
        btn3.bind(on_press=self.next3)
        btn4 = Button(text='Button 4')
        btn4.bind(on_press=self.next4)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        self.add_widget(layout)

    def next1(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "second"

    def next2(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "third"

    def next3(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "fourth"

    def next4(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "fifth"


class SecondScreen(Screen):
    def __init__(self, name="second"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Main Page')
        btn1.bind(on_press=self.next1)
        btn1.size_hint = (None, None)  
        btn1.size = (150, 50)  
        btn1.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        checkbox = CheckBox()
        checkbox.bind(active=self.on_checkbox_active)
        checkbox.size_hint = (None, None)
        checkbox.size = (100, 100)
        checkbox.pos_hint = {'x': 0, 'center_y': 0.5}

        slider = Slider(min=-100, max=100, value=25)
        slider.bind(value=self.on_slider_value_change)
        slider.size_hint = (None, None)
        slider.size = (200, 50)
        slider.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        layout.add_widget(btn1)
        layout.add_widget(checkbox)
        layout.add_widget(slider)
        self.add_widget(layout)

    def next1(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "first"

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

    def on_slider_value_change(self, instance, value):
        print('Slider value changed:', value)


class ThirdScreen(Screen):
    def __init__(self, name="third"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Main Page')
        btn1.bind(on_press=self.next1)

        pb = ProgressBar(max=1000)
        pb.value = 750

        def on_enter(self, instance):
            print('User pressed enter in', instance.text)

        textinput = TextInput(text='Hello world', multiline=False)
        textinput.bind(on_text_validate=self.on_enter)

        layout.add_widget(btn1)
        layout.add_widget(pb)
        layout.add_widget(textinput)

        self.add_widget(layout)



    def next1(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "first"


class FourthScreen(Screen):
    def __init__(self, name="fourth"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Main Page')
        btn1.bind(on_press=self.next1)

        def callback(instance, value):
            print('the switch', instance, 'is', value)

        switch = Switch()
        switch.bind(active=callback)

        dropdown = DropDown()
        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text='Hello', size_hint=(None, None))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
       


        layout.add_widget(btn1)
        layout.add_widget(switch)
        layout.add_widget(mainbutton)
        self.add_widget(layout)

    def next1(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "first"


class FifthScreen(Screen):
    def __init__(self, name="fifth"):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Main Page')
        btn1.bind(on_press=self.next1)

        spinner = Spinner(
            text='Home',
            values=('Home', 'Work', 'Other', 'Custom'),
            size_hint=(None, None),
            size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .5})

        def show_selected_value(spinner, text):
            print('The spinner', spinner, 'has text', text)

        spinner.bind(text=show_selected_value)

        l = Label(text='Hello world', font_size='20sp')

        layout.add_widget(btn1)
        layout.add_widget(spinner)
        layout.add_widget(l)
        self.add_widget(layout)

    def next1(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "first"



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage())
        sm.add_widget(SecondScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(FourthScreen())
        sm.add_widget(FifthScreen())
        return sm


MyApp().run()
