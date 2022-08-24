from datetime import datetime
from .structures import *
from .models import *

def saveLog(usuario, descripcion, excepcion):
    try:
        log = ExceptionLog(
            usuario = usuario,
            descripcion = descripcion,
            excepcion = excepcion,
            fecha = datetime.now()
        )
        log.save()
    except Exception as e:
        print("  ===>  Error: No se puede guardar log. Exception: "+str(e))

def obtenerFecha(fecha):
    splited = fecha.split("-")
    date = datetime(int(splited[0]), int(splited[1]), int(splited[2]))
    return date

def GetSelectData(paciente):
    tipos = ["", "CC", "TI", "RC"]
    selectTipoDocumento = []
    for e in tipos:
        if paciente.tipoDocumento == e:
            selectTipoDocumento.append(SelectItem(e, "selected"))
        else:
            selectTipoDocumento.append(SelectItem(e, ""))

    sexos = ["", "Masculino", "Femenino"]
    selectSexo = []
    for e in sexos:
        if paciente.sexo == e:
            selectSexo.append(SelectItem(e, "selected"))
        else:
            selectSexo.append(SelectItem(e, ""))

    estadosCiviles = ["", "Soltero/a", "Casado/a", "Unión libre", "Separado/a", "Divorciado/a", "Viudo/a"]
    selectEstadoCivil = []
    for e in estadosCiviles:
        if paciente.estadoCivil == e:
            selectEstadoCivil.append(SelectItem(e, "selected"))
        else:
            selectEstadoCivil.append(SelectItem(e, ""))

    diagnosticos = Diagnostico.objects.order_by('nombre')
    selectDiagnostico = []
    selectDiagnostico.append(SelectItem("", "selected", ""))
    for e in diagnosticos:
        if paciente.diagnostico == e:
            selectDiagnostico.append(SelectItem(e.nombre, "selected", e.id))
        else:
            selectDiagnostico.append(SelectItem(e.nombre, "", e.id))

    selectData = SelectData(selectTipoDocumento, selectSexo, selectEstadoCivil, selectDiagnostico)
    return selectData

def GetSelectTipoDocumento():
    tipos = ["", "CC", "TI", "RC"]
    selectTipoDocumento = []
    for e in tipos:
        selectTipoDocumento.append(SelectItem(e, ""))
    return selectTipoDocumento
