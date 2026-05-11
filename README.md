# Paradigmas de Linguagens de Programação — UFS

Repositório de atividades práticas da disciplina **Paradigmas de Linguagens de Programação** da Universidade Federal de Sergipe (UFS).

---

## 📚 Sobre a Disciplina

A disciplina aborda os principais paradigmas de linguagens de programação — imperativo, funcional, orientado a objetos e lógico — com foco em semântica, tipagem e estrutura de linguagens. As atividades envolvem a implementação de interpretadores de linguagens de expressão simples (PLP — *Programming Language Principles*).

---

## 🗂️ Estrutura do Repositório

```
paradigmas-lp/
├── Java/
│   └── le1/                    # Implementação em Java da LE1
│       └── plp/expressions1/
│           ├── Exemplo1.java   # Exemplo simples: (4 + 12) - 3
│           ├── Exemplos.java   # Bateria de exemplos com verificação de tipos
│           ├── Programa.java   # Classe raiz que executa e verifica uma expressão
│           ├── expression/     # Classes de expressão (ExpSoma, ExpAnd, etc.)
│           └── util/           # Utilitários (Tipo)
└── Python/
    └── le1-python/             # Implementação equivalente em Python da LE1
        ├── Programa.py         # Classe raiz que executa e verifica uma expressão
        ├── expression/         # Módulos de expressão (exp_soma, exp_and, etc.)
        └── util/
            └── tipo.py         # Sistema de tipos (Tipo, Tipos)
```

---

## 🧪 Linguagem de Expressão 1 (LE1)

A **LE1** é uma linguagem de expressão simples com suporte a:

| Tipo de Expressão | Operação                         | Exemplo              |
|-------------------|----------------------------------|----------------------|
| Aritmética        | Soma, subtração, negação unária  | `4 + 12 - 3` → `13` |
| String            | Concatenação, comprimento        | `"abc" ++ "def"`, `length("abc")` → `3` |
| Booleana          | And, Or, Not, Igualdade          | `true and false` → `false` |

### Verificação de Tipos

Cada expressão implementa `checaTipo()` / `checa_tipo()`, que valida a consistência dos operandos antes de avaliar. Expressões mal tipadas (e.g. `1 + true`) são detectadas sem avaliar.

### Árvore de Expressão

As expressões são representadas como uma árvore composta de nós (`Expressao`). Por exemplo, `(4 + 12) - 3`:

```
    ExpSub
   /      \
ExpSoma    3
 /    \
4      12
```

---

## ▶️ Como Executar

### Java

**Pré-requisitos:** JDK 8+

```bash
# Compile a partir da raiz do projeto Java
cd Java/le1
javac -d out $(find . -name "*.java")

# Execute o exemplo principal
java -cp out le1.plp.expressions1.Exemplo1

# Execute a bateria de exemplos (com verificação de tipos)
java -cp out le1.plp.expressions1.Exemplos
```

**Saída esperada de `Exemplo1`:**
```
Expressão: 4 + 12 - 3
Bem tipada: true
13
```

### Python

**Pré-requisitos:** Python 3.7+

```bash
cd Python/le1-python

# Execute um programa de teste
python -c "
from expression.exp_soma import ExpSoma
from expression.exp_sub import ExpSub
from expression.valor_inteiro import ValorInteiro
from Programa import Programa

prog = Programa(ExpSub(ExpSoma(ValorInteiro(4), ValorInteiro(12)), ValorInteiro(3)))
print('Bem tipada:', prog.checa_tipo())
prog.executar()
"
```

**Saída esperada:**
```
Bem tipada: True
13
```

---

## 🔧 Tecnologias

| Linguagem | Versão usada | IDE recomendada  |
|-----------|--------------|------------------|
| Java      | JDK 25       | IntelliJ IDEA    |
| Python    | Python 3.13  | VS Code          |

---
