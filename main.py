from diaries.DiarySample import DiarySample
from diaries.FukudaDiary import FukudaDiary

diaries = [DiarySample(), FukudaDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
