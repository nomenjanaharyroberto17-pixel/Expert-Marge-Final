from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Fandokoana ny écran (Dark Mode)
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class ExpertVirtuelPro(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Titre
        self.layout.add_widget(Label(text="EXPERT VIRTUEL PRO", font_size=28, color=(0, 1, 0, 1), bold=True))

        # Fizarana Aviator
        self.layout.add_widget(Label(text="--- AVIATOR PREDICTOR ---", color=(0.2, 0.6, 1, 1)))
        self.aviator_input = TextInput(multiline=False, hint_text="Multipliers (ohatra: 1.25, 3.40, 1.08)", background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))
        self.layout.add_widget(self.aviator_input)

        # Fizarana Foot Virtuel
        self.layout.add_widget(Label(text="--- FOOT VIRTUEL (Scores) ---", color=(0.2, 0.6, 1, 1)))
        self.foot_input = TextInput(multiline=False, hint_text="Scores farany (ohatra: 2-1, 0-0, 1-2)", background_color=(0.1, 0.1, 0.1, 1), foreground_color=(1, 1, 1, 1))
        self.layout.add_widget(self.foot_input)

        # Bokotra Kajio
        btn = Button(text="KAJIO NY ALGORITHME", background_color=(0, 0.7, 0, 1), font_size=20, bold=True)
        btn.bind(on_press=self.analyse_globale)
        self.layout.add_widget(btn)

        # Valiny
        self.resultat = Label(text="Ampidiro ny isa dia tsindrio 'Kajio'", font_size=18, halign="center")
        self.layout.add_widget(self.resultat)
        
        return self.layout

    def analyse_globale(self, instance):
        try:
            # Logic Aviator tsotra
            m_data = [float(x) for x in self.aviator_input.text.split(',')]
            pred_av = round((sum(m_data)/len(m_data)) * 1.12, 2)
            
            # Logic Foot tsotra
            res_val = f"Aviator: x{pred_av}\nFoot: Mety ho Over 1.5"
            self.resultat.text = res_val
        except:
            self.resultat.text = "Hamarino tsara ny isa nampidirinao"

ExpertVirtuelPro().run()


  
