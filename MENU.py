# MÓDULO 3 - ESTRUCTURAS DE DATOS I
# Ejercicio 1: Lista de Tareas con Lista Enlazada
# Ejercicio 2: Juego de Solitario con Listas Enlazadas

import random

# ==================== EJERCICIO 1: LISTA DE TAREAS ====================

class NodoTarea:
    """Nodo que representa una tarea en la lista enlazada"""
    def _init_(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad  # 1 = alta, 2 = media, 3 = baja
        self.siguiente = None

class ListaTareas:
    """Lista enlazada para gestionar tareas"""
    def _init_(self):
        self.cabeza = None
    
    def agregar_tarea(self, descripcion, prioridad):
        """Inserta una tarea al final de la lista"""
        nuevo_nodo = NodoTarea(descripcion, prioridad)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Tarea '{descripcion}' agregada con prioridad {prioridad}")
    
    def mostrar_tareas(self):
        """Muestra todas las tareas con su prioridad"""
        if self.cabeza is None:
            print("No hay tareas en la lista")
            return
        
        print("\n=== LISTA DE TAREAS ===")
        actual = self.cabeza
        contador = 1
        while actual:
            prioridad_texto = {1: "Alta", 2: "Media", 3: "Baja"}[actual.prioridad]
            print(f"{contador}. {actual.descripcion} - Prioridad: {prioridad_texto}")
            actual = actual.siguiente
            contador += 1
        print("========================\n")
    
    def eliminar_tarea(self, descripcion):
        """Elimina la primera tarea que coincida con la descripción"""
        if self.cabeza is None:
            print("No hay tareas para eliminar")
            return
        
        # Si es el primer nodo
        if self.cabeza.descripcion == descripcion:
            self.cabeza = self.cabeza.siguiente
            print(f"Tarea '{descripcion}' eliminada")
            return
        
        # Buscar en el resto de la lista
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.descripcion == descripcion:
                actual.siguiente = actual.siguiente.siguiente
                print(f"Tarea '{descripcion}' eliminada")
                return
            actual = actual.siguiente
        
        print(f"Tarea '{descripcion}' no encontrada")
    
    def ordenar_por_prioridad(self):
        """Ordena la lista según la prioridad (de menor a mayor valor)"""
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        
        # Algoritmo de ordenamiento burbuja para lista enlazada
        intercambiado = True
        while intercambiado:
            intercambiado = False
            actual = self.cabeza
            
            while actual.siguiente:
                if actual.prioridad > actual.siguiente.prioridad:
                    # Intercambiar datos
                    actual.descripcion, actual.siguiente.descripcion = actual.siguiente.descripcion, actual.descripcion
                    actual.prioridad, actual.siguiente.prioridad = actual.siguiente.prioridad, actual.prioridad
                    intercambiado = True
                actual = actual.siguiente
        
        print("Tareas ordenadas por prioridad")

def menu_tareas():
    """Menú principal para gestionar tareas"""
    lista = ListaTareas()
    
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Ordenar por prioridad")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            while True:
                try:
                    prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
                    if prioridad in [1, 2, 3]:
                        break
                    else:
                        print("La prioridad debe ser 1, 2 o 3")
                except ValueError:
                    print("Por favor ingrese un número válido")
            lista.agregar_tarea(descripcion, prioridad)
        
        elif opcion == "2":
            lista.mostrar_tareas()
        
        elif opcion == "3":
            descripcion = input("Descripción de la tarea a eliminar: ")
            lista.eliminar_tarea(descripcion)
        
        elif opcion == "4":
            lista.ordenar_por_prioridad()
        
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

# ==================== EJERCICIO 2: JUEGO DE SOLITARIO ====================

class Carta:
    """Representa una carta del mazo"""
    def _init_(self, valor, palo):
        self.valor = valor  # A, 2-10, J, Q, K
        self.palo = palo    # ♠️, ♥️, ♦️, ♣️
        self.boca_arriba = False
        self.siguiente = None
    
    def _str_(self):
        if not self.boca_arriba:
            return "[?]"
        return f"{self.valor}{self.palo}"
    
    def es_roja(self):
        """Retorna True si la carta es roja (corazones o diamantes)"""
        return self.palo in ['♥️', '♦️']
    
    def es_negra(self):
        """Retorna True si la carta es negra (picas o tréboles)"""
        return self.palo in ['♠️', '♣️']
    
    def valor_numerico(self):
        """Retorna el valor numérico de la carta para comparaciones"""
        valores = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        if self.valor in valores:
            return valores[self.valor]
        return int(self.valor)

class PilaCartas:
    """Lista enlazada que representa una pila de cartas"""
    def _init_(self):
        self.tope = None
        self.tamaño = 0
    
    def apilar(self, carta):
        """Agrega una carta al tope de la pila"""
        carta.siguiente = self.tope
        self.tope = carta
        self.tamaño += 1
    
    def desapilar(self):
        """Quita y retorna la carta del tope"""
        if self.tope is None:
            return None
        carta = self.tope
        self.tope = self.tope.siguiente
        carta.siguiente = None
        self.tamaño -= 1
        return carta
    
    def ver_tope(self):
        """Retorna la carta del tope sin quitarla"""
        return self.tope
    
    def esta_vacia(self):
        """Retorna True si la pila está vacía"""
        return self.tope is None
    
    def mover_subpila(self, cantidad):
        """Mueve una cantidad de cartas del tope y las retorna como lista"""
        if cantidad > self.tamaño:
            return None
        
        cartas = []
        for _ in range(cantidad):
            carta = self.desapilar()
            if carta:
                cartas.append(carta)
        
        return cartas
    
    def agregar_subpila(self, cartas):
        """Agrega una lista de cartas a la pila"""
        for carta in reversed(cartas):
            self.apilar(carta)

class JuegoSolitario:
    """Controla el estado del juego de solitario"""
    def _init_(self):
        self.columnas = [PilaCartas() for _ in range(7)]
        self.bases = [PilaCartas() for _ in range(4)]  # Una por palo
        self.mazo = PilaCartas()
        self.descarte = PilaCartas()
        self.palos = ['♠️', '♥️', '♦️', '♣️']
        self.inicializar_juego()
    
    def crear_mazo(self):
        """Crea un mazo completo de 52 cartas"""
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        cartas = []
        
        for palo in self.palos:
            for valor in valores:
                cartas.append(Carta(valor, palo))
        
        random.shuffle(cartas)
        return cartas
    
    def inicializar_juego(self):
        """Reparte las cartas al inicio del juego"""
        cartas = self.crear_mazo()
        indice = 0
        
        # Repartir cartas en las 7 columnas
        for col in range(7):
            for fila in range(col + 1):
                if indice < len(cartas):
                    carta = cartas[indice]
                    if fila == col:  # La última carta de cada columna boca arriba
                        carta.boca_arriba = True
                    self.columnas[col].apilar(carta)
                    indice += 1
        
        # El resto de cartas van al mazo
        while indice < len(cartas):
            self.mazo.apilar(cartas[indice])
            indice += 1
    
    def robar_del_mazo(self):
        """Roba una carta del mazo y la pone en descarte"""
        if self.mazo.esta_vacia():
            # Si el mazo está vacío, voltear el descarte
            while not self.descarte.esta_vacia():
                carta = self.descarte.desapilar()
                carta.boca_arriba = False
                self.mazo.apilar(carta)
            print("Mazo volteado")
        
        if not self.mazo.esta_vacia():
            carta = self.mazo.desapilar()
            carta.boca_arriba = True
            self.descarte.apilar(carta)
            print(f"Carta robada: {carta}")
        else:
            print("No hay más cartas en el mazo")
    
    def puede_mover_a_columna(self, carta, columna_destino):
        """Verifica si una carta puede moverse a una columna"""
        if self.columnas[columna_destino].esta_vacia():
            return carta.valor == 'K'  # Solo Rey en columna vacía
        
        carta_destino = self.columnas[columna_destino].ver_tope()
        if not carta_destino.boca_arriba:
            return False
        
        # Debe ser valor descendente y color alterno
        valor_carta = carta.valor_numerico()
        valor_destino = carta_destino.valor_numerico()
        
        return (valor_destino - valor_carta == 1 and 
                ((carta.es_roja() and carta_destino.es_negra()) or 
                 (carta.es_negra() and carta_destino.es_roja())))
    
    def puede_mover_a_base(self, carta, base):
        """Verifica si una carta puede moverse a una base"""
        if self.bases[base].esta_vacia():
            return carta.valor == 'A'
        
        carta_base = self.bases[base].ver_tope()
        return (carta.palo == carta_base.palo and 
                carta.valor_numerico() - carta_base.valor_numerico() == 1)
    
    def mover_carta_entre_columnas(self, origen, destino, cantidad=1):
        """Mueve cartas entre columnas"""
        if origen < 0 or origen >= 7 or destino < 0 or destino >= 7:
            print("Columnas inválidas")
            return False
        
        if self.columnas[origen].esta_vacia():
            print("La columna origen está vacía")
            return False
        
        # Verificar que las cartas a mover estén boca arriba y en secuencia válida
        cartas_a_mover = []
        actual = self.columnas[origen].tope
        
        for _ in range(cantidad):
            if actual is None or not actual.boca_arriba:
                print("No se pueden mover cartas boca abajo")
                return False
            cartas_a_mover.append(actual)
            actual = actual.siguiente
        
        # Verificar si el movimiento es válido
        if not self.puede_mover_a_columna(cartas_a_mover[-1], destino):
            print("Movimiento no válido")
            return False
        
        # Realizar el movimiento
        cartas = self.columnas[origen].mover_subpila(cantidad)
        self.columnas[destino].agregar_subpila(cartas)
        
        # Voltear la carta que queda en la columna origen si es necesaria
        if not self.columnas[origen].esta_vacia():
            carta_nueva = self.columnas[origen].ver_tope()
            if not carta_nueva.boca_arriba:
                carta_nueva.boca_arriba = True
        
        print(f"Cartas movidas de columna {origen + 1} a columna {destino + 1}")
        return True
    
    def mover_carta_a_base(self, origen_tipo, origen_indice):
        """Mueve una carta a la base correspondiente"""
        carta = None
        
        if origen_tipo == "columna":
            if self.columnas[origen_indice].esta_vacia():
                print("La columna está vacía")
                return False
            carta = self.columnas[origen_indice].ver_tope()
        elif origen_tipo == "descarte":
            if self.descarte.esta_vacia():
                print("El descarte está vacío")
                return False
            carta = self.descarte.ver_tope()
        else:
            print("Origen inválido")
            return False
        
        # Encontrar la base correspondiente al palo
        base_indice = self.palos.index(carta.palo)
        
        if not self.puede_mover_a_base(carta, base_indice):
            print("No se puede mover la carta a la base")
            return False
        
        # Realizar el movimiento
        if origen_tipo == "columna":
            carta = self.columnas[origen_indice].desapilar()
            # Voltear la siguiente carta si es necesario
            if not self.columnas[origen_indice].esta_vacia():
                siguiente = self.columnas[origen_indice].ver_tope()
                if not siguiente.boca_arriba:
                    siguiente.boca_arriba = True
        else:
            carta = self.descarte.desapilar()
        
        self.bases[base_indice].apilar(carta)
        print(f"Carta {carta} movida a la base")
        return True
    
    def mostrar_tablero(self):
        """Muestra el estado actual del tablero"""
        print("\n" + "="*60)
        print("TABLERO DE SOLITARIO")
        print("="*60)
        
        # Mostrar bases
        print("BASES:")
        for i, base in enumerate(self.bases):
            palo = self.palos[i]
            if base.esta_vacia():
                print(f"{palo}: [vacía]", end="  ")
            else:
                print(f"{palo}: {base.ver_tope()}", end="  ")
        print("\n")
        
        # Mostrar mazo y descarte
        mazo_str = f"[{self.mazo.tamaño}]" if not self.mazo.esta_vacia() else "[vacío]"
        descarte_str = str(self.descarte.ver_tope()) if not self.descarte.esta_vacia() else "[vacío]"
        print(f"MAZO: {mazo_str}    DESCARTE: {descarte_str}\n")
        
        # Mostrar columnas
        print("COLUMNAS:")
        for i in range(7):
            print(f"Col {i+1}: ", end="")
            if self.columnas[i].esta_vacia():
                print("[vacía]")
            else:
                # Mostrar todas las cartas de la columna
                cartas = []
                actual = self.columnas[i].tope
                while actual:
                    cartas.append(str(actual))
                    actual = actual.siguiente
                print(" ".join(reversed(cartas)))
        print("="*60)
    
    def verificar_victoria(self):
        """Verifica si el jugador ha ganado"""
        for base in self.bases:
            if base.tamaño != 13:  # Cada base debe tener 13 cartas (A-K)
                return False
        return True

def menu_solitario():
    """Menú principal del juego de solitario"""
    juego = JuegoSolitario()
    
    while True:
        print("\n=== SOLITARIO ===")
        print("1. Robar del mazo")
        print("2. Mover carta entre columnas")
        print("3. Mover carta a base")
        print("4. Ver tablero")
        print("5. Salir")
        
        if juego.verificar_victoria():
            print("\n¡FELICIDADES! ¡HAS GANADO!")
            break
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            juego.robar_del_mazo()
        
        elif opcion == "2":
            try:
                origen = int(input("Columna origen (1-7): ")) - 1
                destino = int(input("Columna destino (1-7): ")) - 1
                cantidad = int(input("Cantidad de cartas a mover (1 para una carta): "))
                juego.mover_carta_entre_columnas(origen, destino, cantidad)
            except ValueError:
                print("Por favor ingrese números válidos")
        
        elif opcion == "3":
            tipo = input("Mover desde (columna/descarte): ").lower()
            if tipo == "columna":
                try:
                    indice = int(input("Número de columna (1-7): ")) - 1
                    juego.mover_carta_a_base("columna", indice)
                except ValueError:
                    print("Por favor ingrese un número válido")
            elif tipo == "descarte":
                juego.mover_carta_a_base("descarte", 0)
            else:
                print("Tipo inválido")
        
        elif opcion == "4":
            juego.mostrar_tablero()
        
        elif opcion == "5":
            print("¡Gracias por jugar!")
            break
        
        else:
            print("Opción no válida")

# ==================== MENÚ PRINCIPAL ====================

def menu_principal():
    """Menú principal para seleccionar el ejercicio"""
    while True:
        print("\n" + "="*50)
        print("MÓDULO 3 - ESTRUCTURAS DE DATOS I")
        print("="*50)
        print("1. Ejercicio 1: Gestor de Tareas")
        print("2. Ejercicio 2: Juego de Solitario")
        print("3. Salir")
        
        opcion = input("Seleccione un ejercicio: ")
        
        if opcion == "1":
            menu_tareas()
        elif opcion == "2":
            menu_solitario()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if _name_ == "_main_":
    menu_principal()
