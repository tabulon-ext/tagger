from kivy.app import App
from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from PrevNext import NextPrevBar
import SimulateOutside
from kivy.uix.image import Image
import os

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.picture = Image(allow_stretch=True)

        SimulateOutside.makeActiveFile(SimulateOutside.g_picFile)
        print("filename:", SimulateOutside.g_picFile)
        print("path:", SimulateOutside.g_path)
        print("prev:", SimulateOutside.g_prevFile)
        print("next:", SimulateOutside.g_nextFile)
        print("exists:", os.path.isfile(SimulateOutside.g_path + SimulateOutside.g_picFile))
        self.picture.source = SimulateOutside.g_path+SimulateOutside.g_picFile

        Clock.schedule_once(lambda dt: self.add_widget(self.picture), timeout=0.1)
        self.navigationButtons = NextPrevBar()
        Clock.schedule_once(lambda dt: self.add_widget(self.navigationButtons), timeout=0.1)
        self.prevButton = self.navigationButtons.children[1]
        self.nextButton = self.navigationButtons.children[0]
        self.prevButton.bind(on_release=self.goToPrevImage)
        self.nextButton.bind(on_release=self.goToNextImage)

    def goToPrevImage(self, arg):
        if SimulateOutside.getNext() != '':
            SimulateOutside.makeActiveFile(SimulateOutside.getPrev())
            self.picture.source = SimulateOutside.g_path + SimulateOutside.g_picFile

    def goToNextImage(self, arg):
        if SimulateOutside.getNext() != '':
            SimulateOutside.makeActiveFile(SimulateOutside.getNext())
            self.picture.source = SimulateOutside.g_path + SimulateOutside.g_picFile


class Nested2App(App):
    def build(self):
        return ContainerBox()

if __name__ == '__main__':
    Nested2App().run()