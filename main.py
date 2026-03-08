from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MargeExpertApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.layout.add_widget(Label(text="Expert Marge V1", font_size='24sp'))
        
        self.c1 = TextInput(hint_text="Cote 1", input_filter='float', multiline=False)
        self.cn = TextInput(hint_text="Cote N", input_filter='float', multiline=False)
        self.c2 = TextInput(hint_text="Cote 2", input_filter='float', multiline=False)
        
        self.layout.add_widget(self.c1)
        self.layout.add_widget(self.cn)
        self.layout.add_widget(self.c2)
        
        btn = Button(text="Kajio", background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.process)
        self.layout.add_widget(btn)
        
        self.resultat = Label(text="Marge: -- %")
        self.layout.add_widget(self.resultat)
        return self.layout

    def process(self, instance):
        try:
            v1 = float(self.c1.text)
            vn = float(self.cn.text)
            v2 = float(self.c2.text)
            # Ny fomba fikajiana ny marge
            m = (1 - (1/v1 + 1/vn + 1/v2)) * 100
            self.resultat.text = f"Marge: {round(m, 2)} %"
        except:
            self.resultat.text = "Hamarino ny isa nampidirinao"

if __name__ == "__main__":
    MargeExpertApp().run()
  
