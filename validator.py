from selenium import webdriver
from csv import DictReader


class Validator:
    "Manual validator of IMDB"

    def __init__(self):
        self._initialize()

    def _initialize(self):
        # self.PATH = r"C:\Users\asus\Downloads\chromedriver_win32\chromedriver.exe"
        # self.bot = webdriver.Chrome(executable_path=self.PATH)
        self.bot = webdriver.Chrome()
        self.bot.fullscreen_window()

    def access(self, imdb):
        self.bot.get(f'https://www.imdb.com/title/{imdb[1]}/')
        try:
            cont = input(f"Match {imdb[0]}?\n")
        except:
            self.bot.quit()

        if cont == "":
            print("Moving to another IMDB!")

    def get_imdb(self, csv):
        # imdbs
        imdbs = []
        with open(csv, "r") as file:
            table = DictReader(file, delimiter="|")
            for row in table:
                # print(row)
                i = [None, None]
                i[0] = row["title"]
                i[1] = row["imdb_number"]
                imdbs.append(i)

            return imdbs


if __name__ == "__main__":
    imdb = Validator()

    imdbs = imdb.get_imdb("peacocktv_front_2020.08.16_imdb.csv")
    i = 265
    while i < len(imdbs):
        imdb.access(imdbs[i])
        i += 1
