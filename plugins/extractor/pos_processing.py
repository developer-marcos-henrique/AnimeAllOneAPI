from bs4 import BeautifulSoup
import json

class filters:
    def __init__(self, data):
        self.data = data
        # self.websites_html_method = {
        #     "9animetv": {"selector": 'h3[class="film-name"] a' "content": "text", "href"},
        #     "aniwatch": {"selector": 'a[class="nav-item"]' ("href")), ('h3[class="film-name"]', ('text')))),
        #     "animesbr": {"selector": 'div[class="datails"]', "content": ["text", "href"]}
            
        # }

        
        self.websites_list_method = (
            ("animefire", "LIST", (0, 5))
        )

        self.websites_json_method = ("goyabu")

        

    def process(self):

        for x in self.data:
            print(x[0])
            match x[0]:
                case "9animetv":
                    html = BeautifulSoup(x[1], "html.parser").select("div[id='main-content']  h3.film-name a")

                    for content in html:
                        name = content.get_text()
                        url = content['href']

                        
                        print(x[0], name, url)

                case "aniwatch":
                    html = BeautifulSoup(x[1]['html'], "html.parser").select("a")

                    for content in html:
                        url = content['href']
                        name = content.select_one("h3.dynamic-name")
                        
                        if name:
                            name = name.get_text()
                        
                        print(x[0], name, url)


                case "animefire":
                    for content in x[1]:
                        url = content[5]
                        name = content[0]
                        
                        print(x[0], name, url)

                            


                case "animesbr":
                    html = BeautifulSoup(x[1], "html.parser").select("div.search-page div.result-item article div.details a")

                    for i in html:
                        name = i.get_text()
                        url = i['href']

                        
                        print(x[0], name, url)

                case "goyabu":
                    if "error" in x[1].keys():
                        continue
                    
                    for i in x[1].items():
                        name = i[1]['title']
                        url = i[1]['url']
                        
                        
                        print(x[0], name, url)
