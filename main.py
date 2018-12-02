import  json

def main():
    with open("newsafr.json") as file:
        x = json.load(file)

    y = []

    for news in x["rss"]["channel"]["items"]:
        y.append(news["description"])

    print(y)


if __name__ == '__main__':
    main()