import bs4
file = open('main.html', mode='r', encoding='utf-8')
soup = bs4.BeautifulSoup(file,'xml')
chapter_link_dict = {}
lenght = len('https://readlightnovels.net/the-daily-life-of-the-immortal-king/chapter-')
for i in soup.find_all(tag='div'):
    print(i)
    if i.id == 'list-chapter':
        print(i)