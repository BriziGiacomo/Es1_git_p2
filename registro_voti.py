class RegistroVoti:
    def __init__(self):
        self.voti = []

    def media(self):
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

if __name__ == "__main__":
    registro = RegistroVoti()
    registro.aggiungi_voto(8)
    registro.aggiungi_voto(10)
    print(f"Voti registrati: {registro.voti}")

    #Caso di bocciatura
    studenti_bocciati = [voto for voto in registro.voti if voto < 5.45]  
    print(f"Studenti bocciati: {studenti_bocciati}")