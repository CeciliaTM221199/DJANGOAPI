import pytest
from django.test import TestCase
from api.models import *


class RegistroUTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo y realiza pruebas
        instancia = RegistroU(
            nombre="Nombre",
            apellidop="ApellidoP",
            apellidom="ApellidoM",
            email="correo@example.com",
            contra="contrasena123"
        )
        self.assertEqual(instancia.nombre, "Nombre")
        self.assertEqual(instancia.apellidop, "ApellidoP")
        self.assertEqual(instancia.apellidom, "ApellidoM")
        self.assertEqual(instancia.email, "correo@example.com")
        self.assertEqual(instancia.contra, "contrasena123")

class EncuestaTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo y realiza pruebas
        instancia = Encuesta(
            gama="Gama1",
            frecuencia="Frecuente",
            met_pago="Tarjeta",
            dispositivo="Dispositivo1",
            opc_correo="Si",
            serv_mensajeria="WhatsApp",
            opc_chatbot="No",
            opc_atencion_pers="Si",
            tiempo_nave="Rápido"
        )
        self.assertEqual(instancia.gama, "Gama1")
        self.assertEqual(instancia.frecuencia, "Frecuente")
        self.assertEqual(instancia.met_pago, "Tarjeta")
        self.assertEqual(instancia.dispositivo, "Dispositivo1")
        self.assertEqual(instancia.opc_correo, "Si")
        self.assertEqual(instancia.serv_mensajeria, "WhatsApp")
        self.assertEqual(instancia.opc_chatbot, "No")
        self.assertEqual(instancia.opc_atencion_pers, "Si")
        self.assertEqual(instancia.tiempo_nave, "Rápido")

class ProductTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo y realiza pruebas
        instancia = Product(
            name="Producto1",
            price="Precio1"
        )
        self.assertEqual(instancia.name, "Producto1")
        self.assertEqual(instancia.price, "Precio1")


