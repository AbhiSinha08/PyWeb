class Element():
    def __init__(self, type: str, **kwargs) -> None:
        self.type = type
        self.inner_text = ""
        self.inner = []

        # To add CSS properties here

    def text(self, *args: str, heading: int = None) -> None:
        if heading:
            p = Element(f'h{heading}')
        else:
            p = Element('span')
        for text in args:
            text = text.replace("\n", " <br> ")
            p.inner_text += text
        self.inner.append(p)

    def inside(self, type='div', **kwargs):
        element = Element(type, **kwargs)
        self.inner.append(element)
        return element

    def render(self, string: str = "") -> str:
        string += f"<{self.type}>\n"
        if self.inner_text:
            string += self.inner_text
        for element in self.inner:
            string += element.render()
        string += f"</{self.type}>\n"
        return string

class HTML():
    def __init__(self,
                    title: str = "PyWeb Document",
                    icon: str = "icon.ico",
                    lang: str = "en"
                ) -> None :
        self.title = title
        self.icon = icon
        self.lang = lang
        self.meta_charset = "utf-8"
        self.meta_name = {
                    'viewport': 'width=device-width, initial-scale=1',
                    'description': 'An HTML Document generated using PyWeb'
                    }
        self.meta_property = {}
        self.meta_http_equiv = {}

        self.content = Element('body')

    def render_head(self) -> str:
        head = f"""<title> {self.title} </title>
                <link rel="icon" href="{self.icon}" type="image/x-icon">
                <meta charset="{self.meta_charset}">"""
        for name in self.meta_name:
            head += f'\n <meta name="{name}" content="{self.meta_name[name]}">'
        for prop in self.meta_property:
            head += f'\n <meta property="{prop}" content="{self.meta_property[prop]}">'
        for i in self.meta_http_equiv:
            head += f'\n <meta http-equiv="{i}" content="{self.meta_http_equiv[i]}">'

        return head

    def render_body(self) -> str:
        return self.content.render()

    def render(self) -> str:
        return f""" <!DOCTYPE html>
                    <html lang="{self.lang}">
                    <head>
                    {self.render_head()}
                    </head>
                    {self.render_body()}
                    </html>
                """

    def render_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.render())