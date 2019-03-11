import numpy as np
import datetime
import time
import cv2
import os
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

cap = cv2.VideoCapture(0)

tfPeso = TextInput(multiline=False)
peso = ""
floatpeso = 0
def on_text(instance, value):
    print("The widget", instance, "Have: ", value)
def calcular_peso():
    datovalido2 = False
    i = 0
    peso = str(input("Peso: "))
    while datovalido2 == False:
        try:
            peso = peso.replace(",", ".")
            peso = peso.replace(".", "")
            peso = peso.replace("=", "")
            peso = float(peso)
            print(peso)
            if peso != 0:
                datovalido2 = True
        except ValueError as valerr:
            print("Peso no ha sido reconocido como float o es igual a 0.")
            print(peso)
            print(type(peso))
            print(valerr)
            peso = str(input("Peso:"))

    if peso != 0:
        listapesos = []
        for i in range(0, 10):
            inputpeso = input("Peso de la comida: ")
            try:
                inputpeso = inputpeso.replace(",", ".")
                inputpeso = inputpeso.replace("=", "")
                inputpeso = inputpeso[2:]
                inputpeso = float(inputpeso)
                listapesos.append(inputpeso)
            except:
                i -= 1

        floatpeso = float(max(set(listapesos), key=listapesos.count))
        tfPeso.bind(text=on_text)
        print("El peso de la comida es de %.3f kg" % floatpeso)
        try:
            fichero = open("/home/pi/kitchen_app/pesos.log", "a")
            fichero.write("Peso: %.3f medido el " % floatpeso)
            fichero.write("%s" % (datetime.datetime.now()))
            fichero.write("\n")
            fichero.close()
        except:
            print("Ruta de fichero log no encontrada")
        #  cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        print(ret)
        # cv2.imwrite(("C:/Users/Usuario/Desktop/pyCharm/%s.jpg" % (datetime.datetime.now())),frame)
        hora = time.time()
        try:
            cv2.imwrite(("/home/pi/kitchen_app/fotos/%s.jpg" % (hora)), frame)
        except:
            print("Se ha creado la imagen igualmente")
        # cv2.imshow("epppp.jpg", frame)
        # cv2.imwrite("C:/Users/Usuario/Desktop/pyCharm/pycharm.jpg", frame)
        try:
            fichero = open("/home/pi/kitchen_app/pesos.log", "a")
            fichero.write("Ruta absoluta de la imagen: %s\n\n" % (os.path.abspath(("%s.jpg" % (hora)))))
            fichero.close()
        except:
            print("Ruta de fichero log no encontrada")

        # cv2.waitKey()
        cv2.destroyAllWindows()

def callback(instance):
    calcular_peso()
class MyGrid(GridLayout):
    def __init__(self, **kwargs): #**kwargs significa argumentos infinitos
        super(MyGrid, self).__init__(**kwargs) #heredamos GridLayout lo primero de todo
        self.cols = 2
        self.rows = 4
        self.add_widget(Label(text="Nombre: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Fecha: "))
        self.date = TextInput(multiline=False)
        self.add_widget(self.date)
        self.add_widget(Label(text="Ruta de la imagen: "))
        self.ruta = TextInput(multiline=False)
        self.add_widget(self.ruta)
        boton = Button(text="Calcular peso")
        boton.bind(on_press=callback)
        self.add_widget(boton)
        self.add_widget(tfPeso)

class myApp(App):
    def build(self):
        return MyGrid()

if __name__== "__main__":
    myApp().run()

