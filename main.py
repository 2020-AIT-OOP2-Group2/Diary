from diaries.DiarySample import DiarySample
from diaries.TakataDiary import TakataDiary
from diaries.FukudaDiary import FukudaDiary
from diaries.shimuraDiaryNew import shimuraDiaryNew
from diaries.Suzuki_Diary import Suzuki_Diary
from diaries.MasakiDiary import MasakiDiary
from diaries.YamamuraDiary import YamamuraDiary

diaries = [
    DiarySample(),
    YamamuraDiary(),
  　shimuraDiaryNew(),
    FukudaDiary(),
    TakataDiary(),
    MasakiDiary(),
    Suzuki_Diary(),
    ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
