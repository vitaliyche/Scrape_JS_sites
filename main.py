# Subscribe https://www.youtube.com/@pythontempter

from requests_html import HTMLSession

session = HTMLSession()
url = 'https://www.youtube.com/@pythontempter'

html = session.get(url).html

html.render(scrolldown=True, sleep=1, keep_page=True)

videos = html.find('#video-title')

for item in videos:
    video = {
        'title': item.text,
        'link': item.absolute_links
    }
    print(video)
