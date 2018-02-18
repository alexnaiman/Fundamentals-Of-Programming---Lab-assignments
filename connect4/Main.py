from Config import Config


class Main:
    def __init__(self):
        self.config = Config("settings.properties")
        self.config.readSettings()
        # self.ui, self.oponent = self.config.config()
        # self.ui =
        self.app = self.config.config()

    def run(self):
        self.app.run()


main = Main()
main.run()
