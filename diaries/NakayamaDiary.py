from diaries.AbstractDiary import AbstractDiary


class NakayamaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return """今日はいい天気でした.Gitの使い方を学びました.Gitをまともに使うのは高三以来だったので,思い出しながらになりましたが,なんとかついていけました.今後も使っていきたいです.
"""

    def get_author(self):
        return "Nakayama"
