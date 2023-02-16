class PyBundler(object):
    """Classe du constructeur du projet .py à partir du projet .pycrea"""
    def __init__(self, data=None, file=None):
        "constructeur de la classe Bundler(). Arguments : data : les données et file, le fichier. Si il y a un fichier, il sera convertit en data."
        if data == None and not(file == None):
            with open(file, "r") as f:
                self.data = f.read()
        elif not(data == None) and file == None:
            self.data = data
        else:
            try:
                raise Exception
            except Exception as e:
                raise RuntimeError("Il faut au min et max un argument entre file et data !") from e