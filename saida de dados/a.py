s = "PPALLP"
presente = 0
Ausente = 0
atrasado =0
for l in s:
    if l == "A":
        Ausente +=1
    elif l == "L":
        atrasado +=1
    else:
        presente +=1 
print(f"O aluno teve {Ausente} faltas {atrasado} atrasos e {presente} presencias")
