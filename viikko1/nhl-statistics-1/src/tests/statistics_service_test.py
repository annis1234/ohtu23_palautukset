import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.__str__(), "Semenko EDM 4 + 12 = 16")

    def test_search_player_not_found(self):
        player = self.stats.search("Koivu")
        self.assertEqual(player, None)

    def test_find_players_of_the_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(players[0].__str__(), "Semenko EDM 4 + 12 = 16")
        self.assertEqual(players[1].__str__(), "Kurri EDM 37 + 53 = 90")
        self.assertEqual(players[2].__str__(), "Gretzky EDM 35 + 89 = 124")

    def test_top_players_by_goals(self):
        top = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(top[0].__str__(), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(top[1].__str__(), "Yzerman DET 42 + 56 = 98")

    def test_top_players_by_assists(self):
        top = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(top[0].__str__(), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(top[1].__str__(), "Yzerman DET 42 + 56 = 98")

    def test_top_players_by_points(self):
        top = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(top[0].__str__(), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(top[1].__str__(), "Lemieux PIT 45 + 54 = 99")

    def test_top_players(self):
        top = self.stats.top(2)
        self.assertEqual(top[0].__str__(), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(top[1].__str__(), "Lemieux PIT 45 + 54 = 99")

        