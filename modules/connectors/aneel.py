import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from settings import ANEEL_API_HOST


class AneelAPIConnector:

    def __init__(self, host: str = ANEEL_API_HOST):
        self.host = host
        self.retries = 5
        self.backoff_factor = 10
        self.status_forcelist = (500, 502, 503, 504)

    def __requests_retry_session(self, session=None):
        session = session or requests.Session()
        retry = Retry(
            total=self.retries,
            read=self.retries,
            connect=self.retries,
            backoff_factor=self.backoff_factor,
            status_forcelist=self.status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def consult_dataset(self, params):
        records = []
        params["offset"] = 0
        http_session = self.__requests_retry_session()
        while True:
            try:
                print(
                    f"Querying API for resource {params['resource_id']} at offset: {params['offset']}"
                )
                response = http_session.get(url=self.host, params=params, timeout=180)
                response.raise_for_status()
                result = response.json()["result"]
                if result:
                    yield result["records"]
                if len(result["records"]) < params["limit"]:
                    break
                params["offset"] += params["limit"]
            except Exception as error:
                print(f"Request failed after several retries: {str(error)}")
                params["offset"] += params["limit"]
                continue
        return records
