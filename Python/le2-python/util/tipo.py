from enum import Enum


class Tipos(Enum):
    INTEIRO = 1
    BOOLEANO = 2
    STRING = 3
    PID = 4
    TUPLA = 5


class Tipo:
    # Simulação dos atributos estáticos e imutáveis do Java
    TIPO_INTEIRO = None
    TIPO_BOOLEANO = None
    TIPO_STRING = None
    TIPO_PID = None
    TIPO_TUPLA = None
    TIPO_INDEFINIDO = None

    def __init__(self, tipo=None, prox=None):

        if tipo is None:
            # Se for passado apenas o próximo ou nada, assume todos os tipos do Enum
            if isinstance(tipo, Tipo) or tipo is None:
                prox = tipo if isinstance(tipo, Tipo) else prox
                self._tipo = {t for t in Tipos}
        elif isinstance(tipo, set):
            self._tipo = tipo
        else:
            # Caso receba um único elemento do Enum, envelopa em um set
            self._tipo = {tipo}

        self.prox = prox

    def get(self) -> set:
        # Retorna uma cópia rasa para simular o comportamento de imutabilidade (unmodifiableSet)
        return self._tipo.copy()

    def e_inteiro(self) -> bool:
        return Tipos.INTEIRO in self._tipo

    def e_booleano(self) -> bool:
        return Tipos.BOOLEANO in self._tipo

    def e_string(self) -> bool:
        return Tipos.STRING in self._tipo

    def e_pid(self) -> bool:
        return Tipos.PID in self._tipo

    def e_tupla(self) -> bool:
        return Tipos.TUPLA in self._tipo

    def e_void(self) -> bool:
        return len(self._tipo) == 0

    def e_valido(self) -> bool:
        return len(self._tipo) == 1

    def intersecao(self, outro_tipo: 'Tipo') -> 'Tipo':
        if self._tipo == outro_tipo._tipo:
            return self
        else:
            # O operador '&' realiza a interseção entre dois sets no Python
            t_intersecao = self._tipo & outro_tipo._tipo
            return Tipo(t_intersecao)

    def __eq__(self, outro) -> bool:
        if not isinstance(outro, Tipo):
            return False
        return self._tipo == outro._tipo

    def __repr__(self):
        nomes_tipos = [t.name for t in self._tipo]
        return f"Tipo({nomes_tipos})" + (f" -> {self.prox}" if self.prox else "")


# Inicialização das constantes estáticas (equivalente ao bloco static do Java)
Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_PID = Tipo({Tipos.PID})
Tipo.TIPO_TUPLA = Tipo({Tipos.TUPLA})
Tipo.TIPO_INDEFINIDO = Tipo(set())
