import base64
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from errors import IdentifierError
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data import PasswordStorage
    from interfaces import ExporterProto


class CipherMixin:
    def _decrypt(self, ciphertext: str, key: str) -> str:
        byte_key = key.encode('utf8')
        encrypted_key = SHA256.new(byte_key).digest()
        d = base64.b64decode(ciphertext)
        iv, _ciphertext = d[:AES.block_size], d[AES.block_size:]
        cipher = AES.new(encrypted_key, AES.MODE_CFB, iv)
        return cipher.decrypt(_ciphertext).decode('utf8')

    def _encrypt(self, plaintext: str, key: str) -> str:
        byte_key = key.encode('utf8')
        encrypted_key = SHA256.new(byte_key).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(encrypted_key, AES.MODE_CFB, iv)
        res = base64.b64encode(iv + cipher.encrypt(plaintext.encode('utf8')))
        return res.decode('utf8')


class PasswordManager(CipherMixin):
    def __init__(self,
                 password_connector:
                 'PasswordStorage') -> None:
        self.password_connector = password_connector

    def get_password(self, identifier: str,
                     entered_key: str) -> IdentifierError | str:
        try:
            self.ident_existence(identifier)
        except IdentifierError as err:
            return err
        password = self.password_connector.read()[identifier]
        return self._decrypt(password, entered_key)

    def add_password(self, password: str,
                     identifier: str,
                     entered_key: str) -> None:
        try:
            self.ident_uniqueness(identifier)
            all_passwords = self.password_connector.read()
            all_passwords[identifier] = self._encrypt(password, entered_key)
            self.password_connector.record(all_passwords)
        except IdentifierError as err:
            print(err)

    def delete(self, identifier: str) -> None:
        try:
            self.ident_existence(identifier)
            all_passwords = self.password_connector.read()
            del all_passwords[identifier]
            self.password_connector.record(all_passwords)
        except IdentifierError as err:
            print(err)

    def get_password_list(self) -> list[str]:
        return list(self.password_connector.read().keys())

    def ident_existence(self, identifier: str) -> None:
        identifier_list = [ident.lower() for ident in self.get_password_list()]
        if identifier.lower() not in identifier_list:
            raise IdentifierError('This identifier is not exist.')

    def ident_uniqueness(self, identifier: str) -> None:
        identifier_list = [ident.lower() for ident in self.get_password_list()]
        if identifier.lower() not in identifier_list:
            raise IdentifierError('This identifier already exists.')

    def export_all_passwords(self,
                             db_connector: 'ExporterProto',
                             key: str) -> None:
        password_dict = {}
        for identifier, password in self.password_connector.read().items():
            password_dict[identifier] = self._decrypt(password, key)
        db_connector.export(password_dict)
