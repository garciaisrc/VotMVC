from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos


class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()

    def index(self):
        return self.repositorioCandidatos.findAll()

    def create(self, infoCandidatos):
        nuevoCandidato = Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        CandidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellidos = infoCandidato["apellidos"]
        CandidatoActual.cedula = infoCandidato["cedula"]
        CandidatoActual.partido = infoCandidato["partido"]
        CandidatoActual.estado = infoCandidato["estado"]
        CandidatoActual.descripcion = infoCandidato["descripcion"]
        return self.repositorioCandidatos.save(CandidatoActual)

    def delete(self, id):
        return self.repositorioCandidatos.delete(id)
