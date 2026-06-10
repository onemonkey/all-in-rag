import importlib.util
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "code"
    / "C9"
    / "agent(代码系ai生成)"
    / "amount_normalizer.py"
)

spec = importlib.util.spec_from_file_location("amount_normalizer", MODULE_PATH)
amount_normalizer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(amount_normalizer)
AmountNormalizer = amount_normalizer.AmountNormalizer


def test_parse_numeric_amount_with_unit():
    normalizer = AmountNormalizer()

    assert normalizer.parse_amount_with_unit("300毫升") == ("300", "毫升", 300.0)


def test_parse_textual_amount_with_trailing_ingredient():
    normalizer = AmountNormalizer()

    assert normalizer.parse_amount_with_unit("一小勺盐") == ("1小勺", "盐", 3)
    assert normalizer.parse_amount_with_unit("适量盐") == ("适量", "盐", None)


def test_parse_textual_amount_without_trailing_ingredient():
    normalizer = AmountNormalizer()

    assert normalizer.parse_amount_with_unit("酌量") == ("适量", "", None)
    assert normalizer.parse_amount_with_unit("2-3滴") == ("几滴", "", 1)
