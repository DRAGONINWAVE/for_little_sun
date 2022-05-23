from collections.abc import Sequence

def columnize(sequence:Sequence[str],num_columns:int = 0) -> list[tuple[str, ...]]:
    if num_columns == 0:
        num_columns = round(len(sequence)**.5)
    num_rows,reminder = divmod(len(sequence),num_columns)
    num_rows += bool(reminder)
    return [tuple(sequence[i::num_rows]) for i in range(num_rows)]

animals = 'drake fawn heron ibex koala lynx tahr xerus yak zapus'.split()
print(animals)
table = columnize(animals)
print(table)