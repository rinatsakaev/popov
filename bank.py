import random

from center import Center
from client import Client


class Bank:
    def __init__(self, suspiciousness: int, center: Center):
        self.suspiciousness = suspiciousness
        self.center = center

    def verify_client(self, client: Client) -> bool:
        certificate_hash = client.ask_for_hash(0)
        if not self.center.certificate_exists(certificate_hash):
            return False

        for _ in range(self.suspiciousness):
            r = random.randint(0, pow(10, 6))
            client_hash = client.ask_for_hash(r)
            center_hash = self.center.ask_for_hash(certificate_hash, r)
            if client_hash == center_hash:
                continue
            else:
                return False

        return True