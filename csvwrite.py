test = [
    {"url":"zooplus.fr","id":"23"},
    {"url":"zooplus.de","id":"24"},
    {"url":"zooplus.no","id":"13"},
    {"url":"zooplus.pl","id":"3"},
]


class Csv:
    def __init__(self,pairs):
        f = open("results.csv", 'a')
        for pair in pairs:
            print(pair["url"])
            print(pair["id"])
            f.write(pair["url"]+","+pair["id"]+","+pair["title"]+"\n")


# Csv(test)