"""Motor generico FIRST / FOLLOW / PREDICT / tabla LL(1).

Sigue el PDF "Analisis sintactico descendente" (diapos 10-20, 24):
 - PRIMEROS por punto fijo (diapos 11, 13).
 - SIGUIENTES por punto fijo (diapo 15). El $ solo vive en SIGUIENTES.
 - PRED(A -> alfa) (diapo 17).
 - Tabla LL(1) + conflictos (diapos 19, 24).

Formato de gramatica:
    {"S": [["A", "uno", "B", "C"], ["S", "dos"]], ...}
La produccion epsilon se escribe ["ε"]. El simbolo inicial se pasa aparte.
"""

EPS = "ε"
END = "$"


def _terminales_no_terminales(gramatica):
    no_term = set(gramatica.keys())
    term = set()
    for alts in gramatica.values():
        for alt in alts:
            for s in alt:
                if s not in (EPS,) and s not in no_term:
                    term.add(s)
    return term, no_term


def calcular_nullable(gramatica):
    """Un NT es anulable si puede derivar ε (punto fijo)."""
    anul = set()
    for nt, alts in gramatica.items():
        if any(alt == [EPS] for alt in alts):
            anul.add(nt)
    cambio = True
    while cambio:
        cambio = False
        for nt, alts in gramatica.items():
            if nt in anul:
                continue
            for alt in alts:
                if alt == [EPS]:
                    continue
                if all(s in anul for s in alt):
                    # ojo: si alt tiene un terminal, `s in anul` es False -> no cuenta
                    anul.add(nt)
                    cambio = True
                    break
    return anul


def _first_seq(seq, first, terminales):
    """PRIMEROS de una secuencia (diapo 11). `first` solo tiene NT."""
    res = set()
    if seq == [EPS]:
        return {EPS}
    for s in seq:
        if s == EPS:
            res.add(EPS)
            break
        if s in terminales:
            res.add(s)
            break
        # no terminal
        res |= (first.get(s, set()) - {EPS})
        if EPS not in first.get(s, set()):
            break
    else:
        # solo si TODOS fueron anulables (el for no hizo break)
        res.add(EPS)
    return res


def calcular_first(gramatica, anulables):
    term, _ = _terminales_no_terminales(gramatica)
    first = {nt: set() for nt in gramatica}
    cambio = True
    while cambio:
        cambio = False
        for nt, alts in gramatica.items():
            for alt in alts:
                nuevo = _first_seq(alt, first, term)
                if not nuevo <= first[nt]:
                    first[nt] |= nuevo
                    cambio = True
    return first


def _seq_anulable(seq, anulables):
    if seq == [EPS]:
        return True
    return all(s in anulables for s in seq)


def calcular_follow(gramatica, first, anulables, inicial):
    term, no_term = _terminales_no_terminales(gramatica)
    follow = {nt: set() for nt in gramatica}
    follow[inicial].add(END)
    cambio = True
    while cambio:
        cambio = False
        for a, alts in gramatica.items():
            for alt in alts:
                if alt == [EPS]:
                    continue
                for i, b in enumerate(alt):
                    if b not in no_term:
                        continue
                    beta = alt[i + 1:]
                    if beta:
                        fb = _first_seq(beta, first, term) - {EPS}
                        if not fb <= follow[b]:
                            follow[b] |= fb
                            cambio = True
                    # beta vacia o anulable -> hereda SIGUIENTES(A). Diapo 15 regla 2.
                    if not beta or _seq_anulable(beta, anulables):
                        if not follow[a] <= follow[b]:
                            follow[b] |= follow[a]
                            cambio = True
    # ε nunca pertenece a un SIGUIENTES (diapo 15). Blindaje:
    for nt in follow:
        follow[nt].discard(EPS)
    return follow


def calcular_predict(gramatica, first, follow):
    """Devuelve lista de (nt, indice, alfa, first_alfa, pred). Diapo 17."""
    term, _ = _terminales_no_terminales(gramatica)
    filas = []
    for nt, alts in gramatica.items():
        for i, alt in enumerate(alts):
            fa = _first_seq(alt, first, term)
            if EPS not in fa:
                pred = set(fa)
            else:
                pred = (fa - {EPS}) | follow[nt]
            filas.append((nt, i, alt, fa, pred))
    return filas


def construir_tabla(gramatica, predict_rows):
    """M[(nt, terminal)] = lista de indices de produccion. Conflicto si > 1."""
    tabla = {}
    for nt, i, _alt, _fa, pred in predict_rows:
        for a in pred:
            tabla.setdefault((nt, a), []).append(i)
    return tabla


def conflictos(tabla):
    return {k: v for k, v in tabla.items() if len(v) > 1}


def es_ll1(tabla):
    return not conflictos(tabla)


def _ord_key(s):
    # $ al final, ε primero si apareciera; resto alfabetico.
    if s == END:
        return (1, s)
    return (0, s)


def fmt_conj(c):
    return "{" + ", ".join(sorted(c, key=_ord_key)) + "}"


def fmt_alt(alt):
    return " ".join(alt)
