import requests


class HotyBin:
    def __init__(self, text: str):
        self.text = text

    def paste(self):
        try:
            r = requests.post(
                "https://nekobin.com/api/documents",
                json={"content": self.text},
                timeout=10
            )
            if r.status_code == 200:
                key = r.json()["result"]["key"]
                return f"https://nekobin.com/{key}"
        except Exception:
            pass

        return "Paste failed"

