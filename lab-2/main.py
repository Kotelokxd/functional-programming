import re
from collections import Counter
from typing import Optional


def petrov_split_words(text: str) -> list[str]:
    return re.findall(r"[^\W_]+", text.lower(), flags=re.UNICODE)


def petrov_count_word_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(petrov_split_words(text)))


def petrov_top_word(text: str) -> Optional[str]:
    return max(petrov_count_word_frequencies(text), key=lambda word: (petrov_count_word_frequencies(text)[word], word), default=None)

print("Разделенные слова:",
      petrov_split_words("Сегодня солнечный день. Сегодня тепло, а вечером будет прохладно"))
print("Частота слов:",
      petrov_count_word_frequencies("Сегодня солнечный день. Сегодня тепло, а вечером будет прохладно"))
print("Самое частое слово:",
      petrov_top_word("Сегодня солнечный день. Сегодня тепло, а вечером будет прохладно"))