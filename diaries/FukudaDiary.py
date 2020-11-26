from diaries.AbstractDiary import AbstractDiary


class FukudaDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "物理実験...おわらない..."

    def get_author(self):
        return "Fukuda"
