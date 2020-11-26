from diaries.DiarySample import DiarySample
from diaries.shimuraDiaryNew import shimuraDiaryNew
from diaries.MasakiDiary import MasakiDiary

diaries = [DiarySample(), shimuraDiaryNew(),MasakiDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()