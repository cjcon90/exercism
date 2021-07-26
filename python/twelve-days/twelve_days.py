from typing import List

LYRICS = {
	1: ['first', "a Partridge in a Pear Tree."],
	2: ['second', "two Turtle Doves, "],
	3: ['third', "three French Hens, "],
    4: ['fourth', "four Calling Birds, "],
    5: ['fifth', "five Gold Rings, "],
    6: ['sixth', "six Geese-a-Laying, "],
    7: ['seventh', "seven Swans-a-Swimming, "],
    8: ['eighth', "eight Maids-a-Milking, "],
    9: ['ninth', "nine Ladies Dancing, "],
    10: ['tenth', "ten Lords-a-Leaping, "],
    11: ['eleventh', "eleven Pipers Piping, "],
    12: ['twelfth', "twelve Drummers Drumming, "]
}

def recite(start_verse: int, end_verse: int) -> List[str]:
    song = []
    while start_verse <= end_verse:
        verse = f"On the {LYRICS[start_verse][0]} day of Christmas my true love gave to me: "
        for i in range(start_verse, 0, -1):
            if i == 1 and start_verse > 1:
                verse += "and "
            verse += LYRICS[i][1]
        song.append(verse)
        start_verse += 1
    return song
