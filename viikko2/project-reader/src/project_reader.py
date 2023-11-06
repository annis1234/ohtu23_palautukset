from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        dic = tomlkit.loads(content)
        print(dic)

        name = dic['tool']['poetry']['name']
        description = dic['tool']['poetry']['description']

        lic = dic['tool']['poetry']['license']

        authors = dic['tool']['poetry']['authors']

        dependencies = dic['tool']['poetry']['dependencies']
        keys_dep = [key for key in dependencies.keys()]

        dev_dependencies = dic['tool']['poetry']['group']['dev']['dependencies']
        keys_dev = [key for key in dev_dependencies.keys()]

        project = Project(name, description, lic, authors, keys_dep, keys_dev)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        return project
        
