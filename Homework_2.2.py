import json
import re

list_files = [('newsafr.json', 'utf-8'),
              ('newscy.json', 'koi8-r'),
              ('newsfr.json', 'iso-8859-5'),
              ('newsit.json', 'cp1251')
    ]


def get_dict(list_files):
    for json_file, coding_file in list_files:
        with open(json_file, 'r', encoding=coding_file) as f:
            data = json.load(f)
            words = {}
            for cdata in data['rss']['channel']['item']:
                if len(cdata['description']) > 1:
                    string_from_description = cdata['description']
                else:
                    string_from_description = cdata['description']['__cdata']

                for word in string_from_description.lower().split():
                    word = re.sub(r'\<[^>]*\>', '', word)
                    for _ in word:
                        word = word.strip("/")
                    if len(word) > 6:
                        words[word] = words.get(word, 0) + 1
        print_dict(json_file, words)


def print_dict(json_file, words):
    print('----------------{}----------------------'.format(json_file))
    for word in sorted(words, key=words.get, reverse=True)[:10]:
        print("Слово '{0}' встречается {1} раз".format(word, words[word]))
       

if __name__ == "__main__":
    get_dict(list_files)
