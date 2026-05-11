from enum import Enum, auto
from typing import Set, Optional, ClassVar

class Tipos(Enum):
    INTEIRO = auto()
    BOOLEANO = auto()
    STRING = auto()
    PID = auto()
    TUPLA = auto()

class Tipo:
    # Definição de constantes de classe (Singleton-like)
    TIPO_INTEIRO: 'Tipo'
    TIPO_BOOLEANO: 'Tipo'
    TIPO_STRING: 'Tipo'
    TIPO_INDEFINIDO: 'Tipo'
    # ... inicializados após a definição da classe

    def __init__(self, tipos: Set[Tipos], prox: Optional['Tipo'] = None):
        # Se tipos for None, assume todos (análogo ao EnumSet.allOf)
        self._tipos = tipos if tipos is not None else set(Tipos)
        self.prox = prox

    @property
    def tipos(self):
        return frozenset(self._tipos) # Imutável como no Java

    def e_inteiro(self) -> bool:
        return Tipos.INTEIRO in self._tipos

    def e_booleano(self) -> bool:
        return Tipos.BOOLEANO in self._tipos
    
    def e_string(self) -> bool:
        return Tipos.STRING in self._tipos

    def e_void(self) -> bool:
        return not self._tipos

    def e_valido(self) -> bool:
        return len(self._tipos) == 1

    def intersecao(self, outro: 'Tipo') -> 'Tipo':
        """Usa o operador '&' de conjuntos para interseção idiomática."""
        novo_set = self._tipos & outro._tipos
        return Tipo(novo_set)

    def __eq__(self, outro):
        if not isinstance(outro, Tipo):
            return False
        return self._tipos == outro._tipos

# Inicialização das instâncias compartilhadas
Tipo.TIPO_INTEIRO = Tipo({Tipos.INTEIRO})
Tipo.TIPO_BOOLEANO = Tipo({Tipos.BOOLEANO})
Tipo.TIPO_STRING = Tipo({Tipos.STRING})
Tipo.TIPO_INDEFINIDO = Tipo(set())