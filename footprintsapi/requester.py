"""Module housing the SOAP request handler."""

from .utils import parse_keys, set_default_attr
from requests.auth import HTTPBasicAuth
from requests import Response, Session
from .exceptions import (
    ResourceDoesNotExist,
    FootprintsException,
    Unauthorized,
    BadRequest,
    Forbidden,
)
from typing import NoReturn
from zeep.transports import Transport
from zeep.cache import SqliteCache
from zeep import Client, Settings
from typing import Optional
from http import HTTPStatus
import requests
import zeep


class Requester:
    """Responsible for handling SOAP requests."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        base_url: str,
        settings: Optional[Settings] = None,
        storage_url: Optional[str] = None,
        timeout: Optional[int] = 60,
    ) -> NoReturn:
        """Init function."""
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self._cache = []
        self._settings = settings
        self._session = Session()
        self._session.auth = HTTPBasicAuth(self.client_id, self.client_secret)
        self.storage_url = storage_url
        cache = None
        if self.storage_url:
            cache = SqliteCache(path=storage_url, timeout=timeout)
        try:
            self._client = Client(
                self.base_url,
                transport=Transport(session=self._session, cache=cache),
                settings=self._settings,
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Unauthorized(e)
            raise BadRequest(e)

        except requests.exceptions.ConnectionError as e:
            raise ResourceDoesNotExist()

    def request(
        self, method_name: str, params: Optional[dict] = {}, **kwargs
    ) -> Response:
        """Make a request to the Footprints API and return the response.

        :param method_name: The name of the method to use for the request.
        For example: `getItemId`, `getTicketDetails`, `getItemDetails`.

        :param params: The parameters to send to footprints.
        """
        # I believe this is an exhaustive list for the methods the SOAP API supports?
        query_methods = [
            "createCI",
            "createContact",
            "createItem",
            "createOrEditContact",
            "createTicket",
            "createTicketAndLinkAssets",
            "editCI",
            "editContact",
            "editItem",
            "editTicket",
            "getContactAssociatedTickets",
            "getItemDetails",
            "getItemId",
            "getTicketDetails",
            "linkItems",
            "linkTickets",
            "listContainerDefinitions",
            "listFieldDefinitions",
            "listItemDefinitions",
            "listQuickTemplates",
            "listSearches",
            "runSearch",
        ]

        if method_name not in query_methods:
            raise ValueError("Unsupported method.")

        if "kwargs" not in params and kwargs:
            params = {**params, **kwargs}

        # Convert params keys to footprints naming convention
        if params:
            params = parse_keys(params)

        response = None
        try:
            # Dynamically call the method
            response = self._client.service[method_name](params)

            # Doesn't always return a regular json response and can sometimes
            # return objects.
            if hasattr(response, "__dict__"):
                set_default_attr(response, "_itemId", params.get("_itemId"))
                set_default_attr(
                    response,
                    "_itemDefinitionId",
                    params.get("_itemDefinitionId"),
                )
                set_default_attr(
                    response,
                    "_ticketDefinitionId",
                    params.get("_itemDefinitionId"),
                )
                set_default_attr(
                    response, "_ticketNumber", params.get("_ticketNumber")
                )

            # Add response to internal cache
            if len(self._cache) > 4:
                self._cache.pop()

            self._cache.insert(0, response)

        except requests.exceptions.HTTPError as e:
            raise FootprintsException(e)

        except zeep.exceptions.ValidationError as e:
            raise BadRequest(e)

        except zeep.exceptions.Fault as e:
            raise ResourceDoesNotExist(e)

        except AttributeError:
            raise ResourceDoesNotExist()

        except ValueError:
            raise Forbidden()

        return response
