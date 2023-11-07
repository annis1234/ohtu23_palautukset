class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_lists(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:\n- {self._stringify_lists(self.authors)}"
            f"\n"
            f"\nDependencies:\n- {self._stringify_lists(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies:\n- {self._stringify_lists(self.dev_dependencies)}"
        )
