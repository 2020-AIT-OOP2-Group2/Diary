from diaries.DiarySample import DiarySample
from diaries.YamamuraDiary import YamamuraDiary

diaries = [
    DiarySample(),
    YamamuraDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()