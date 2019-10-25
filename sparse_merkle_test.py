from sparse_merkle import SparseMerkle
from unittest.mock import MagicMock

import unittest

class TestSparseMerkle(unittest.TestCase):
    def setUp(self):
        self.x = SparseMerkle()

        def side_effect(value):
            return str(value)
        
        self.x.get_hash = MagicMock(side_effect = side_effect)
        
    def test_get_height(self):
        self.assertEqual(self.x.get_height(2), 2)
        self.assertEqual(self.x.get_height(3), 2)
        self.assertEqual(self.x.get_height(9), 4)
    
    def test_get_concat(self):
        self.assertEqual(self.x.get_concat('1', '2'), '1-2')

    def test_get_null_proofs(self):
        expected = {}
        expected[1] = '0'
        expected[2] = '-'.join(['0' for i in range(2)])
        expected[3] = '-'.join(['0' for i in range(4)])
        expected[4] = '-'.join(['0' for i in range(8)])
        expected[5] = '-'.join(['0' for i in range(16)])
        expected[6] = '-'.join(['0' for i in range(32)])
        self.assertEqual(self.x.get_null_proofs(6), expected)

    def test_present(self):
        self.assertEqual(self.x.present(2, 4, [1]), True)
        self.assertEqual(self.x.present(1, 4, [7]), True)
        self.assertEqual(self.x.present(2, 4, [4, 5]), False)
        self.assertEqual(self.x.present(2, 4, [3, 5]), True)

    def test_find_root(self):
        null_proofs = self.x.get_null_proofs(4)
        self.assertEqual(self.x.find_root(1, 4, [], null_proofs),
                         '0-0-0-0-0-0-0-0')
        self.assertEqual(self.x.find_root(1, 4, [0], null_proofs),
                         '8-0-0-0-0-0-0-0')
        self.assertEqual(self.x.find_root(1, 4, [0, 4], null_proofs),
                         '8-0-0-0-12-0-0-0')
        self.assertEqual(self.x.find_root(1, 4, [0, 1, 2, 3, 4, 5, 6, 7], null_proofs),
                         '8-9-10-11-12-13-14-15')


if __name__ == '__main__':
    unittest.main()
