# Scrapy - Google Covid News 🚀

Scrapy to https://news.google.com/covid19/map and export in JSON file

## Comenzando 

Fork this project and in turn check the `mt-scrapy` branch, which contains the source code.

### Pre-requisitos 📋

You need install and use:

```
Python3
pip3
```

### Instalación 🔧

In the branch `mt-scrapy`, Install the requirements:

```
python3 -m venv venv
pip3 install -r requirements.txt
```

Execute the env, open the folder `gcovid` and run the scrapy

```
source venv/bin/activate
cd gcovid
rm dist/response.json | scrapy crawl spider_google
```

After that, you generate the next response in the path `dist/response.json`:

```json
{
    "header": {
        "title": "Worldwide",
        "date": "2020-08-02T16:02:18Z",
        "values": [
            { "title": "Confirmed", "value": 17859793 },
            { "title": "Recovered", "value": 10564263 },
            { "title": "Deaths", "value": 685179 }
        ]
    },
    "content": [
        {
            "confirmed": 17859793,
            "newCases": 2297,
            "recovered": 10564263,
            "deaths": 685179,
            "country": "Worldwide",
            "code": "ALL",
            "tempCountry": "Worldwide"
        },
        {
            "confirmed": 4705403,
            "newCases": 14278,
            "recovered": 2301821,
            "deaths": 156744,
            "country": "United States",
            "code": "US",
            "tempCountry": "United States"
        }
    ],
}
```

## Despliegue 📦

1. Login in https://scrapinghub.com
2. In the dashboard, press the button **Create Project**
3. Write a name of the project: `scrapy-google-covid` and press the button **Create**
4. Srapinghub, give you the steps and the credentials like that:
```shell script
$ pip install shub
$ shub login
API key: dd7c837f14c947c7a39ce7baae339bcd
$ shub deploy 466670
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (MIT) - mira el archivo [LICENSE.md](LICENSE.md) para detalles


---
⌨️ con ❤️ por [Supermavster](https://github.com/Supeprmavster) 😉
