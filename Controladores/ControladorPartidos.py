from Modelos.Partidos import Partidos
from Repositorios.RepositorioPartidos import RepositorioPartidos


class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()

    def index(self):
        return self.repositorioPartidos.findAll()

    def create(self, infoPartidos):
        nuevopartidopol = Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevopartidopol)

    def show(self, id):
        partidopol = Partidos(self.repositorioPartidos.findById(id))
        return partidopol.__dict__

    def update(self, id, infoPartidos):
        PartidopolActual = Partidos(self.repositorioPartidos.findById(id))
        PartidopolActual.nombre = infoPartidos["nombre"]
        PartidopolActual.estado = infoPartidos["estado"]
        return self.repositorioPartidos.save(PartidopolActual)

    def delete(self, id):
        return self.repositorioPartidos.delete(id)