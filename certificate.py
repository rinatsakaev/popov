import hashlib


class Certificate:
    def __init__(self, id: int, income: int):
        self.id = id
        self.income = income

    def get_hash(self, nonce):
        data = f"id={self.id};income={self.income};nonce={nonce};"
        return hashlib.sha1(data.encode('utf-8')).hexdigest()
