import hashlib
import secrets
import string
import threading
import uuid

from app.constants import Constants


class UniqueIDGenerationManager:
    """
    Generate a 10-character Base62 UUID with high entropy.
    Combines uuid4, cryptographic randomness, and SHA-256 hashing.
    """

    def __init__(self, length=10):
        """
        Constructir takes length of the unique_id to be generated.
        """
        self.length = length
        self.lock = threading.Lock()
        self.charset = string.ascii_letters + string.digits

    def generate_unique_id(self):
        """
        Generates a unique 14-character Base62 string by:
        - Creating a UUID4 seed
        - Appending a 256-bit random secret
        - Hashing the combined data
        - Encoding the hash digest to Base62
        """
        with self.lock:
            unique_seed = f"{uuid.uuid4()}"
            random_secret = secrets.token_bytes(32)
            combined_data = unique_seed.encode() + random_secret
            hash_digest = hashlib.sha256(combined_data).digest()
            unique_id = self._hash_to_base62(hash_digest)
            return Constants.SHORT_URL.format(unique_id=unique_id)

    def _hash_to_base62(self, hash_bytes):
        """
        Converts a byte-based hash into a Base62-encoded string of given length.

        Args:
            hash_bytes (bytes): The input hash digest (e.g., from SHA-256)
            length (int): Desired length of the output Base62 string

        Returns:
            str: A Base62-encoded string
        """
        num = int.from_bytes(hash_bytes, byteorder="big")
        result = ""
        for _ in range(self.length):
            result = self.charset[num % 62] + result
            num //= 62
        return result
