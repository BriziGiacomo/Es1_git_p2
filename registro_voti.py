class RegistroVoti:
    def __init__(self):
        self.voti = []

    def media(self):
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

    if __name__ == "__main__":
        registro = RegistroVoti()
        registro.aggiungi_voto(8)
        registro.aggiungi_voto(10)
        print(f"Voti registrati: {registro.voti}")

    # Caso di prova
        m = registro.media()
        print(f"Media calcolata: {m}")
        assert m == 9.0, f"Errore nel calcolo: atteso 9.0, ottenuto {m}"
        print("Test media superato con successo.")    
        