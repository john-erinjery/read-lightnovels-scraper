#!C:\Programing\python-web\env\Scripts\python.exe
import bs4
from pickle import dump
from fpdf import FPDF
import requests
import codecs
import os
soup = bs4.BeautifulSoup(open('body.html', mode='r', encoding='utf-8'), 'xml')
pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size = 13)

def extract_links_from_body() -> dict:
    soup = bs4.BeautifulSoup(open('body.html', mode='r', encoding='utf-8'), 'xml')
    global n
    link_dict = {}
    for i in soup.find_all('a'):
        if i.parent.parent.name == 'ul':
            if i.parent.parent['class'] == 'list-chapter':
                for j in i.children:
                    if j.name == 'span':
                        if j.has_attr('class'):
                            if j['class'] == 'chapter-text':
                                text = j.text
                                n = ''
                                for k in text.split()[1]:
                                    if k.isdigit():
                                        n += k
                                link_dict[int(n)] = i['href']
    return link_dict

def create_links_dat():
    link_dict = extract_links_from_body()
    with open('chapter_links.dat', 'wb') as f:
        dump(link_dict, f)

def split_at_words_(line, num):
    splitted_line = line.split()
    line_list = []
    temp_line = ''
    count = 0
    if len(line) <= num:
        return [line]
    ns = 0
    ne = 0
    indexes = []
    for i in splitted_line:
        count += len(i) + 1
        ne += 1
        if count >= num:
            indexes.append([ns, ne])
            ns = ne
            count = len(i)
        else:
            pass
    for i in indexes:
        for j in splitted_line[i[0]:i[1]]:
            temp_line += j + ' '
        line_list.append(temp_line)
        temp_line = ''
    for i in splitted_line[ns:]:
        temp_line += i + ' '
    line_list.append(temp_line)
    return line_list

def download_chapter_with_url(_url):
    r = requests.get(url=_url, stream=True)
    r.encoding = 'UTF-8'
    soup = bs4.BeautifulSoup(r.content, 'xml')
    decoded_data = codecs.decode(soup.prettify('UTF-8'), 'UTF-8').replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"').replace('…', '...').replace('–', '-').replace('―', '-').replace('　', ' ')
    soup_2 = bs4.BeautifulSoup(decoded_data, 'xml')
    return soup_2
    

def get_chapter_content(markup):
    div = markup.find(name='div', attrs={'class' : 'chapter-content'})
    if os.path.exists('content.txt'):
        pass
    else:
        open('content.txt', 'w')
    with open('content.txt', 'a') as f:
        for i in div.children:
            if i.name == 'p':
                try:
                    f.write(str(i.get_text().strip()+ '\n'))
                except:
                    print('character error, ripping off one line. : ')
                    print(i.get_text(), '\n')


def text_to_pdf_converter(file, range_):
    for i in file:
        lines = split_at_words_(i, 100)
        for j in lines:
            pdf.cell(300, 7, txt=j, ln = 1, align = 'L')
    pdf.output(f"{range_[0]}-{range_[1]}.pdf")
