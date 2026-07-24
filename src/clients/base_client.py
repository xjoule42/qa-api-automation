import requests

from config.settings import BASE_URL, TIMEOUT
from src.utils.logger import get_logger

logger = get_logger(__name__)


class BaseClient:

    def __init__(self):

        self.base_url = BASE_URL
        self.timeout = TIMEOUT

        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    def set_headers(self, headers:dict):
        """
        Update session headers.
        """
        self.session.headers.update(headers)

    def set_token(self, token: str):
        """
        Set Bearer authentication token
        """
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def clear_token(self):
        """
        Remove Authorization header.
        """
        self.session.headers.pop("Authorization", None)


    def _log_request(self, method, url, params=None, payload=None):
        """Log outgoing HTTP request."""

        logger.info("=" * 60)
        logger.info(f"{method} {url}")

        if params:
            logger.info(f"Query Params: {params}")

        if payload:
            logger.info(f"Payload: {payload}")

    def _log_response(self, response):
        """Log incoming HTTP response."""

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")
        logger.info("=" * 60)

    def get(self, endpoint, params=None):

        url = f"{self.base_url}{endpoint}"

        self._log_request("GET", url, params=params)

        response = self.session.get(
            url,
            params=params,
            timeout=self.timeout
        )

        self._log_response(response)

        return response

    def post(self, endpoint, payload=None):

        url = f"{self.base_url}{endpoint}"

        self._log_request("POST", url, payload=payload)

        response = self.session.post(
            url,
            json=payload,
            timeout=self.timeout
        )

        self._log_response(response)

        return response

    def put(self, endpoint, payload=None):

        url = f"{self.base_url}{endpoint}"

        self._log_request("PUT", url, payload=payload)

        response = self.session.put(
            url,
            json=payload,
            timeout=self.timeout
        )

        self._log_response(response)

        return response

    def patch(self, endpoint, payload=None):

        url = f"{self.base_url}{endpoint}"

        self._log_request("PATCH", url, payload=payload)

        response = self.session.patch(
            url,
            json=payload,
            timeout=self.timeout
        )

        self._log_response(response)

        return response

    def delete(self, endpoint):

        url = f"{self.base_url}{endpoint}"

        self._log_request("DELETE", url)

        response = self.session.delete(
            url,
            timeout=self.timeout
        )

        self._log_response(response)

        return response