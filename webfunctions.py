class WebFunctions:  # Newegg
    def __init__(self, cell):
        self.cell = cell

    @classmethod
    def url_changer(cls, base, page_num):
        new_url = base + f"{page_num}.html"
        return new_url


def url_changer(base, page_num):
    new_url = base + f"{page_num}.html"
    return new_url