from diaries.AbstractDiary import AbstractDiary


class Suzuki_Diary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "なにもない一日だった"

    def get_author(self):
        return "鈴木巧"