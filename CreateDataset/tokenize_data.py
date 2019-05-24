from nltk import sent_tokenize
import re

textFileName = 'nhaGiaKim'

# Read input file
with open(f'{textFileName}.txt', 'r', encoding='utf8') as f:
    data = f.read()

# Spliting paragraph
paragraphs = data.split('\n')


# Spliting sentence of each paragraph
paragraph_sentence_list = []
for paragraph in paragraphs:
    paragraph = paragraph.replace('\n', ' ')
    paragraph = paragraph.replace(' - ', '')
    paragraph = re.sub(r'[^a-zA-Z0123456789_.,?!:'
                       'áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệíìỉĩị'
                       'óòỏõọôốồổỗộơớờởỡợuúùủũụưứừửữựyýỳỷỹỵ'
                       'ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊ'
                       'ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢUÚÙỦŨỤƯỨỪỬỮỰYÝỲỶỸỴ ]',
                       '', paragraph)
    paragraph_sentence_list.append(sent_tokenize(paragraph))


# Proper format for Aeneas
text = ''
count = 0
for paragraph in paragraph_sentence_list:
    if 'Chương' in ' '.join(paragraph):
        if count != 0:
            with open(
                f'../TTS-fpt-api/textData/{textFileName}-aeneas-{count}.txt',
                'w', encoding='utf8'
            ) as fw:
                fw.write(text)
        text = ''
        count += 1
        text += '\n'.join(paragraph)
        text += '\n\n'
    else:
        text += '\n'.join(paragraph)
        text += '\n\n'
with open(f'../TTS-fpt-api/textData/{textFileName}-aeneas-{count}.txt',
          'w', encoding='utf8') as fw:
                fw.write(text)
