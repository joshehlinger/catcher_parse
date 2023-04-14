import re

import PyPDF2


REGEX = r'([A-z][^.!?]*[.!?]*"?)'

def clean_text(datum):
    text = datum.replace('D.B.', 'DB').replace('t.b.', 'tb')\
        .replace('Mrs.', 'Mrs').replace('Mr.', 'Mr')
    return text

def clean_sentence(datum):
    sentence = datum.strip().replace('\n', '').replace('"', '')\
        .replace(',', '').replace('.', '').replace("'", '').replace('?', '')\
        .replace('!', '').replace('--', ' ')
    return sentence

def main():
    reader = PyPDF2.PdfReader('./catcher_text.pdf')

    file = open('catcher_output.txt', 'w')

    for page in reader.pages:
        text = page.extract_text()
        text = clean_text(text)
        for sentence in re.findall(REGEX, text):
            sentence = clean_sentence(sentence)
            if sentence:
                file.write(sentence + '\n')

    file.close()

if __name__ == '__main__':
    main()