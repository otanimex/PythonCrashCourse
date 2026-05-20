#Lista de personas con las que me gustaría tener una cena
personas=["Ana Tamara","Ana Bertha","Samantha","Frida","Gabriela","Zaa","David"]
mensaje="Por medio de la presente Alexandra le invita a usted "
mensaje2=" a su gran cena de graduación, favor de confirmar su asistencia"
for persona in personas:
    print(mensaje+persona+mensaje2)

noAsistentes=[personas[-1],personas[-2]]
mensaje3="Por razones de tiempos no podrán asistir:"
print(mensaje3)
for noAsistente in noAsistentes:
    print(noAsistente)
    personas.pop()

mensaje4="Los asistentes al evento serán:"
print(mensaje4)
for persona in personas:
    print(persona)

mensaje5="Se han incluido nuevos invitados:"
personas.insert(2,"Norma Alicia")
personas.insert(3,"Karla Paulina")
personas.append("Onegui")
print(mensaje5)
for persona in personas:
    print(persona)
