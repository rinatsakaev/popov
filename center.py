from typing import Dict

from certificate import Certificate


class Center:
    def __init__(self):
        self.cache = dict()

    def create_certificate(self, client_id: int, client_income: int) -> Certificate:
        certificate = Certificate(client_id, client_income)
        self.cache[certificate.get_hash(0)]: Dict[str, Certificate] = certificate
        return certificate

    def certificate_exists(self, certificate_hash: str) -> bool:
        return certificate_hash in self.cache

    def ask_for_hash(self, old_hash: str, nonce):
        certificate = self.cache.get(old_hash)
        if certificate is None:
            raise ValueError("Certificate not found")
        return certificate.get_hash(nonce)

