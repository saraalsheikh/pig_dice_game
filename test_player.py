import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player("Alice")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.score, 0)

    def test_set_name(self):
        player = Player("Alice")
        player.set_name("Bob")
        self.assertEqual(player.name, "Bob")

    def test_add_score(self):
        player = Player("Alice")
        player.add_score(10)
        self.assertEqual(player.score, 10)

    def test_reset_score(self):
        player = Player("Alice")
        player.add_score(10)
        player.reset_score()
        self.assertEqual(player.score, 0)

    def test_get_name(self):
        player = Player("Alice")
        self.assertEqual(player.get_name(), "Alice")

    def test_get_score(self):
        player = Player("Alice")
        player.add_score(15)
        self.assertEqual(player.get_score(), 15)

if __name__ == "__main__":
    unittest.main()