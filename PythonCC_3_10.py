vacunas=["HEXAVALENTE","BCG",
        "ANTIHEPATITISB",
        "PENTAVALENTE",
        "DPT",
        "ANTIROTAVIRUS",
        "SABIN",
        "SR",
        "INFLUENZAAYB",
        "TRIPLE VIRAL",
        "ANTINEUMOCOCICA",
        "VPH"]
print(vacunas)
print(sorted(vacunas))
print(sorted(vacunas, reverse=True))
print(len(vacunas))
vacunas.pop()
del(vacunas[0])
print(vacunas)

vacunas.insert(0,"INFLUENZA23SEROTIPOS")
vacunas.append("DPrT")
print(vacunas)
vacunas.pop()
del(vacunas[0])


vacunas.sort()
print(vacunas)
vacunas.reverse()
print(vacunas)
