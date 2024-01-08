#2 listas, una con nombres otra con apellidos
nombres = ["Lucas","Tomas","Daniel","Camila","Roberto"]
apellidos = ["Dalto","Gimenes","Ramirez","Peralta","Chano"]

#Registrar esta informacion en un TXT de forma optima
with open("Archivos_Problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n----------\n") for n,a in zip(nombres,apellidos)]