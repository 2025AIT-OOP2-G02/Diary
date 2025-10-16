from diaries.DiarySample import DiarySample
from diaries.nakamotoDiary import nakamotoDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    nakamotoDiary(),
]
for d in diaries:   
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
