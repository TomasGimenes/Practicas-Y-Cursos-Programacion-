#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(seft,err):
        print(f"Impresionante,cometitste el siguiente error: {err}")

#lanzando mi propia excepcion
try:    
    raise MiExcepcion("jajajaja, oersona poco culta")
except:
    print("Como vas a cometer ese error?")