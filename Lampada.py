class Lampada:
    marca = None
    potencia = None
    estado = None
    cor_luz = None

    def ligar_lampada(self):
        if(self.estado == "ligada"):
            print(f'A lâmpada já está {self.estado}!')
        else:
            self.estado = "A lâmpada está ligada!"    
    
    def desligar_lampada(self):
        if(self.estado == "desligada"):
            print(f'A lâmpada já está {self.estado}!')
        else:
            self.estado = "A lâmpada está desligada!"    

def main():
    lampada = Lampada()

    lampada.cor_luz = "branca"
    lampada.potencia = "55w"
    lampada.estado = "desligada"
    lampada.marca = "Boa luz"


    print(f'{lampada.estado}')
    lampada.desligar_lampada()
    print(f'{lampada.estado}')
    lampada.ligar_lampada()
    print(f'{lampada.estado}')

if __name__ == "__main__":
    main()