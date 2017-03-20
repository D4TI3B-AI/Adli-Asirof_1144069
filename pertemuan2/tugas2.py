graph = {'stadion siliwangi': ['Jalan Bangka', 'Jalan manado','Jalan Manado'],
             'Jalan Bangka': ['Jalan Ermawar','Jalan Tongkeng'],
              'Jalan Manado': ['Jalan Patra Komala','Jalan Tongkeng'],
             'Jalan Manado': ['Jalan Ermawar','Jalan Tongkeng'],
             'Jalan Tongkeng': ['Jalan Ermawar','Jalan Patra Komala','Jalan Ermawar'],
         }
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Menuju Stadion Siliwangi")
print ("Stadion Siliwangi,Jalan Bangka,Jalan Manado,Jalan Tongkeng,Jalan Patra Komala")
print ("\n")
awal = raw_input("Masukan Awal : ")
tujuan = raw_input("Masukan Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil
