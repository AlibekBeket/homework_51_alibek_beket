from random import randint

from cat_web.json_file import *


class CatAction:
    def __init__(self, file_path: str, request):
        self.file_path = file_path
        self.request = request

    def new_cat(self):
        file_check(self.file_path)
        if file_read(self.file_path) == {} or self.request.POST.get('cat_name'):
            cat_status = {
                'cat_name': self.request.POST.get('cat_name'),
                'cat_age': 1,
                'cat_happiness_level': 10,
                'cat_satiety_level': 40,
                'cat_status': 'awake'
            }
            file_update(self.file_path, cat_status)

    def cat_action(self):
        cat_status = file_read(self.file_path)
        request = self.request
        if cat_status.get('cat_status') == 'sleeping':
            if request.POST.get('action_cat'):
                if request.POST.get('action_cat') == 'play':
                    cat_status['cat_happiness_level'] -= 5
                    cat_status['cat_status'] = 'awake'
        elif cat_status.get('cat_status') == 'awake':
            if request.POST.get('action_cat'):
                if request.POST.get('action_cat') == 'play':
                    if randint(1, 3) < 3:
                        cat_status['cat_happiness_level'] += 15
                        cat_status['cat_satiety_level'] -= 10
                    else:
                        cat_status['cat_happiness_level'] = 0
                elif request.POST.get('action_cat') == 'feed':
                    cat_status['cat_happiness_level'] += 5
                    cat_status['cat_satiety_level'] += 15
                elif request.POST.get('action_cat') == 'sleep':
                    cat_status['cat_status'] = 'sleeping'
        file_update('static/cat_status.json', cat_status)

    def cat_stats_check(self):
        cat_status = file_read(self.file_path)
        if cat_status.get('cat_happiness_level') < 0:
            cat_status['cat_happiness_level'] = 0
        if cat_status.get('cat_satiety_level') < 0:
            cat_status['cat_satiety_level'] = 0
        if cat_status.get('cat_happiness_level') > 100:
            cat_status['cat_happiness_level'] = 100
        if cat_status.get('cat_satiety_level') > 100:
            cat_status['cat_satiety_level'] = 100
            cat_status['cat_happiness_level'] -= 35
            if cat_status.get('cat_happiness_level') < 0:
                cat_status['cat_happiness_level'] = 0
        file_update('static/cat_status.json', cat_status)

    def return_cat_dict(self):
        return file_read(self.file_path)
