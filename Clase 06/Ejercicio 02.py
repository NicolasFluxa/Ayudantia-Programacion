

"""
Crea un mini reproductor de medios con:

Una clase base Media que encapsule título y duración (privados) y defina un método abstracto play().

Dos subclases:

Song (canción)

Podcast (incluye además un atributo host)

Una clase Playlist que mantenga internamente una lista de objetos Media, con métodos para añadir pistas y reproducir toda la lista.

Sobrecarga de + para concatenar dos playlists y de len() para obtener cuántas pistas hay.
"""

from abc import ABC, abstractmethod

# 1. Clase base abstracta
class Media(ABC):
    def __init__(self, titulo, duracion):
        self.__titulo = titulo        # Privado
        self.__duracion = duracion    # Privado (en segundos)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def duracion(self):
        return self.__duracion

    @abstractmethod
    def play(self):
        """Inicia la reproducción del medio."""
        pass

    def __str__(self):
        return f"{self.__titulo} ({self.__duracion}s)"

# 2a. Subclase Song
class Song(Media):
    def play(self):
        return f"▶️ Reproduciendo canción: {self}"

# 2b. Subclase Podcast
class Podcast(Media):
    def __init__(self, titulo, duracion, host):
        super().__init__(titulo, duracion)
        self.__host = host  # Privado

    def play(self):
        return (f"🎙️ Reproduciendo podcast: {self} — "
                f"Host: {self.__host}")

# 3. Playlist
class Playlist:
    def __init__(self, nombre):
        self.__nombre = nombre      # Privado
        self.__tracks = []          # Lista privada de Media

    def add(self, medio: Media):
        self.__tracks.append(medio)

    def play_all(self):
        print(f"📂 Playlist: {self.__nombre}")
        for m in self.__tracks:
            print(m.play())

    def __add__(self, otra):
        if not isinstance(otra, Playlist):
            return NotImplemented
        nueva = Playlist(f"{self.__nombre} + {otra.__nombre}")
        nueva.__tracks = self.__tracks.copy() + otra.__tracks.copy()
        return nueva

    def __len__(self):
        return len(self.__tracks)

# --- Uso cotidiano ---
if __name__ == "__main__":
    s1 = Song("Imagine", 183)
    p1 = Podcast("Python Talks", 3600, "María Pérez")

    pl1 = Playlist("Favoritas")
    pl1.add(s1)
    pl1.add(p1)
    pl1.play_all()
    print("Cantidad pistas:", len(pl1))
    print("-" * 40)

    # Concatenar con otra playlist
    pl2 = Playlist("Descubrimientos")
    pl2.add(Song("New Song", 200))
    combined = pl1 + pl2
    combined.play_all()
    print("Total pistas combinado:", len(combined))


"""
¿Cómo se aplica el encapsulamiento en la clase Media y cuáles son sus beneficios?

Los atributos __titulo y __duracion son privados y sólo accesibles vía propiedades (@property), impidiendo lecturas o escrituras directas desde fuera.

Esto previene asignaciones inválidas (por ejemplo, duraciones negativas) y facilita mantener invariantes internas.

¿Qué muestra el método play() en cada subclase y cómo ejemplifica el polimorfismo?

Song.play() retorna una cadena con icono de canción y sus datos; Podcast.play() incluye icono de podcast, datos y además el nombre del host.

Llamar play() en una colección de objetos Media ejecuta la implementación específica de cada tipo, sin necesidad de comprobar manualmente su clase.

Explique cómo la sobrecarga de __add__ une dos playlists sin modificar las originales.

Sobre el operador +, se crea una nueva instancia de Playlist cuyo nombre concatena ambos nombres originales.

Luego se asigna a su lista interna la copia (.copy()) de las dos listas de pistas, dejando intactas las listas de las playlists originales.
"""
