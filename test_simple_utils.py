"""Unit tests for simple_utils.py"""

import pytest

from simple_utils import celsius_to_fahrenheit, count_words, reverse_string


class TestReverseString:
    def test_reverses_basic_word(self):
        assert reverse_string("hello") == "olleh"

    def test_reverses_sentence_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"

    def test_empty_string_returns_empty(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("a") == "a"

    def test_palindrome_is_unchanged(self):
        assert reverse_string("racecar") == "racecar"

    def test_reversing_twice_returns_original(self):
        text = "Reversal Test 123"
        assert reverse_string(reverse_string(text)) == text

    def test_string_with_special_characters(self):
        assert reverse_string("a1! b2@") == "2b !1a"

    def test_string_with_unicode_characters(self):
        assert reverse_string("héllo") == "olléh"

    def test_string_with_only_whitespace(self):
        assert reverse_string("   ") == "   "

    def test_string_with_newline_characters(self):
        assert reverse_string("line1\nline2") == "2enil\n1enil"

    def test_non_string_input_raises_type_error(self):
        with pytest.raises(TypeError):
            reverse_string(None)


class TestCountWords:
    def test_counts_words_in_normal_sentence(self):
        assert count_words("The quick brown fox") == 4

    def test_single_word(self):
        assert count_words("hello") == 1

    def test_empty_string_has_zero_words(self):
        assert count_words("") == 0

    def test_whitespace_only_string_has_zero_words(self):
        assert count_words("   ") == 0

    def test_multiple_spaces_between_words_are_collapsed(self):
        assert count_words("hello    world") == 2

    def test_leading_and_trailing_whitespace_ignored(self):
        assert count_words("  hello world  ") == 2

    def test_counts_words_separated_by_tabs_and_newlines(self):
        assert count_words("hello\tworld\nfoo") == 3

    def test_sentence_with_punctuation_counts_tokens(self):
        assert count_words("Hello, world!") == 2

    def test_return_type_is_int(self):
        assert isinstance(count_words("hello world"), int)

    def test_non_string_input_raises_attribute_error(self):
        with pytest.raises(AttributeError):
            count_words(None)


class TestCelsiusToFahrenheit:
    def test_freezing_point_of_water(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_boiling_point_of_water(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_negative_temperature(self):
        assert celsius_to_fahrenheit(-40) == -40

    def test_body_temperature_approx(self):
        assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

    def test_float_input(self):
        assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)

    def test_zero_kelvin_offset_like_extreme_negative(self):
        assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)

    def test_large_positive_value(self):
        assert celsius_to_fahrenheit(1000) == pytest.approx(1832.0)

    def test_non_numeric_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit("abc")