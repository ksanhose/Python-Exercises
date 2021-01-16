import textwrap


def get_mirrored_ascii_text(text, uppercase=True):
    if uppercase:
        text = text.upper()

    mirrored_chars = []
    
    for char in text:
        if 32 <= 128 - ord(char) <= 126:
            mirrored_chars.append(chr(128 - ord(char)))

    mirrored_ascii_text = ''.join(mirrored_chars[::-1])

    return mirrored_ascii_text


if __name__ == '__main__':
    text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
    industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it 
    to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, 
    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
    Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    '''

    mirrored_ascii_text = get_mirrored_ascii_text(text, uppercase=True)

    print('\n'.join(textwrap.wrap(mirrored_ascii_text, 64)))
