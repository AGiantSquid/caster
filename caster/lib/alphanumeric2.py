from dragonfly import (Key, Text, Choice)

from caster.lib import settings


def get_alphabet_choice(spec):
    return Choice(spec,
                  {
                      "arch": "a",
                      "brov": "b",
                      "char": "c",
                      "dell": "d",
                      "etch": "e",
                      "fomp": "f",
                      "goof": "g",
                      "hark": "h",
                      "ice": "i",
                      "jinx": "j",
                      "koop": "k",
                      "lug": "l",
                      "mowsh | mouse": "m",
                      "nerb": "n",
                      "orks": "o",
                      "pooch": "p",
                      "quash": "q",
                      "rosh": "r",
                      "sook | souk": "s",
                      "teek": "t",
                      "unks": "u",
                      "verge": "v",
                      "womp": "w",
                      "trex": "x",
                      "yang": "y",
                      "zerb | Zerby": "z",
                  })


def word_number(wn):
    numbers_to_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    Text(numbers_to_words[int(wn)]).execute()


def numbers_list_1_to_9():
    result = ["one",
              "torque",
              "traio",
              "fairn",
              "faif",
              "six",
              "seven",
              "eigen",
              "nine"]
    if not settings.SETTINGS["miscellaneous"]["integer_remap_opt_in"]:
        result[1] = "two"
        result[2] = "three"
        result[3] = "four"
        result[4] = "five"
        result[7] = "eight"
    return result


def numbers_map_1_to_9():
    result = {}
    l = numbers_list_1_to_9()
    for i in range(0, len(l)):
        result[l[i]] = i + 1
    return result


def numbers2(wnKK):
    Text(str(wnKK)).execute()


def letters(big, dict1, dict2, letter):
    '''used with alphabet.txt'''
    d1 = str(dict1)
    if d1 != "":
        Text(d1).execute()
    if str(big) != "":
        Key("shift:down").execute()
    letter.execute()
    if str(big) != "":
        Key("shift:up").execute()
    d2 = str(dict2)
    if d2 != "":
        Text(d2).execute()

def modifiers(mod, letter):
    if str(mod) != "":
        Key(str(mod) + ":down").execute()
    Key(letter).execute()
    if str(mod) != "":
        Key(str(mod) + ":up").execute()
# Key("shift:up, ctrl:up, alt:up")

def letters2(sky, letter):
    if str(sky) != "":
        Key("shift:down").execute()
    Key(letter).execute()
    if str(sky) != "":
        Key("shift:up").execute()

def elite_text(text):
    elite_map = {"a": "@", "b": "|3", "c": "(", "d": "|)", "e": "3",
                 "f": "|=", "g": "6", "h": "]-[", "i": "|", "j": "_|",
                 "k": "|{", "l": "|_", "m": r"|\/|", "n": r"|\|", "o": "()",
                 "p": "|D", "q": "(,)", "r": "|2", "s": "$", "t": "']['",
                 "u": "|_|", "v": r"\/", "w": r"\/\/", "x": "}{", "y": "`/", "z": r"(\)"}
    text = str(text).lower()
    result = ""
    for c in text:
        if c in elite_map:
            result += elite_map[c]
        else:
            result += c
    Text(result).execute()
