from diaries.DiarySample import DiarySample
from diaries.TakataDiary import TakataDiary

diaries = [DiarySample(),TakataDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()