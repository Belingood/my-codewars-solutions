def is_balanced(source: str, caps: str) -> bool:

    caps_from_source: str = ''.join(filter(lambda x: x in caps, source))
    new_ln: int = 0

    while new_ln != len(caps_from_source):
        new_ln: int = len(caps_from_source)
        for i in range(0, len(caps), 2):
            caps_from_source: str = caps_from_source.replace(caps[i: i + 2], '')

    return False if new_ln else True




if __name__ == '__main__':
    print(is_balanced("(Sensei [says] yes!)", "()[]"))
    print(is_balanced("(Sensei [says) no!]", "()[]"))
