def two_sum(nums, target):
    # Crear un diccionario para almacenar los valores y sus índices
    num_dict = {}
    
    # Recorrer el array
    for i, num in enumerate(nums):
        # Calcular el complemento necesario para alcanzar el objetivo
        complement = target - num
        
        # Verificar si el complemento ya está en el diccionario
        if complement in num_dict:
            # Devolver los índices de los dos números que suman el objetivo
            return [num_dict[complement], i]
        
        # Si no está en el diccionario, agregar el número actual y su índice
        num_dict[num] = i
    
    # En caso de que no se encuentre ninguna solución
    return None

nums = [2, 7, 11, 15]
target = 9
resultado = two_sum(nums, target)
print(resultado)