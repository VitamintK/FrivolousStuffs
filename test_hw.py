def triple(triples, new_element):
    if len(triples[0]) < 3:
        triples[0].append(new_element)
        return triples
    else:
        new_triple = triples[-1][1:3] + [new_element]
        return triples + [new_triple]

def peaks(iterable):
    reduced = reduce(triple, iterable, [[]])#reduce produces a list of triples: note []
    filtered = filter(lambda x: max(x) == x[1], reduced) #filter out triples not representing peaks
    mapped = map(lambda x: x[1], filtered) #map triple to its middle value
    return list(mapped) #map is a generator; store its values in list
