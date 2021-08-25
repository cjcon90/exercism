from typing import List

LYRICS = ( 
    ['first', "a Partridge in a Pear Tree."],
    ['second', "two Turtle Doves, and "],
    ['third', "three French Hens, "],
    ['fourth', "four Calling Birds, "],
    ['fifth', "five Gold Rings, "],
    ['sixth', "six Geese-a-Laying, "],
    ['seventh', "seven Swans-a-Swimming, "],
    ['eighth', "eight Maids-a-Milking, "],
    ['ninth', "nine Ladies Dancing, "],
    ['tenth', "ten Lords-a-Leaping, "],
    ['eleventh', "eleven Pipers Piping, "],
    ['twelfth', "twelve Drummers Drumming, "]
)

def recite(start_day: int, end_day: int) -> List[str]:
    song = []
    while start_day <= end_day:
        verse = get_verse(start_day - 1)
        song.append(verse)
        start_day += 1
    return song

def get_verse(day: int) -> str:
    verse = f"On the {LYRICS[day][0]} day of Christmas my true love gave to me: "
    while day >= 0:
        verse += LYRICS[day][1]
        day -= 1
    return verse
