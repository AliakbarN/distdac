class UrlGenerator:
    def __init__(self) -> None:
        self.base_url = "https://yandex.com/maps/10335/tashkent/?mode=routes&rtext={{point_1_x}}%2C{{point_1_y}}~{{point_2_x}}%2C{{point_2_y}}&rtt=auto&ruri=~&z=14"

    def set_base_url(self, base_url: str) -> None:
        self.base_url = base_url

    def generate(self, data: dict) -> str:
        url = self.base_url
        for key, value in data.items():
            url = url.replace("{{" + str(key) + "}}", str(value))

        return url
