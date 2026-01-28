import requests


class HottyBin:
    def __init__(self, content: str):
        self.content = content

    def paste(self):
        try:
            r = requests.post(
                "https://nekobin.com/api/documents",
                json={"content": self.content},
                timeout=10
            )
            if r.status_code == 200:
                key = r.json()["result"]["key"]
                return f"https://nekobin.com/{key}"
        except Exception:
            pass
        return "Paste failed"


class AMBOTOPBin:
    def __init__(self, content: str):
        self.content = content

    def paste(self):
        try:
            r = requests.post(
                "https://nekobin.com/api/documents",
                json={"content": self.content},
                timeout=10
            )
            if r.status_code == 200:
                key = r.json()["result"]["key"]
                return f"https://nekobin.com/{key}"
        except Exception:
            pass
        return "Paste failed"
