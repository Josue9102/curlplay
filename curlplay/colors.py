class Color:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def get_color_code(color_name):
        # Example: Return console color codes based on color name
        color_codes = {
            "red": "\033[31m",
            "green": "\033[32m",
            "blue": "\033[34m",
            "reset": "\033[0m",
        }
        return color_codes.get(color_name.lower(), color_codes["reset"])
