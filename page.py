import requests
from time import sleep
ajax_url = "https://readlightnovels.net/wp-admin/admin-ajax.php"


def pagination(ch_id, page_range):
    html_list = []
    for page in range(page_range[0], page_range[1] + 1):
        data = {'action': 'tw_ajax', 'type': 'pagination',
                'id': ch_id, 'page': str(page)}
        r = requests.post(ajax_url, data=data)
        html_list.append((r.json()))
    sleep(0.5)
    return html_list
