import extractor
import os
link_dict = extractor.extract_links_from_body()
print(f'chapters {list(link_dict.keys())[0]} to {list(link_dict.keys())[-1]} detected.')
range_ = eval(input('\nenter range : '))

for i in range(range_[0], range_[1] + 1):
    print('\ndownloading and processing chapter..', i)
    extractor.get_chapter_content(extractor.download_chapter_with_url(link_dict[i]))
print('\nconverting to PDF..')
extractor.text_to_pdf_converter(open('content.txt', 'r', encoding='utf-8', errors='ignore'), range_)
print('\ndeleting content.txt and cache..')
os.remove('content.txt')
print('done!')