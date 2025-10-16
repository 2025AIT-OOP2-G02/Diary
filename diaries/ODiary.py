from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):
    def get_date(self):
        return "2021-10-16"

    def get_summary(self):
        return "OOP2難しい"

    def get_author(self):
        return "oda"
