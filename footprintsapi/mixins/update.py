"""Collection of pure update mixins."""

from typing import Union, Optional
from ..utils import cleanup_args


class EditCIMixin:
    """Adds basic `editCI` functionality to Footprints object."""

    def update_ci(
        self,
        cmdb_definition_id: str,
        ci_id: Union[str, int],
        ci_fields=list,
        status: str = None,
        submitter: Optional[str] = None,
        **kwargs
    ) -> str:
        """Update a CI.

        :param cmdb_definition_id: The cmdb definition id.

        :param ci_id: The CI id.

        :param cifields: List of dicts with itemFields and itemValues.

        :param status: The status.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editCI`
        :return: CI ID.
        """
        return self._requester.request(
            method_name="editCI", params=cleanup_args(locals()), **kwargs
        )


class EditContactMixin:
    """Adds basic `editContact` functionality to Footprints Object."""

    def update_contact(
        self,
        address_book_definition_id: Union[str, int],
        contact_id: Union[str, int],
        contact_fields: list,
        submitter: Optional[str] = None,
        **kwargs
    ) -> str:
        """Update a contact.

        :param address_book_definition_id: The address book to add the contact in.

        :param contact_id: The contact id.

        :param contact_fields: List of dicts with itemFields and itemValues.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editContact`

        :return: Contact ID.
        """
        return self._requester.request(
            method_name="editContact", params=cleanup_args(locals()), **kwargs
        )


class EditItemMixin:
    """Adds basic `editItem` functionality to Footprints object."""

    def update_item(
        self,
        item_definition_id: Union[str, int],
        item_id: str,
        item_fields: list,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs
    ) -> str:
        """Update an Item.

        :param item_definition_id: The container item definition.

        :param item_id: The item id.

        :param item_fields: List of dicts with itemFields and itemValues.

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editItem`

        :return: Item id.method_name=
        """
        return self._requester.request(
            method_name="editItem", params=cleanup_args(locals()), **kwargs
        )


class EditTicketMixin:
    """Adds basic `editTicket` functionality to Footprints object."""

    def update_ticket(
        self,
        ticket_definition_id: Union[str, int],
        ticket_id: Union[str, int],
        ticket_fields: list,
        contact_definition_id: Union[str, int] = None,
        select_contact: Optional[str] = None,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs
    ) -> str:
        """Update a ticket.

        :param ticket_definition_id: The container ticket definition id.

        :param ticket_id: The id of the ticket to edit.

        :param ticket_fields: List of dicts with itemFields and itemValues.

        :param contact_definition_id: The contact definition id for contact linking.

        :param select_contact: Contact primary key, usually email.

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editTicket`

        :return: Ticket id.
        """
        return self._requester.request(
            method_name="editTicket", params=cleanup_args(locals()), **kwargs
        )
