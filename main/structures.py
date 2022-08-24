class Alert:
    def __init__(self, mensaje, tipo):
        self.mensaje = mensaje
        self.tipo = tipo

class SelectItem:
    def __init__(self, nombre, selected, id=0):
        self.id = id
        self.nombre = nombre
        self.selected = selected

class SelectData:
    def __init__(self, selectTipoDocumento, selectSexo, selectEstadoCivil, selectDiagnostico):
        self.selectTipoDocumento = selectTipoDocumento
        self.selectSexo = selectSexo
        self.selectEstadoCivil = selectEstadoCivil
        self.selectDiagnostico = selectDiagnostico
