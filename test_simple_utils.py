import unittest

from simple_utils import celsius_to_fahrenheit, count_words, reverse_string


class ReverseStringTests(unittest.TestCase):
    def test_reverses_simple_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverses_sentence_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_empty_string_returns_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome_returns_same_string(self):
        self.assertEqual(reverse_string("level"), "level")

    def test_string_with_punctuation_and_numbers(self):
        self.assertEqual(reverse_string("abc123!"), "!321cba")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("héllo"), "olléh")


class CountWordsTests(unittest.TestCase):
    def test_counts_words_in_simple_sentence(self):
        self.assertEqual(count_words("hello world"), 2)

    def test_single_word(self):
        self.assertEqual(count_words("hello"), 1)

    def test_empty_string_has_zero_words(self):
        self.assertEqual(count_words(""), 0)

    def test_string_with_only_whitespace_has_zero_words(self):
        self.assertEqual(count_words("   "), 0)

    def test_extra_whitespace_between_words_is_ignored(self):
        self.assertEqual(count_words("hello    world  foo"), 3)

    def test_leading_and_trailing_whitespace_is_ignored(self):
        self.assertEqual(count_words("  hello world  "), 2)

    def test_counts_words_separated_by_newlines_and_tabs(self):
        self.assertEqual(count_words("hello\nworld\tfoo"), 3)


class CelsiusToFahrenheitTests(unittest.TestCase):
    def test_freezing_point_of_water(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_boiling_point_of_water(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_body_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6)

    def test_negative_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_fractional_celsius_value(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88)

    def test_accepts_integer_and_returns_numeric_type(self):
        result = celsius_to_fahrenheit(10)
        self.assertEqual(result, 50)
        self.assertIsInstance(result, float)


if __name__ == "__main__":
    unittest.main()