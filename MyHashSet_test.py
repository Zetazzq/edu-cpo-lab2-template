import unittest
from hypothesis import given, strategies
from MyHashSet import (MyHashSet, myHash, cons, remove, member, size, fromList,
                       toList, intersection, find, setFilter, setMap,
                       setReduce, empty, concat)


class TestMyHashSetMethods(unittest.TestCase):

    def test_init(self):
        hashset = MyHashSet()
        self.assertEqual(hashset.length, 61)

    def test_hash(self):
        hashset = MyHashSet()
        hash_value = myHash(hashset, 63)
        self.assertEqual(hash_value, 2)

    def test_add(self):
        a = MyHashSet()
        b = cons(a, 36)
        self.assertEqual(member(a, 36), False)
        self.assertEqual(member(b, 36), True)

    def test_remove(self):
        hashset = fromList([1, 2, 5])
        self.assertEqual(toList(remove(hashset, 2)), [1, 5])
        self.assertEqual(toList(hashset), [1, 2, 5])

    def test_fromList(self):
        a = fromList([1, 2, 3])
        b = cons(a, 1)
        b = cons(b, 2)
        b = cons(b, 3)
        self.assertEqual(a, b)

    def test_str(self):
        a = fromList([2, 3, 1])
        b = fromList([1, 2, 3])
        c = empty()
        self.assertEqual(str(a), "{1, 2, 3}")
        self.assertEqual(str(b), "{1, 2, 3}")
        self.assertEqual(str(c), "{}")

    def test_size(self):
        a = empty()
        self.assertEqual(size(a), 0)
        b = concat(a, fromList([36, 48]))
        self.assertEqual(size(b), 2)

    def test_toList(self):
        a = fromList([4, 2, 3, 1])
        self.assertEqual(toList(a), [1, 2, 3, 4])

    def test_find(self):
        hashset = fromList([2, 3, 1, 4])
        self.assertEqual(
            find(hashset, lambda x: x % 2 == 1), [1, 3])

    def test_filter(self):
        hashset = fromList([2, 3, 1, 4])
        self.assertEqual(
            toList(setFilter(hashset, lambda x: x % 2 == 0)), [2, 4])

    def test_intersection(self):
        a = fromList([1, 2, 5, 7, 8])
        b = fromList([3, 6, 2, 5, 8])
        self.assertEqual(toList(intersection(a, b)), [2, 5, 8])

    def test_map(self):
        a = fromList([2, 3, 1])
        b = setMap(a, lambda x: x ** 3)
        self.assertEqual(toList(b), [1, 8, 27])

    def test_reduce(self):
        a = empty()
        self.assertEqual(setReduce(a, lambda x, y: x * y, 1), 1)
        b = concat(a, fromList([6, 9]))
        self.assertEqual(setReduce(b, lambda x, y: x * y, 1), 54)

    def test_iter(self):
        x = [1, 2, 3]
        hashset = fromList(x)
        tmp = []
        for e in hashset:
            tmp.append(e.value)
        tmp.sort()
        self.assertEqual(x, tmp)
        self.assertEqual(toList(hashset), tmp)
        i = iter(MyHashSet())
        self.assertRaises(StopIteration, lambda: next(i))

    @given(a=strategies.lists(strategies.integers()),
           b=strategies.lists(strategies.integers()),
           c=strategies.lists(strategies.integers()))
    def test_associativity(self, a, b, c):
        A = fromList(a)
        B = fromList(b)
        C = fromList(c)
        self.assertEqual(concat(A, concat(B, C)), concat(concat(A, B), C))

    @given(_list=strategies.lists(strategies.integers()))
    def test_empty(self, _list):
        a = fromList(_list)
        self.assertEqual(concat(a, empty()), a)
        self.assertEqual(concat(empty(), a), a)


if __name__ == '__main__':
    unittest.main(verbosity=2)
