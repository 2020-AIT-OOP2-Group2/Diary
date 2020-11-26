from diaries.DiarySample import DiarySample
from diaries.TakataDiary import TakataDiary
from diaries.shimuraDiaryNew import shimuraDiaryNew

diaries = [DiarySample(),TakataDiary(), ]
diaries = [DiarySample(), shimuraDiaryNew(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()