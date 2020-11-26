from diaries.AbstractDiary import AbstractDiary


class MasakiDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "優しい仲間でよかった"

    def get_author(self):
        return "Masaki"