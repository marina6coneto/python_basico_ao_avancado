# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return
        print(f'{self.nome} está filmando.')
        self.filmando = True
        
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando.')
            return
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False
    
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto estiver filmando.')
            return
        print(f'{self.nome} está fotografando.')
        
        
c1 = Camera('Sony')
c2 = Camera('Canon')
        
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()