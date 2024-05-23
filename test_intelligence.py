import unittest
from src.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    def test_easy_decision(self):
        intelligence = Intelligence(level='easy')
        decision1 = intelligence.make_decision(10)
        decision2 = intelligence.make_decision(20)
        decision3 = intelligence.make_decision(30)
        self.assertEqual(decision1, 'roll')
        self.assertEqual(decision2, 'hold')
        self.assertEqual(decision3, 'hold')

    def test_medium_decision(self):
        intelligence = Intelligence(level='medium')
        decision1 = intelligence.make_decision(15)
        decision2 = intelligence.make_decision(25)
        decision3 = intelligence.make_decision(35)
        self.assertEqual(decision1, 'roll')
        self.assertEqual(decision2, 'hold')
        self.assertEqual(decision3, 'hold')

    def test_hard_decision(self):
        intelligence = Intelligence(level='hard')
        decision1 = intelligence.make_decision(20)
        decision2 = intelligence.make_decision(30)
        decision3 = intelligence.make_decision(40)
        self.assertEqual(decision1, 'roll')
        self.assertEqual(decision2, 'hold')
        self.assertEqual(decision3, 'hold')


if __name__ == '__main__':
    unittest.main()