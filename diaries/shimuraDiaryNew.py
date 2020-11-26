from diaries.AbstractDiary import AbstractDiary


class shimuraDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "資料がなくて焦ってる"

    def get_author(self):
        return "Shimura"