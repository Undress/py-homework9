import json
import xml.etree.ElementTree as ET




def main():

    words_json = parse_json('newsafr.json')
    words_xml = parse_xml('newsafr.xml')

    print(search_top(words_json))
    print(search_top(words_xml))


def parse_xml(xml_file):

    words = []

    news = ET.parse(xml_file)

    articles = news.findall('channel/item/description')

    for article in articles:
        for word in article.text.split(" "):
            words.append(word)

    return words


def parse_json(json_file):

    words = []

    with open(json_file) as file:
        news = json.load(file)

    for article in news["rss"]["channel"]["items"]:
        for word in article["description"].split(" "):
            words.append(word)

    return words



def search_top(words):

    final_words = []
    final_dict = {}

    for word in words:
        if len(word) > 6:
            final_words.append(word)

    for word in final_words:
        if not(word in final_dict):
            final_dict.update({word : 1})
        else:
            final_dict[word] += 1

    result = sorted(final_dict.items(), key=lambda x:x[1], reverse=True)[:10]

    return result



if __name__ == '__main__':
    main()