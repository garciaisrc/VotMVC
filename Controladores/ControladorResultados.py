from Modelos.Resultados import Resultados
from Repositorios.RepositorioResultados import RepositorioResultados


class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self, infoResultados):
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultados):
        ResultantActual = Resultados(self.repositorioResultados.findById(id))
        ResultantActual.partidos = infoResultados["partidos"]
        ResultantActual.votos = infoResultados["votos"]
        return self.repositorioResultados.save(ResultantActual)

    def delete(self, id):
        return self.repositorioResultados.delete(id)