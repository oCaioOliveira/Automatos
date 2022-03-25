from functools import partial
from itertools import chain
#
# Automatos
#
estados = {1, 4}
transicoes = {
    (1, "a"): {2},
    (1, "b"): {4},
    (2, "b"): {3, 4},
    (3, "a"): {2},
    (3, "b"): {4},
    (4, "a"): {3},
}
validos = {3}
epsilons = {
    3: {2, 4},
    2: {4},
}

def NFA(transicoes, estados: set, validos, st) -> bool:
    estados = estados.copy()
    for i in st:
        estados = set(chain.from_iterable(transicoes.get((s, i), ()) for s in estados))

    return bool(estados.intersection(validos))


def NFAalter(transicoes, estados: set, validos, st) -> bool:
    estados = estados.copy()
    for i in st:
        novos_estados = set()
        for estado in estados:
            novos_estados.update(transicoes.get((estado, i), ()))
        estados = novos_estados

    return bool(estados.intersection(validos))


def NFAe(transicoes, estados: set, validos, epsiolons, st) -> bool:
    estados = estados.copy()

    for estado in estados.copy():
        estados.update(epsilons.get(estado, ()))

    for i in st:
        novos_estados = set()
        for estado in estados:
            novos_estados.update(transicoes.get((estado, i), ()))
        estados = novos_estados

        for estado in estados.copy():
            estados.update(epsilons.get(estado, ()))

    return bool(estados.intersection(validos))

abba1 = partial(NFA, transicoes, estados, validos)
abba2 = partial(NFAe, transicoes, estados, validos, epsilons)

testes = ["a", "ab", "aba", "aabb", "abba", "abba" * 4, "abaaba", "abaa"]
for st in testes:
        print(f"{st}: {abba1(st)}/{abba2(st)}")