from Types import DataType
from AvarageMark import AvarageMark
import pytest

RatingsType = dict[str, float]


class TestCountSubjects:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Глухов Геннадий Сергеевич":
                [
                    ("математика", 95),
                    ("русский язык", 76),
                    ("программирование", 90),

                ],

            "Косов Михаил Владимирович":
                [
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ],

            "Зотов Степан Олегович":
                [
                    ("математика", 76),
                    ("русский язык", 100),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Глухов Геннадий Сергеевич": 2,
            "Косов Михаил Владимирович": 1,
            "Зотов Степан Олегович": 2
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating = AvarageMark(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = AvarageMark(input_data[0]).calc()
        for student in rating:
            rating_score = rating[student]
            assert rating_score == input_data[1][student]
