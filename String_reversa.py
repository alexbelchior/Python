texto = "chamada"


def solution(texto):
    nString = ""
    for i in range(len(texto)):
        nString = nString + texto[len(texto)-1-i]
    return nString
  
print(solution(texto))
