import unittest
from unittest.mock import MagicMock
from consumption_app.usecases.get_consumption_between import GetConsumptionBetween
from consumption_app.infrastructure.models.energy import Energy
from datetime import datetime

class TestGetConsumptionBetween(unittest.TestCase):

    def test_execute_raise_error_start_bigger_end(self):
        with self.assertRaises(ValueError):
            mock_repo = MagicMock()

            start = datetime.fromisoformat("2025-01-06T08:00")
            end = datetime.fromisoformat("2025-01-06T07:00")

            mock_repo.get_between.return_value = [
                Energy(date=start, consumption=40000),
                Energy(date=end, consumption=42000)
            ]

            usecase = GetConsumptionBetween(repository=mock_repo)

            result = usecase.execute(start,end)
            mock_repo.get_between.assert_called_once()

    def test_execute_returns_expected_data(self):
        mock_repo = MagicMock()

        start = datetime.fromisoformat("2025-01-06T06:00")
        end = datetime.fromisoformat("2025-01-06T07:00")

        mock_repo.get_between.return_value = [
            Energy(date=start, consumption=40000),
            Energy(date=end, consumption=42000)
        ]

        usecase = GetConsumptionBetween(repository=mock_repo)

        result = usecase.execute(start,end)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['consumption'], 40000000000)
        self.assertEqual(result[0]['date'], start.isoformat())
        mock_repo.get_between.assert_called_once()

