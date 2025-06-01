def character_counter(s: str):
    if not isinstance(s, str):
        raise TypeError("Type should be str")
    data = dict()
    for i in range(len(s)):
        if data.__contains__(s[i]):
            data[s[i]] += 1
        else:
            data[s[i]] = 1

    count = 0
    for key, value in data.items():
        if value > 1:
            count += 1
    return count

