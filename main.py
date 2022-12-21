class field_object():
    def __init__(self, callable=False, other_obj=[], sym='?'):
        self._callable = callable
        self._other_obj = other_obj
        self.sym = sym

    def can_move(self, object_name):
        return self._callable ^ (not object_name in self._other_obj)

    def __str__(self):
        return self.sym

    def move(self, x, y):
        pass


class Wall(field_object):
    def __init__(self):
        super().__init__(True, [], '#')


class Space(field_object):
    def __init__(self):
        super().__init__(False, [], ' ')


class Player(field_object):
    def __init__(self):
        super().__init__(False, ['#', '@'], '@')


class Field:
    def __init__(self, name):
        with open(name, 'r') as f:
            mp = list(map(list, (f.read().split('\n'))))
        self._field = [[None for x in range(len(mp[0]))] for y in range(len(mp))]
        for y in range(len(self._field)):
            for x in range(len(self._field)):
                self._field[y][x] = ret_class(mp[y][x])

    def print(self):
        for y in self._field:
            print(''.join(map(str, y)))

    def __getitem__(self, key):
        return self._field[key[1]][key[0]]


def ret_class(sym):
    for x in (Wall(), Space()):
        if x.sym == sym:
            return x
    return field_object()


field = Field('1.txt')
field.print()
print(field[0, 0].can_move('@'))