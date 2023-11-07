from urllib import request
from project import Project
import tomlkit

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        project_info = tomlkit.loads(content)

        name = project_info['tool']['poetry']['name']
        description = project_info['tool']['poetry']['description']

        license = project_info['tool']['poetry']['license']

        authors = project_info['tool']['poetry']['authors']

        dependencies= project_info['tool']['poetry']['dependencies']
        dependencies_names = [key for key in dependencies.keys()]

        dev_dependencies = project_info['tool']['poetry']['group']['dev']['dependencies']
        dev_dependencies_names = [key for key in dev_dependencies.keys()]

        project = Project(name, description, license, authors, dependencies_names, dev_dependencies_names)

        return project
        
