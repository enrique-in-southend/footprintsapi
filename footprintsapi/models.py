"""Base FootprintsObject."""

import json
from typing import Optional, Union

from .mixins import (
    COMMON_ATTRS,
    CommonMixin,
    CreateCIMixin,
    CreateContactMixin,
    CreateItemMixin,
    CreateOrEditContactMixin,
    CreateTicketAndLinkAssets,
    CustomAttributesMixin,
    EditCIMixin,
    EditContactMixin,
    EditItemMixin,
    EditTicketMixin,
    GetContactAssociatedTickets,
    GetItemDetailsMixin,
    GetItemIdMixin,
    LinkItems,
    LinkTickets,
    ListContainerDefinitionsMixin,
    ListFieldDefinitionsMixin,
    ListItemDefinitionsMixin,
    ListQuickTemplatesMixin,
    ListSearchesMixin,
    RunSearchMixin,
)
from .requester import Requester
from .utils import cleanup_args, get_attributes, parse_keys, pretty_attributes, to_dict


class FootprintsObject:
    """Base class for all classes representing objects returned by the API.

    This makes a call to :func:`Footprintsapi.FootprintsObject.set_attributes`
    to dynamically construct this object's attributes with a JSON object.
    """

    def __init__(self, requester: Requester, attributes: dict) -> None:
        """:param attributes: Dict(JSON) to build this object with."""
        self._requester = requester
        self._original_attributes = {}
        self.attributes = {}
        self.set_attributes(attributes)
        self._update_attributes = True

    def __repr__(self) -> str:
        """Class representation."""
        class_name = self.__class__.__name__
        ignored_attrs = [
            "attributes",
            "_requester",
            "_original_attributes",
            "_update_attributes",
        ]

        attrs = [k for k in self.__dict__.keys() if k not in ignored_attrs]
        attrs = pretty_attributes(self.attributes, attrs, 8)
        return f"{class_name}({attrs})"

    def __setattr__(self, key, value) -> None:
        """Set attributes."""
        if getattr(self, "_update_attributes", False):
            self.attributes[key] = value
        super(FootprintsObject, self).__setattr__(key, value)

    @property
    def to_json(self) -> dict:
        """Return the original JSON response from the API."""
        return self._original_attributes

    def set_attributes(self, attributes: Union[dict, object]) -> None:
        """Load this object with attributes.

        This method attempts to detect special types based on the field's content
        and will create an additional attribute of that type.

        :param attributes: The JSON/dict/object to build this object with.
        """
        self.attributes = attributes
        if hasattr(attributes, "_itemFields"):
            self.attributes = dict(
                get_attributes(
                    fields_to_iterate=attributes._itemFields["itemFields"],
                    attributes_to_fetch=COMMON_ATTRS,
                )
            )

        if isinstance(self.attributes, object) and not isinstance(
            self.attributes, dict
        ):
            self.attributes = to_dict(attributes)

        if hasattr(self, "get_custom_attributes"):
            self.attributes.update(self.get_custom_attributes())

        if any(map(lambda k: k.startswith("_"), self.attributes.keys())):
            self.attributes = parse_keys(self.attributes, "snake_case")

        self._original_attributes = attributes
        if isinstance(self._original_attributes, object):
            self._original_attributes = json.dumps(
                attributes, default=lambda o: o.__dict__, indent=2
            )

        for key, value in self.attributes.items():
            self.__setattr__(key, value)


class Ticket(FootprintsObject, CustomAttributesMixin):
    """Base class for tickets."""

    def update(
        self,
        ticket_fields: dict,
        ticket_id: Union[str, int] = None,
        ticket_definition_id: Union[str, int] = None,
        contact_definition_id: Union[str, int] = None,
        select_contact: Optional[str] = None,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Update a ticket.

        :param ticket_fields: Dict with itemfield list dicts with itemFields and itemValues.

        :param ticket_id: The id of the ticket to edit. (Optional as
        ticket object already has its own ticket id)

        :param ticket_definition_id: The container ticket definition id. (Optional as
        ticket object already has its own ticket definition id)

        :param contact_definition_id: The contact definition id for contact linking.

        :param select_contact: Contact primary key, usually email.

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editTicket`

        :return: Ticket id.
        """
        params = cleanup_args(locals())
        if "ticket_definition_id" not in params:
            params["ticket_definition_id"] = self.ticket_definition_id
        if "ticket_id" not in params:
            params["ticket_id"] = self.item_id
        return self._requester.request(
            method_name="editTicket", params=params, **kwargs
        )


class Item(FootprintsObject):
    """Base class for tickets."""

    def update(
        self,
        item_fields: dict,
        item_id: str = None,
        item_definition_id: Union[str, int] = None,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Update an Item.

        :param item_fields: List of dicts with itemFields and itemValues.

        :param item_definition_id: The container item definition. (Optional)

        :param item_id: The item id. (Optional)

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `PUT editItem`

        :return: Item id.
        """
        params = cleanup_args(locals())
        if "item_definition_id" not in params:
            params["item_definition_id"] = self.item_definition_id
        if "item_id" not in params:
            params["item_id"] = self.item_id
        return self._requester.request(method_name="editItem", params=params, **kwargs)


class FootprintsBaseObject(
    CreateCIMixin,
    CreateContactMixin,
    CreateItemMixin,
    CreateOrEditContactMixin,
    CreateTicketAndLinkAssets,
    EditCIMixin,
    EditContactMixin,
    EditItemMixin,
    EditTicketMixin,
    GetItemIdMixin,
    GetItemDetailsMixin,
    GetContactAssociatedTickets,
    ListContainerDefinitionsMixin,
    ListFieldDefinitionsMixin,
    ListItemDefinitionsMixin,
    ListQuickTemplatesMixin,
    ListSearchesMixin,
    RunSearchMixin,
    LinkItems,
):
    """Base class for main Footprints wrapper."""

    pass
