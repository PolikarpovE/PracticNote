from AppController import AppController
from UserInterface import UserInterface
from CatalogNotes import CatalogNotes

def application_start(app):
    app.start()

if __name__ == '__main__':
    app = AppController(None, UserInterface(), CatalogNotes('catalog.json'))
    application_start(app)
