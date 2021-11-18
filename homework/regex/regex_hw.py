import re
import urllib.request

webUrl = urllib.request.urlopen('http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83')

data = webUrl.read()
# print(data.decode('utf-8'))

answer = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)',str(data))
names = re.findall(r'(?<=\n)(.+)(\n)?(?=<b>)',str(data.decode('utf-8')))

new_names = []
for name in names:
    for el in name:
        string_to_append = ''
        for words in el.split():
            words = words.replace("<p>","")
            words = words.replace("</p>","")
            string_to_append += words + ' '
        new_names.append(string_to_append)

for elements in new_names:
    if elements == '':
        new_names.remove(elements)


dictionary = dict(zip(new_names,answer))
i = 1
for el in dictionary.keys():
    print(i,el,dictionary[el])
    i+=1



