from diaries.AbstractDiary import AbstractDiary


class TakataDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "とりあえずコメント"

    def get_author(self):
        return "Takata064"