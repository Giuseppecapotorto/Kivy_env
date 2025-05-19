
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

class GymApp(MDApp):
    users = ListProperty([])

    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def save_user(self):
        name = self.root.ids.name_field.text
        surname = self.root.ids.surname_field.text
        phone = self.root.ids.phone_field.text

        if name and surname and phone:
            user_info = f"{name} {surname} - {phone}"
            print(f"Salvo utente: {user_info}")  # Debug
            self.users.append(user_info)
            self.update_user_list()
            self.clear_fields()
        else:
            print("Compila tutti i campi!")

    def update_user_list(self):
        user_list = self.root.ids.user_list
        user_list.clear_widgets()

        for user in self.users:
            user_row = MDBoxLayout(orientation="horizontal", spacing="10dp", size_hint_y=None, height="50dp")


            user_item = OneLineListItem(text=user)

            delete_button = MDRaisedButton(text="❌ Cancella", size_hint_x=None, width=120)
            delete_button.bind(on_release=lambda instance, u=user: self.delete_user(u))

            user_row.add_widget(user_item)
            user_row.add_widget(delete_button)

            user_list.add_widget(user_row)

    def delete_user(self, user):
        if user in self.users:
            self.users.remove(user)
            self.update_user_list()

    def clear_fields(self):
        self.root.ids.name_field.text = ""
        self.root.ids.surname_field.text = ""
        self.root.ids.phone_field.text = ""

GymApp().run()
