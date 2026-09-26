class LuminariaSmart:
    def __init__(self, id_dispositivo: str):
        self.id_dispositivo: str = id_dispositivo
        self.ligada: bool = False
        self.intensidade: int = 0  # Valor padrão 0

    def alternar_estado(self) -> None:
        self.ligada = not self.ligada

    def ajustar_intensidade(self, valor: int) -> None:
        if valor < 0:
            self.intensidade = 0
        elif valor > 100:
            self.intensidade = 100
        else:
            self.intensidade = valor

    def __str__(self) -> str:
        estado = "Ligada" if self.ligada else "Desligada"
        return f"Luminária [ID: {self.id_dispositivo}, Estado: {estado}, Intensidade: {self.intensidade}%]"


# Execução do cenário solicitado
if __name__ == "__main__":
    # 1. Cria uma instância da classe
    luminaria = LuminariaSmart("LUM-001")

    # 2. Liga a luminária (inverte o estado inicial de False para True)
    luminaria.alternar_estado()

    # 3. Ajusta a intensidade
    luminaria.ajustar_intensidade(75)

    # 4. Imprime o estado final do objeto
    print(luminaria)