from diaries.AbstractDiary import AbstractDiary

class nakamotoDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "今日は雨が断続的に降っていた。しかも、大学に来るまでに電車が混んでいて精神的にも疲れた。心の底から雨の日に大学に行くのは嫌だと思った。バイトの日は暴風雨がいい。"

    def get_author(self):
        return "nakamoto"