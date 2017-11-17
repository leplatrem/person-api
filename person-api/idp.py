import json
import logging
from config import get_config
from six.moves.urllib.request import urlopen
from jose import jwt


logger = logging.getLogger(__name__)
CONFIG = get_config()


class AuthError(Exception):
    """Generic exception facility for jwt exceptions."""
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


class TrustedParty(object):
    """Dictates things that are true about the Key Server in the trust."""
    def __init__(self):
        self.auth_zero_url = CONFIG('auth0_url')

    @property
    def jwks_url(self):
        return "https://"+self.auth_zero_url+"/.well-known/jwks.json"

    @property
    def public_key(self):
        public_key = self._tokenize_public_key(self._load_public_key())
        return public_key

    def _load_public_key(self):
        jsonurl = urlopen(self.jwks_url)
        jwks = json.loads(jsonurl.read())
        return jwks

    def _tokenize_public_key(self, public_key_json):
        rsa_key = {}
        for key in public_key_json["keys"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
        return rsa_key


class Trust(object):
    """Validate JWT and audience."""
    @property
    def api_audience(self):
        return CONFIG('audience')

    @property
    def algorithms(self):
        return ["RS256"]

    def verify(self, token, rsa_signature):
        try:
            logger.info('Attempting to verify token: {}'.format(token))
            payload = jwt.decode(
                token,
                rsa_signature,
                algorithms=self.algorithms,
                audience=self.api_audience,
                issuer="https://"+CONFIG('auth0_url')+"/"
            )
        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                            "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                            "description":
                                "incorrect claims,"
                                "please check the audience and issuer"}, 401)
        except Exception as e:
            logger.error('Unknown parsing problem: {}'.format(e))
            raise AuthError({"code": "invalid_header",
                            "description":
                                "Unable to parse authentication"
                                " token."}, 400)
        return payload
