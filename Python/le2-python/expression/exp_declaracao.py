from memory.variavel_ja_declarada_exception import VariavelJaDeclaradaException


class ExpDeclaracao:
    def __init__(self, declarations: list, expressao_arg):
        self.seqdec_variavel = declarations
        self.expressao = expressao_arg

    def avaliar(self, ambiente):
        ambiente.incrementa()

        resolved_values = self._resolve_value_bindings(ambiente)
        self._include_value_bindings(ambiente, resolved_values)

        result = self.expressao.avaliar(ambiente)

        ambiente.restaura()
        return result

    def _include_value_bindings(self, ambiente, resolved_values: dict):
        for id_obj, valor in resolved_values.items():
            ambiente.map(id_obj, valor)

    def _resolve_value_bindings(self, ambiente) -> dict:
        resolved_values = {}
        for declaration in self.seqdec_variavel:
            resolved_values[declaration.id] = declaration.expressao.avaliar(
                ambiente)
        return resolved_values

    def checa_tipo(self, ambiente) -> bool:
        ambiente.incrementa()
        result = False
        try:
            if self._check_type_bindings(ambiente):
                resolved_types = self._resolve_type_bindings(ambiente)
                self._include_type_bindings(ambiente, resolved_types)
                result = self.expressao.checa_tipo(ambiente)
            else:
                result = False
        finally:
            # Garante que o ambiente seja restaurado mesmo se ocorrer uma exceção
            ambiente.restaura()
        return result

    def _include_type_bindings(self, ambiente, resolved_types: dict):
        for id_obj, tipo in resolved_types.items():
            ambiente.map(id_obj, tipo)

    def _resolve_type_bindings(self, ambiente) -> dict:
        resolved_types = {}
        for declaration in self.seqdec_variavel:
            var_id = declaration.id
            if var_id in resolved_types:
                raise VariavelJaDeclaradaException(var_id)

            resolved_types[var_id] = declaration.expressao.get_tipo(ambiente)
        return resolved_types

    def _check_type_bindings(self, ambiente) -> bool:
        for declaration in self.seqdec_variavel:
            if not declaration.expressao.checa_tipo(ambiente):
                return False
        return True

    def get_tipo(self, ambiente):
        ambiente.incrementa()
        resolved_types = self._resolve_type_bindings(ambiente)
        self._include_type_bindings(ambiente, resolved_types)

        result = self.expressao.get_tipo(ambiente)

        ambiente.restaura()
        return result
