def text_formatting(text: str, width: int, style: str) -> str:

    lines = []
    line = ''
    for word in text.split():
        if len(line) + len(word) <= width:
            line += word + ' '
        else:
            lines.append(line.rstrip())
            line = word + ' '
    lines.append(line.rstrip())

    def justify(line, width):

        words = line.split()
        fill = width - sum(len(word) for word in words)
        spaces = len(words) - 1
        if not spaces:
            return line
        nspace, wspace_count = divmod(fill, spaces)
        space = ' ' * nspace
        wspace = space + ' '
        return space.join(words).replace(space, wspace, wspace_count)

    result = []

    for line in lines:
        if style == 'c':
            line = line.center(width)
            result.append(line.rstrip())
        elif style == 'r':
            line = line.rjust(width)
            result.append(line.rstrip())
        elif style == 'l':
            result.append(line.rstrip())
        elif style == 'j':
            result.append(justify(line, width))

    if style == 'j':
        last = result.pop()
        result.append(' '.join(last.split()))

    return '\n'.join(result)


if __name__ == '__main__':
    LINE = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure '
            'harum suscipit aperiam aliquam ad, perferendis ex molestias '
            'reiciendis accusantium quos, tempore sunt quod veniam, eveniet '
            'et necessitatibus mollitia. Quasi, culpa.')

    print('Example:')
    print(text_formatting(LINE, 38, 'l'))

    assert text_formatting(LINE, 38, 'l') == \
        '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa.''', 'Left 38'

    assert text_formatting(LINE, 30, 'c') == \
        ''' Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa.''', 'Center 30'

    assert text_formatting(LINE, 50, 'r') == \
        '''           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa.''', 'Right 50'

    assert text_formatting(LINE, 45, 'j') == \
        '''Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa.''', 'Justify 45'
