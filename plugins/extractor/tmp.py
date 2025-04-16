from bs4 import BeautifulSoup





x = {"41854":{"title":"Steins;Gate Dublado","url":"https:\/\/goyabu.to\/anime\/steinsgate-dublado","img":"https:\/\/goyabu.to\/wp-content\/uploads\/2023\/08\/Steins-Gate-Dublado-Todos-os-Episodios-Online-Goyabu.jpg"},"26191":{"title":"Steins;Gate 0","url":"https:\/\/goyabu.to\/anime\/steinsgate-0","img":"https:\/\/goyabu.to\/wp-content\/uploads\/2023\/05\/steins-gate-0-todos-os-episodios-goyabu.jpg"},"26151":{"title":"Steins;Gate","url":"https:\/\/goyabu.to\/anime\/steinsgate","img":"https:\/\/goyabu.to\/wp-content\/uploads\/2023\/05\/steins-gate-todos-os-episodios-goyabu.jpg"}}

for i in x.items():
    name = i[1]['title']
    url = i[1]['url']

    
    print(name, url)
