from Modelos.Mesas import Mesas
from Repositorios.RepositorioMesas import RepositorioMesas


class ControladorMesas():
    def __init__(self):
        self.repositorioMesas = RepositorioMesas()

    def index(self):
        return self.repositorioMesas.findAll()

    def create(self, infoMesas):
        nuevaMesa = Mesas(infoMesas)
        return self.repositorioMesas.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesas(self.repositorioMesas.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesas):
        MesaActual = Mesas(self.repositorioMesas.findById(id))
        MesaActual.localizacion = infoMesas["localizacion"]
        MesaActual.estado = infoMesas["estado"]
        return self.repositorioMesas.save(MesaActual)

    def delete(self, id):
        return self.repositorioMesas.delete(id)
