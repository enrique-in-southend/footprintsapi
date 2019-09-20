"""Used to connect to BMC (Numara) Footprints SOAP API.

Contains the footprints client, which all supported endpoints should be
either directly or indirectly accessible from.
"""

from .models import Ticket, Item, FootprintsBaseObject
from typing import Union, Optional, NoReturn
from .requester import Requester
from .mixins import CommonMixin
from .utils import cleanup_args
from requests import Response
from zeep import Settings


class Footprints(CommonMixin, FootprintsBaseObject):
    """The main class to be instantiated to provide access to Footprints's SOAP API."""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        base_url: str = None,
        settings: Optional[object] = None,
        storage_url: Optional[str] = None,
        timeout: Optional[int] = 60,
    ) -> NoReturn:
        """Init function.

        :param client_id: The username/client id.

        :param client_secret: password/client secret.

        :param base_url: The base URL of the footprints instance.

        :param storage_url: A url path for sqlite to store the wsdl.

        :param timeout: A timeout for the DB only relevant when providing a storage url.
        """
        if settings and not isinstance(settings, Settings):
            raise TypeError(
                "Settings are expected in the form of a Settings object."
            )

        self._requester = Requester(
            client_id, client_secret, base_url, settings, storage_url, timeout
        )
        # Initialize any mixins.
        super().__init__()

    def get_item(
        self,
        item_definition_id: Union[str, int],
        item_id: Union[str, int],
        fields_to_retrieve: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Retrieve item details.

        :param item_id: The id of the item to retrieve.

        :param item_definition_id: The global item definition, can only be
        optionally passed if it already has been defined within the Footprints
        object.

        :param fields_to_retrieve: List of external field names to retrieve.

        :param submitter: Userid/username of submitter.

        :calls: `GET getItemDetails`

        :return: Item object.
        """
        return Item(
            *self._obj_data(
                method_name="getItemDetails",
                params=cleanup_args(locals()),
                **kwargs,
            )
        )

    def get_ticket(
        self,
        item_definition_id: Union[str, int],
        item_id: Union[str, int],
        submitter: Optional[str] = None,
        fields_to_retrieve: Optional[list] = None,
        **kwargs,
    ) -> Ticket:
        """Get a footprints ticket.

        :param item_id: The ticket's item identifier or item_number.

        :param submitter: Userid/username of submitter.

        :param fields_to_retrieve: What specific fields to retrieve. List of external field names.

        :calls: `GET getTicketDetails`

        :return: Ticket object
        """
        # Create params based on local args
        params = cleanup_args(locals())

        if kwargs:
            params = {**params, **kwargs}

        if isinstance(item_id, str):
            params["item_number"] = item_id
            params["item_id"] = self.get_item_id(**params)

        return Ticket(
            *self._obj_data(
                method_name="getTicketDetails", params=params, **kwargs
            )
        )

    def create_ticket(
        self,
        ticket_definition_id: Union[str, int],
        ticket_fields: dict,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        quick_template_id: Optional[str] = None,
        contact_definition_id: Optional[str] = None,
        select_contact: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create a footprints ticket.

        :param ticket_fields: List of ticket fieldnames. Field names are the external names.

        :param ticket_values: The values associated with the ticket fields.

        :param assignees: List of people to assign to ticket.

        :param submitter: The person who submitted the ticket.

        :param quick_template_id: The id for the quick template.

        :param contact_definition_id: The id for contact linking.

        :param selectContact: The contact primary key. Usually an email address.

        :calls: `POST createTicket`

        :return: Item ID

        """
        return self._requester.request(
            method_name="createTicket", params=cleanup_args(locals()), **kwargs
        )
