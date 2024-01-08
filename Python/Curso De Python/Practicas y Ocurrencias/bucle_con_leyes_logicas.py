dist = "(p ∧ q) ∨ r"
dist1 = "(p ∨ r) ∧ (q ∨ r)"

pregunta = input("¿quieres simplificar utilizando distributiva?: ")

if pregunta == "si":
    while dist == ("(p ∧ q) ∨ r"):
        dist = dist1
        print(dist)
        dist = "(p ∧ q) ∨ r"
        print(dist)