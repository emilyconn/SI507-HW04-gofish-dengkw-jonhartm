import unittest
from go_fish import *

class TestCard(unittest.TestCase):
    def test_Init(self):
        # Invalid types in constructor
        with self.assertRaises(TypeError): Card(suit="Diamonds")
        with self.assertRaises(TypeError): Card(rank="Ace")
        # Suit out of range
        with self.assertRaises(IndexError): Card(suit=-1)
        with self.assertRaises(IndexError): Card(suit=12)
        # Rank out of range
        with self.assertRaises(IndexError): Card(rank=0)
        with self.assertRaises(IndexError): Card(rank=14)

    def test_String(self):
        self.assertEqual(str(Card(0,5)), "The 5 of Diamonds")
        self.assertEqual(str(Card(3,13)), "The King of Spades")

    def test_Equal(self):
        self.assertEqual(Card(2,5), Card(2,5))
        self.assertNotEqual(Card(2,5), Card(2,12))
        self.assertNotEqual(Card(2,5), Card(0,5))

unittest.main(verbosity=2)
