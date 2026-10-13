from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle

# ထောင့်ဝိုင်းနေသော ခလုတ်အသစ် (Rounded Button) ဖန်တီးခြင်း
class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        
        with self.canvas.before:
            self.bg_color = Color(0.12, 0.47, 0.95, 1) 
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[15])
            
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class VideoPlayerApp(MDApp):
    def build(self):
        # အမှောင်စတိုင် (Dark Theme) နှင့် အရောင်သတ်မှတ်ခြင်း
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"

        # ပင်မ Screen ဖန်တီးခြင်း
        screen = MDScreen()

        # အပြင်အဆင် Layout (ဒေါင်လိုက်စီရန်)
        layout = MDBoxLayout(orientation='vertical')

        # ထိပ်ဆုံးက ခေါင်းစဉ် (Top Title)
        title_box = MDBoxLayout(size_hint_y=None, height="56dp", padding=16)
        title_label = MDLabel(
            text="My KivyMD Video Player",
            halign="center",
            theme_text_color="Primary",
        )
        title_box.add_widget(title_label)
        layout.add_widget(title_box)

        # Video Player ထည့်သွင်းခြင်း (မူလက Online ဗီဒီယိုကို ယာယီထည့်ထားသည်)
        self.player = VideoPlayer(
            source='',
            state='stop',
            options={'eos': 'loop'}
        )
        layout.add_widget(self.player)

        # ထိန်းချုပ်ရန် ခလုတ်များ ထည့်သွင်းမည့် Layout (ဘေးတိုက်စီရန်)
        btn_layout = MDBoxLayout(
            size_hint_y=None, 
            height="70dp", 
            padding=10, 
            spacing=10
        )
        
        # ဖိုင်ရွေးရန် ခလုတ်နှင့် Play, Pause, Stop ခလုတ်များ
        file_btn = RoundedButton(text="Open File", on_release=self.open_file_chooser)
        play_btn = RoundedButton(text="Play", on_release=self.play_video)
        pause_btn = RoundedButton(text="Pause", on_release=self.pause_video)
        stop_btn = RoundedButton(text="Stop", on_release=self.stop_video)

        btn_layout.add_widget(file_btn)
        btn_layout.add_widget(play_btn)
        btn_layout.add_widget(pause_btn)
        btn_layout.add_widget(stop_btn)
        
        layout.add_widget(btn_layout)
        screen.add_widget(layout)
        return screen

    # ဖိုင်ရွေးချယ်ရန် Popup ဖွင့်ပေးသည့် လုပ်ဆောင်ချက်
    def open_file_chooser(self, instance):
        content = MDBoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # ဗီဒီယိုဖိုင်များကိုသာ ရှာဖွေရန် Filter ထည့်ထားခြင်း (.mp4, .mkv, .avi)
        filechooser = FileChooserIconView(
            filters=['*.mp4', '*.mkv', '*.avi', '*.mov'],
            path='/home/' # လိုအပ်ပါက မိမိစက်ထဲက လမ်းကြောင်းကို ပြောင်းနိုင်သည်
        )
        content.add_widget(filechooser)

        # ရွေးချယ်ရန်နှင့် ပိတ်ရန် ခလုတ်များအတွက် Layout
        select_layout = MDBoxLayout(size_hint_y=None, height="50dp", spacing=10)
        select_btn = RoundedButton(text="Select", on_release=lambda x: self.load_video(filechooser.selection, popup))
        cancel_btn = RoundedButton(text="Cancel", on_release=lambda x: popup.dismiss())
        
        select_layout.add_widget(select_btn)
        select_layout.add_widget(cancel_btn)
        content.add_widget(select_layout)

        # Popup ဖြင့် ပြသခြင်း
        popup = Popup(title="Select Video File", content=content, size_hint=(0.9, 0.9))
        popup.open()

    # ရွေးချယ်လိုက်သော ဗီဒီယိုဖိုင်ကို ပလေယာထဲသို့ ထည့်သွင်းခြင်း
    def load_video(self, selection, popup):
        if selection:
            self.player.source = selection[0]
            self.player.state = 'play'
            popup.dismiss()

    def play_video(self, instance):
        if self.player.source:
            self.player.state = 'play'

    def pause_video(self, instance):
        self.player.state = 'pause'

    def stop_video(self, instance):
        self.player.state = 'stop'

if __name__ == '__main__':
    VideoPlayerApp().run()
