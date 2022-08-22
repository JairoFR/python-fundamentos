from clases import Mascota
from clases import Ninja

max = Mascota("max", "perro", "dormir", "Guau Guau Guau Guau!!")
alimento_mascota = ["dogshow", "champion dog", "cachupin"]
jairo = Ninja("jairo", "flores", max, "hueso de pollo", alimento_mascota)
jairo.mascota.niveles()
jairo.sleep().alimentar().bañar().mascota.niveles()