def extraction(text: str, steps: list, start: int, back: bool) -> str:

    text = text[::-1][start:] if back else text[start:]
    result = text[0]

    for step in steps:
        try:
            result += text[step]
            text = text[step:]
        except IndexError:
            break

    return result
