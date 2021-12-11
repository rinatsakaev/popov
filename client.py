from center import Center


class Client:
    def __init__(self, id: int, income: int, center: Center):
        self.__id = id
        self.__income = income
        self.__certificate = None
        self._center = center

    def request_certificate(self) -> None:
        self.__certificate = self._center.create_certificate(self.__id, self.__income)

    def ask_for_hash(self, nonce: int) -> str:
        return self.__certificate.get_hash(nonce)


