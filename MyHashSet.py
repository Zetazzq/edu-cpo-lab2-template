class Node(object):
    def __init__(self, key=None, value=None, _next=None):
        self.key = key
        self.value = value
        self.next = _next


class MyHashSet(object):
    init = object()

    def __init__(self, length=61):
        self.data = [self.init for _ in range(length)]
        self.length = length
        self.size = 0

    def toNodeList(self) -> list:
        nodelist = []
        for i in range(self.length):
            if isinstance(self.data[i], Node):
                point = self.data[i]
                while point is not None:
                    nodelist.append(point)
                    point = point.next
        return nodelist

    def __eq__(self, other) -> bool:
        if toList(self) == toList(other):
            return True
        return False

    def __iter__(self):
        iter_list = self.toNodeList()
        return iter(iter_list)

    def __str__(self):
        lst = toList(self)
        res = "{"
        if len(lst) != 0:
            res += str(lst[0])
        for i in lst[1:]:
            res += ", " + str(i)
        res += "}"
        return res


def add(mySet: MyHashSet, value: int) -> None:
    key = value
    hash_value = myHash(mySet, key)
    add_node = Node(key, value)
    if not isinstance(mySet.data[hash_value], Node):
        mySet.data[hash_value] = add_node
        mySet.size += 1
    else:
        head = mySet.data[hash_value]
        while head.next is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        if head.key == key:
            head.value = value
            return
        head.next = add_node
        mySet.size += 1


def setCopy(mySet: MyHashSet) -> MyHashSet:
    newSet = MyHashSet()
    newSet.length = mySet.length
    newSet.size = mySet.size
    newSet.data = [newSet.init for _ in range(newSet.length)]
    for i in range(len(newSet.data)):
        if mySet.data[i] != mySet.init:
            psrc = mySet.data[i]
            newSet.data[i] = Node(psrc.key, psrc.value, psrc.next)
            pdst = newSet.data[i]
            while psrc.next is not None:
                psrc = psrc.next
                pdst.next = Node(psrc.key, psrc.value, psrc.next)
                pdst = pdst.next
    return newSet


def myHash(mySet: MyHashSet, key: int) -> int:
    hash_value = key % mySet.length
    return hash_value


def cons(mySet: MyHashSet, value: int) -> MyHashSet:
    newSet = setCopy(mySet)
    if value is not None:
        add(newSet, value)
    return newSet


def remove(mySet: MyHashSet, value: int) -> MyHashSet:
    newSet = setCopy(mySet)
    hash_value = myHash(mySet, value)
    if not isinstance(newSet.data[hash_value], Node):
        return newSet
    elif newSet.data[hash_value].value is value:
        newSet.data[hash_value] = newSet.data[hash_value].next
        newSet.size -= 1
        return newSet
    p = newSet.data[hash_value]
    q = newSet.data[hash_value].next
    while q.next is not None:
        if q.value == value:
            p.next = q.next
            newSet.size -= 1
            return newSet
        p = q
        q = q.next
    if q.key == value:
        p.next = None
        newSet.size -= 1
    return newSet


def member(mySet: MyHashSet, value: int) -> bool:
    hash_value = myHash(mySet, value)
    p = mySet.data[hash_value]
    while isinstance(p, Node):
        if p.value == value:
            return True
        p = p.next
    return False


def size(mySet: MyHashSet) -> int:
    return mySet.size


def fromList(lst: list) -> MyHashSet:
    newSet = MyHashSet()
    for value in lst:
        add(newSet, value)
    return newSet


def toList(mySet: MyHashSet) -> list:
    lst = []
    for i in range(mySet.length):
        if isinstance(mySet.data[i], Node):
            head = mySet.data[i]
            while head is not None:
                lst.append(head.value)
                head = head.next
    lst.sort()
    return lst


def intersection(set1: MyHashSet, set2: MyHashSet) -> MyHashSet:
    lst1 = toList(set1)
    lst2 = toList(set2)
    lst = [value for value in lst1 if value in lst2]
    return fromList(lst)


def find(mySet: MyHashSet, func) -> list:
    lstS = toList(mySet)
    lstD = [value for value in lstS if func(value) is True]
    lstD.sort()
    return lstD


def setFilter(mySet: MyHashSet, func) -> MyHashSet:
    lst = find(mySet, func)
    return fromList(lst)


def setMap(mySet: MyHashSet, func) -> MyHashSet:
    list_src = toList(mySet)
    for i in range(len(list_src)):
        list_src[i] = func(list_src[i])
    return fromList(list_src)


def setReduce(mySet: MyHashSet, func, init_state: int) -> int:
    res = init_state
    it = iter(mySet)
    for i in it:
        res = func(res, i.value)
    return res


def empty() -> MyHashSet:
    return MyHashSet()


def concat(set1: MyHashSet, set2: MyHashSet) -> MyHashSet:
    newSet = setCopy(set1)
    for value in toList(set2):
        add(newSet, value)
    return newSet
