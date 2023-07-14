import random

hype = {
    "col_1": [
        "Champ,",
        "Fact:",
        "Everybody says",
        "Dang...",
        "Check it:",
        "Just Saying...",
        "Superstar,",
        "Tiger,",
        "Self,",
        "Know this:",
        "News alert:",
        "Girl,",
        "Ace,",
        "Excuse me but",
        "Experts agree:",
        "In my opinion,",
        "Hear ye, hear ye:",
        "Okay, listen up:"
        ],
    "col_2": [
        "the mere idea of you",
        "your soul",
        "your hair today",
        "everything you do",
        "your personal style",
        "every thought you have",
        "that sparkle in your eye",
        "your presence here",
        "what you got going on",
        "the essential you",
        "your life's journey",
        "that saucy personality",
        "your DNA",
        "that brain of yours",
        "your choice of attire",
        "the way you roll",
        "whatever your secret is",
        "all of y'all"
    ],
    "col_3": [
        "has serious game,",
        "rains magic,",
        "deserves the Nobel Prize,",
        "raises the roof,",
        "breeds miracles,",
        "is paying off big time,",
        "shows mad skills,",
        "just shimmers,",
        "is a national treasure,",
        "gets the party hopping,",
        "is the next big thing,",
        "roars like a lion,",
        "is a rainbow factory,",
        "is made of diamonds,",
        "makes birds sing,",
        "should be taught in school,",
        "makes my world go 'round,",
        "is 100% legit,"
    ],
    "col_4": [
        "24/7.",
        "can I get an amen?",
        "and thats a fact.",
        "so treat yourself",
        "you feel me?",
        "that's just science.",
        "would I lie?",
        "for reals.",
        "mic drop.",
        "you hidden gem.",
        "snuggle bear.",
        "period.",
        "can I get an amen?",
        "now let's dance.",
        "high five.",
        "say it again!",
        "according to CNN.",
        "so get used to it."
    ]
}


def pick_random_segment(col_name):
    upper_limit=len(hype[col_name])-1
    lower_limit=0
    list_rand=random.randint(lower_limit,upper_limit)
    segment = hype[col_name][list_rand]
    return segment

def pep_talk_generator():
    phrase = ""
    for col_name in hype.keys():
        segment = pick_random_segment(col_name)
        phrase = phrase+" "+segment
    return phrase

if __name__=='__main__':
    print(pep_talk_generator())