j = [
    {1234:"1234",
     1234:"1234"}
]

set_of_dicts = set(frozenset(d.items()) for d in j)

print(len(set_of_dicts))