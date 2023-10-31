from clase_equipo import Equipo, ruta_de_archivo
from app import dream_team_app

if __name__ == "__main__":
    equipo = Equipo(ruta_de_archivo)
    dream_team_app(equipo)