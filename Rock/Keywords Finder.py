def checkio(text: str, words: str) -> str:

    temp = ''
    for word in sorted(words.split(), key=len, reverse=True):
        for text_word in text.split():
            if word.lower() in text_word.lower() and 'span' not in text_word:
                st = text_word.lower().find(word.lower())
                end = st + len(word)
                temp += text_word[:st]+'<span>'+text_word[st:end] +'</span>'+text_word[end:] + ' '
            else:
                temp += text_word + ' '
        text = temp
        temp = ''
    print(text.strip())


checkio("This is only a text example for task example.",
        "example") == "This is only a text <span>example</span> for task <span>example</span>."
checkio("Python is a widely used high-level programming language.",
        "pyThoN") == "<span>Python</span> is a widely used high-level programming language."
checkio("It is experiment for control groups with similar distributions.",
        "is im") == "It <span>is</span> exper<span>im</span>ent for control groups with s<span>im</span>ilar d<span>is</span>tributions."
checkio("The National Aeronautics and Space Administration (NASA).",
        "nasa  THE") == "<span>The</span> National Aeronautics and Space Administration (<span>NASA</span>)."
checkio("Did you find anything?", "word space tree") == "Did you find anything?"
checkio("Hello World! Or LOL", "hell world or lo") == "<span>Hello</span> <span>World</span>! <span>Or</span> <span>LO</span>L"
