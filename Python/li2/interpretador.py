# ==============================================================================
# AMBIENTE DE EXECUÇÃO (Escopo Dinâmico)
# ==============================================================================
class AmbienteExecucaoImperativa2:
    def __init__(self):
        # Memória principal: pilha de mapeamentos de variáveis (Id -> Valor)
        self.pilha_memoria = [{}]
        # Pilha de mapeamentos de procedimentos (Id -> Procedimento)
        self.pilha_procedimentos = [{}]
        # Entrada e Saída
        self.entrada = []
        self.saida = []

    def incrementa(self):
        """Incrementa o escopo (empilha novos frames de memória e procedimentos)"""
        self.pilha_memoria.append({})
        self.pilha_procedimentos.append({})

    def restaura(self):
        """Restaura o escopo anterior (desempilha)"""
        if len(self.pilha_memoria) > 1:
            self.pilha_memoria.pop()
            self.pilha_procedimentos.pop()

    def map_variavel(self, id_var, valor):
        self.pilha_memoria[-1][id_var] = valor

    def set_variavel(self, id_var, valor):
        for frame in reversed(self.pilha_memoria):
            if id_var in frame:
                frame[id_var] = valor
                return
        raise Exception(f"Erro Semântico: Variável '{id_var}' não declarada.")

    def get_variavel(self, id_var):
        for frame in reversed(self.pilha_memoria):
            if id_var in frame:
                return frame[id_var]
        raise Exception(f"Erro Semântico: Variável '{id_var}' não declarada.")

    # Gerenciamento de Procedimentos
    def map_procedimento(self, id_proc, procedimento):
        self.pilha_procedimentos[-1][id_proc] = procedimento

    def get_procedimento(self, id_proc):
        for frame in reversed(self.pilha_procedimentos):
            if id_proc in frame:
                return frame[id_proc]
        raise Exception(f"Erro Semântico: Procedimento '{id_proc}' não declarado.")

    def write(self, valor):
        self.saida.append(valor)

class Exp:
    def avaliar(self, amb):
        pass

class Valor(Exp):
    def __init__(self, valor):
        self.valor = valor
    def avaliar(self, amb):
        return self.valor

class Id(Exp):
    def __init__(self, nome):
        self.nome = nome
    def avaliar(self, amb):
        return amb.get_variavel(self.nome)

class ExpSoma(Exp):
    def __init__(self, exp1, exp2):
        self.exp1, self.exp2 = exp1, exp2
    def avaliar(self, amb):
        return self.exp1.avaliar(amb) + self.exp2.avaliar(amb)

class ExpSub(Exp):
    def __init__(self, exp1, exp2):
        self.exp1, self.exp2 = exp1, exp2
    def avaliar(self, amb):
        return self.exp1.avaliar(amb) - self.exp2.avaliar(amb)

class ExpIgual(Exp):
    def __init__(self, exp1, exp2):
        self.exp1, self.exp2 = exp1, exp2
    def avaliar(self, amb):
        return self.exp1.avaliar(amb) == self.exp2.avaliar(amb)

class ExpNot(Exp):
    def __init__(self, exp):
        self.exp = exp
    def avaliar(self, amb):
        return not self.exp.avaliar(amb)


class Procedimento:
    def __init__(self, parametros_formais, comando):
        self.parametros_formais = parametros_formais
        self.comando = comando

class Declaracao:
    def executar(self, amb):
        pass

class DecVariavel(Declaracao):
    def __init__(self, nome, exp_inicial):
        self.nome = nome
        self.exp_inicial = exp_inicial
    def executar(self, amb):
        valor = self.exp_inicial.avaliar(amb)
        amb.map_variavel(self.nome, valor)

class DecProcedimento(Declaracao):
    def __init__(self, nome, parametros, comando):
        self.nome = nome
        self.parametros = parametros
        self.comando = comando
    def executar(self, amb):
        proc = Procedimento(self.parametros, self.comando)
        amb.map_procedimento(self.nome, proc)

class DecComposta(Declaracao):
    def __init__(self, decs):
        self.decs = decs
    def executar(self, amb):
        for dec in self.decs:
            dec.executar(amb)

class Comando:
    def executar(self, amb):
        pass

class Skip(Comando):
    def executar(self, amb):
        pass

class Atribuicao(Comando):
    def __init__(self, nome_id, exp):
        self.nome_id = nome_id
        self.exp = exp
    def executar(self, amb):
        valor = self.exp.avaliar(amb)
        amb.set_variavel(self.nome_id, valor)

class Write(Comando):
    def __init__(self, exp):
        self.exp = exp
    def executar(self, amb):
        valor = self.exp.avaliar(amb)
        amb.write(valor)

class Sequencia(Comando):
    def __init__(self, comandos):
        self.comandos = comandos
    def executar(self, amb):
        for cmd in self.comandos:
            cmd.executar(amb)

class ComandoDeclaracao(Comando):
    def __init__(self, declaracao, comando):
        self.declaracao = declaracao
        self.comando = comando
    def executar(self, amb):
        amb.incrementa()
        self.declaracao.executar(amb)
        self.comando.executar(amb)
        amb.restaura()

class IfThenElse(Comando):
    def __init__(self, condicao, comando_then, comando_else):
        self.condicao = condicao
        self.comando_then = comando_then
        self.comando_else = comando_else
    def executar(self, amb):
        if self.condicao.avaliar(amb):
            self.comando_then.executar(amb)
        else:
            self.comando_else.executar(amb)

class ChamadaProcedimento(Comando):
    def __init__(self, nome_procedimento, parametros_reais):
        self.nome_procedimento = nome_procedimento
        self.parametros_reais = parametros_reais

    def executar(self, amb):
        proc = amb.get_procedimento(self.nome_procedimento)
        valores_reais = [exp.avaliar(amb) for exp in self.parametros_reais]
        amb.incrementa()
        for param, val in zip(proc.parametros_formais, valores_reais):
            amb.map_variavel(param, val)
        proc.comando.executar(amb)
        amb.restaura()