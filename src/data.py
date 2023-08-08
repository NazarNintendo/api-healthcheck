import json
from typing import Dict, List


class API:
    """
    API class store API data.

    Attributes
    ----------
    id : str
        The API's unique id for the purpose of storing.
    url : str
        The URL to send requests to.
    freq : int
        The frequency of requests in seconds.
    integration : str
        The integration to use for the request.
    args : List[str]
        The arguments to send with the request.
    """

    def __init__(self, data: Dict) -> None:
        """
        Initialize the API object.
        :param data: The data to initialize the object with.
        :return: None
        """
        self.id = data["id"]
        self.url = data["url"]
        self.freq = data["freq"]
        self.integration = data["integration"]
        self.args = data["args"]


class APIState:
    """
    APIState class stores the state of the APIs.

    Attributes
    ----------
    state : Dict[str, bool]
        The state of the APIs.
    """

    def __init__(self, api_ids: List[str]) -> None:
        """
        Initialize the APIState object.
        :param api_ids: The list of ids of the APIs.
        :return: None
        """
        self.state = {}
        for api_id in api_ids:
            self.state[api_id] = False

    def set(self, api_id: str, state: bool) -> None:
        """
        Set the state of an API.
        :param api_id: The id of the API.
        :param state: The state of the API.
        :return: None
        """
        self.state[api_id] = state

    def get(self, api_id: str) -> bool:
        """
        Get the state of an API.
        :param api_id: The id of the API.
        :return: The state of the API.
        """
        return self.state[api_id]


def load_data() -> List[API]:
    """
    Load the data from the data.json file.
    :return: The list of API objects.
    """
    with open("data.json") as json_file:
        apis = json.load(json_file)
    return [API(api) for api in apis]
