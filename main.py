from diaries.DiarySample import DiarySample
from diaries.shimuraDiaryNew import shimuraDiaryNew
from diaries.Suzuki_Diary import Suzuki_Diary

diaries = [DiarySample(), shimuraDiaryNew(), Suzuki_Diary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()