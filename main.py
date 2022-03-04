from functools import partial
#
# Automatos
#
estado = 1
transicoes = {
    (1, "a"): 2,
    (1, "b"): 4,
    (2, "b"): 3,
    (3, "a"): 2,
    (3, "b"): 4,
    (4, "a"): 3,
}
validos = {3}

def DFA(transicoes, estado, validos, st) -> bool:
    for i in st:
        try:
            estado = transicoes[estado, i]
        except KeyError:
            return False
    return estado in validos

abba1 = partial(DFA, transicoes, estado, validos)
abba2 = partial(DFA, transicoes, estado, {2})

testes = ["ab", "aabb", "abba", "abba" * 4, "a", "aba"]
for st in testes:
        print(f"{st}: {abba1(st)}/{abba2(st)}")