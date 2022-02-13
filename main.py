from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, StringProperty, ObjectProperty, BooleanProperty
import certifi
import os

from connect import *

os.environ['SSL_CERT_FILE'] = certifi.where()
user = {'username': '', 'pass': '', 'host': ''}
pos = None


class MainMenu(Screen):

    def to_shops(self):
        sm.get_screen('shops').refresh()
        sm.current = 'shops'

    def to_products(self):
        sm.get_screen('products').refresh()
        sm.current = 'products'


class ProductScreen(Screen):
    rv_layout = ObjectProperty(None)
    query = ObjectProperty(None)
    selection = ObjectProperty(None)

    def refresh(self):
        products = get_products(user, pos, self.selection.text, self.query.text)
        self.rv.data = [{'text': str(x.get('name')) + ' ' + str(x.get('price')) + ' PLN', 'id': str(x.get('id'))} for x
                        in products]

    def __init__(self, **kw):
        super().__init__(**kw)
        self.refresh()


class MessageBox(Popup):

    def check_quantity(self):
        product = sm.get_screen('products').rv.rv_layout.info[0]
        if pos is None:
            return 'Dostępna ilość: wybierz oddzial'
        else:
            return 'Dostępna ilość: {}'.format(get_quantity(pos, product, user))

    def popup_dismiss(self):
        self.dismiss()


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    """ Adds selection and focus behaviour to the view. """
    info = ObjectProperty(None)
    pos = ObjectProperty(None)


class SelectableLabel(RecycleDataViewBehavior, Label):
    """ Add selection support to the Label """
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        """ Add selection on touch down """
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        """ Respond to the selection of items in the view. """
        global pos
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
            pos = self.id
            print(pos)
        else:
            print("selection removed for {0}".format(rv.data[index]))
            pos = None


class SelectableButton(RecycleDataViewBehavior, Button):
    """ Add selection support to the Label """
    index = None

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_press(self):
        self.parent.info = get_info(self.id, user)

    def on_release(self):
        MessageBox().open()


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    host = ObjectProperty(None)
    prompt = ObjectProperty(None)

    def connect(self):
        try:
            global user
            user['username'] = self.username.text
            user['pass'] = self.password.text
            user['host'] = self.host.text
            con = connect(user)
            print('Good login')
        except:
            self.prompt.text = "Connection to database error"
        sm.add_widget(ShopsScreen(name='shops'))
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(ProductScreen(name='products'))
        con.close()
        sm.current = 'menu'


class ShopsScreen(Screen):
    data_items = ListProperty([])
    list = ObjectProperty(None)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.refresh()

    def refresh(self):
        rows = get_shops(user)
        self.rv.data = rows


kv = Builder.load_file("my.kv")
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.current = 'login'


class MainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MainApp().run()
