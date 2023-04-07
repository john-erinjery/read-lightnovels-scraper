import extractor
import os
from page import pagination
from math import ceil
ch_id = input('Enter Chapter ID : ')
range_ = eval(input('Enter range to download : '))
min_page = ceil(range_[0]/48)
max_page = ceil(range_[1]/48)
first_ch = range_[0]
pages = pagination(ch_id, [min_page, max_page])
start = (min_page - 1)*48 + 1
for i in pages:
    link_dict = extractor.extract_links_from_body(i['list_chap'], start=start)
    ch_r = []
    for j in list(link_dict.keys()):
        if int(j) >= first_ch and int(j) <= range_[1]:
            ch_r.append(j)
    for k in ch_r:
        print('downloading and processing chapter..', k)
        extractor.get_chapter_content(
            extractor.download_chapter_with_url(link_dict[str(k)]))
        first_ch += 1
    start += 48

print('\nconverting to PDF..')
extractor.text_to_pdf_converter(
    open('content.txt', 'r', encoding='utf-8', errors='ignore'), range_)
print('\ndeleting content.txt and cache..')
os.remove('content.txt')
print('done!')
