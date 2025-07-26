import re


def snake_case(song):
    new_song = ""
    song = song.lower()
    for char in song:
        if char == " ":
            new_song += "_"
        else:
            new_song += char
    return new_song

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def checker0(song, password):
    song = snake_case(song)
    if song not in password:
        return 0
    else:
        return 100

def checker1(password):
    if len(password) < 8 or len(password) > 50:
        return 1
    else:
        return 100

def checker2(password):
    pattern = r"\s"
    if match := re.search(pattern, password):
        return 2
    else:
        return 100

def checker3(password):
    pattern = r"[A-Z]+"
    if match := re.search(pattern, password):
        return 100
    else:
        return 3

def checker4(password):
    pattern1 = r"[AEIOU]+"
    pattern2 = r"[aeiou]+"
    match1 = re.search(pattern1, password)
    match2 = re.search(pattern2, password)

    if match1 and match2:
            return 100
    else:
        return 4

def checker5(password):
    pattern = r"\d"
    if match := re.search(pattern, password):
        return 100
    else:
        return 5

def checker6(password):
    pattern = r"\d+"
    match = re.findall(pattern, password)
    sum = 0

    for num in match:
        sum += int(num)

    if sum == 37:
        return 100
    else:
        return 6

def checker7(password):
    pattern = r"\W+"
    if match := re.search(pattern, password):
        return 100
    else:
        return 7

def checker8(password):
    pattern = r"[\./-]"
    match = re.findall(pattern, password)
    if len(match) >= 3:
        return 100
    else:
        return 8

def checker9(password):
    pattern = r"[IVXLCDM]+"
    if match := re.search(pattern, password):
        return 100
    else:
        return 9

def checker10(password):
    pattern = r"\d+"
    match = re.findall(pattern, password)

    catch = map(int, match)

    for num in catch:
        if is_prime(num):
            return 100
    return 10

def checker11(password):
    rainbow = r"(violet|indigo|blue|green|yellow|orange|red)"
    if match := re.search(rainbow, password, re.IGNORECASE):
        return 100
    else:
        return 11

def checker12(password):
    pattern = r"#([0-9A-F]{2}){3}"
    if match := re.search(pattern, password, re.IGNORECASE):
        return 100
    else:
        return 12

if __name__ == "__main__":
    print(checker12("#AABBHH"))