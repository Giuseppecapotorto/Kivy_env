from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#F8BBD0"  # Light Pink
    text_color: "#880E4F"  # Darker Pink for contrast
    icon_color: "#880E4F"
    ripple_color: "#F48FB1"
    selected_color: "#AD1457"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#880E4F"
    icon_color: "#880E4F"
    focus_behavior: False
    selected_color: "#880E4F"
    _no_ripple_effect: True

MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "Palestra App"
        md_bg_color: "#F8BBD0"
        specific_text_color: "#880E4F"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr_schede"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "10dp"
                    spacing: "10dp"

                    MDLabel:
                        text: "Schede"
                        halign: "center"

                    ScrollView:
                        MDList:
                            id: user_list

            MDScreen:
                name: "scr_workouts"
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"
                    padding: "10dp"

                    MDLabel:
                        text: "Workouts"
                        halign: "center"
                        font_style: "H4"

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: "Allenamento Cardio"
                                on_press: screen_manager.current = "scr_cardio"
                                IconLeftWidget:
                                    icon: "heart-pulse"

                            OneLineIconListItem:
                                text: "Allenamento Braccia"
                                on_press: screen_manager.current = "scr_braccia"
                                IconLeftWidget:
                                    icon: "dumbbell"

                            OneLineIconListItem:
                                text: "Allenamento Gambe"
                                on_press: screen_manager.current = "scr_gambe"
                                IconLeftWidget:
                                    icon: "run-fast"

                            OneLineIconListItem:
                                text: "Allenamento Dorso"
                                on_press: screen_manager.current = "scr_dorso"
                                IconLeftWidget:
                                    icon: "weight-lifter"

                            OneLineIconListItem:
                                text: "Allenamento Petto"
                                on_press: screen_manager.current = "scr_petto"
                                IconLeftWidget:
                                    icon: "arm-flex-outline"

                            OneLineIconListItem:
                                text: "Allenamento Addome"
                                on_press: screen_manager.current = "scr_addome"
                                IconLeftWidget:
                                    icon: "ab-testing"

            MDScreen:
                name: "scr_users"
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "10dp"
                    spacing: "10dp"

                    MDLabel:
                        text: "User "
                        halign: "center"

                    MDTextField:
                        id: name_field
                        hint_text: "Nome"
                        mode: "rectangle"

                    MDTextField:
                        id: surname_field
                        hint_text: "Cognome"
                        mode: "rectangle"

                    MDTextField:
                        id: phone_field
                        hint_text: "Numero di telefono"
                        mode: "rectangle"

                    MDRaisedButton:
                        text: "Salva"
                        on_press: app.save_user()

            MDScreen:
                name: "scr_settings"
                MDLabel:
                    text: "Setting"
                    halign: "center"

            # Schermate specifiche per ogni tipo di allenamento
            MDScreen:
                name: "scr_cardio"
                MDLabel:
                    text: "Allenamento Cardio"
                    halign: "center"

            MDScreen:
                name: "scr_braccia"
                MDLabel:
                    text: "Allenamento Braccia"
                    halign: "center"

            MDScreen:
                name: "scr_gambe"
                MDLabel:
                    text: "Allenamento Gambe"
                    halign: "center"

            MDScreen:
                name: "scr_dorso"
                MDLabel:
                    text: "Allenamento Dorso"
                    halign: "center"

            MDScreen:
                name: "scr_petto"
                MDLabel:
                    text: "Allenamento Petto"
                    halign: "center"

            MDScreen:
                name: "scr_addome"
                MDLabel:
                    text: "Allenamento Addome"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Home"
                    title_color: "#880E4F"
                    text: "Lara"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Gestione"

                DrawerClickableItem:
                    icon: "alien"
                    text: "Schede allenamento"
                    on_press:
                        nav_drawer.set_state("close")
                        screen_manager.current = "scr_schede"

                DrawerClickableItem:
                    icon: "dumbbell"
                    text: "Workouts"
                    on_press: 
                        nav_drawer.set_state("close")
                        screen_manager.current = "scr_workouts"

                DrawerClickableItem:
                    icon: "account-group"
                    text: "User "
                    on_press:
                        nav_drawer.set_state("close")
                        screen_manager.current = "scr_users"

                DrawerClickableItem:
                    icon: "cog"
                    text: "Setting"
                    on_press:
                        nav_drawer.set_state("close")
                        screen_manager.current = "scr_settings"
'''

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

