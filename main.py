from diaries.DiarySample import DiarySample
from diaries.nakamotoDiary import nakamotoDiary
from diaries.NakayamaDiary import NakayamaDiary
from diaries.ODiary import DiarySample as DS
from diaries.K24012_Diary import K24012_Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    nakamotoDiary(),
    NakayamaDiary(),
    DS(),
    K24012_Diary(),
]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
