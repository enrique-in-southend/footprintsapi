"""Collection of common mixins."""

from typing import Optional, Tuple, Union

from footprintsapi.requester import Requester

from .utils import cleanup_args, get_attributes

COMMON_ATTRS = [
    "Title",
    "Created By",
    "Full Name",
    "Priority",
    "Status",
    "User ID",
    "Description",
    "Email Address",
]

CUSTOM_ATTRS = [
    "Escalation Status",
    "Email Assignees",
    "PreEscalation",
    "Email Address",
    "Assignees",
    "CC Email",
    "Internal",
    "Service",
    "Details",
    "Email CC",
    "Full Name",
]


class CommonMixin:
    """Common mixin class."""

    def _obj_data(
        self, method_name: str, params: dict, **kwargs
    ) -> Tuple[Requester, dict]:
        """Will wrap data within a FootprintsObject."""
        return (self._requester, self._requester.request(method_name, params, **kwargs))


class CustomAttributesMixin:
    """Mixin class to get custom attributes."""

    def get_custom_attributes(
        self, custom_attributes: Optional[list] = CUSTOM_ATTRS
    ) -> dict:
        """Find custom attributes relevant to your organization."""
        attributes = {}
        try:
            attributes = get_attributes(
                fields_to_iterate=self.attributes.get("_customFields")["itemFields"],
                attributes_to_fetch=custom_attributes,
            )
        except TypeError:
            pass
        return attributes


class GetItemIdMixin:
    """Add basic `getItemId` functionality to Footprints object."""

    def get_item_id(
        self,
        item_definition_id: Union[str, int],
        item_number: Union[str, int],
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Retrieve an item id.

        :param item_number: The Service request number,
        can optionally include the organization prefix.

        :param item_definition_id: The global item definition, can only be
        optionally passed if it already has been defined within the Footprints
        object.

        :param submitter: Userid/username of submitter.

        :calls: `GET getItemId`

        :return: Item id.
        """
        return self._requester.request(
            method_name="getItemId", params=cleanup_args(locals()), **kwargs
        )


class GetItemDetailsMixin:
    """Add basic `getItemDetails` functionality to Footprints object."""

    def get_item_details(
        self,
        item_definition_id: Union[str, int],
        item_id: Union[str, int],
        fields_to_retrieve: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> dict:
        """Retrieve item details.

        :param item_id: The id of the item to retrieve.

        :param item_definition_id: The global item definition, can only be
        optionally passed if it already has been defined within the Footprints
        object.

        :param fields_to_retrieve: List of external field names to retrieve.

        :param submitter: Userid/username of submitter.

        :calls: `GET getItemDetails`

        :return: Dict of item fields and assignees.
        """
        return self._requester.request(
            method_name="getItemDetails", params=cleanup_args(locals()), **kwargs
        )


class GetContactAssociatedTickets:
    """Add basic `getContactAssociatedTickets` functionality to Footprints object."""

    def get_contact_associated_tickets(
        self,
        contact_definition_id: Union[str, int],
        primary_key_value: str,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> dict:
        """Retrieve tickets from associated contacts.

        :param contact_definition_id: The contact definition id/item definition id.

        :param primary_key_value: Contact primary key. Usually email.

        :param submitter: Userid/username of submitter.

        :calls: `GET getContactAssociatedTickets`

        :known_issues: https://communities.bmc.com/thread/158874?start=0&tstart=0
        """
        return self._requester.request(
            method_name="getContactAssociatedTickets",
            params=cleanup_args(locals()),
            **kwargs,
        )


class ListContainerDefinitionsMixin:
    """Add basic `listContainerDefinitions` functionality to Footprints object."""

    def get_container_definitions(
        self,
        container_subtype_name: Optional[str] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrieve workspace IDs and names.

        :param container_subtype_name: The workspace name.

        :param submitter: Userid/username of submitter.

        :calls: `GET listContainerDefinitions`
        """
        return self._requester.request(
            method_name="listContainerDefinitions",
            params=cleanup_args(locals()),
            **kwargs,
        )


class ListItemDefinitionsMixin:
    """Add basic `listItemDefinitions` functionality to Footprints object."""

    def get_item_definitions(
        self,
        container_definition_id: Union[str, int],
        item_subtype_name: Optional[str] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrieve the IDs of the record/template definitions in a workspace.

        :param container_definition_id: The container id.

        :param item_subtype_name: The item name.

        :param submitter: Userid/username of submitter.

        :calls: `GET listItemDefinitions`
        """
        return self._requester.request(
            method_name="listItemDefinitions", params=cleanup_args(locals()), **kwargs
        )


class ListFieldDefinitionsMixin:
    """Add basic `listFieldDefinitions` functionality to Footprints object."""

    def get_field_definitions(
        self,
        item_definition_id: Union[str, int],
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrieve the IDs of the record/template definitions in a workspace.

        :param item_definition_id: The id of an item.

        :param submitter: Userid/username of submitter.

        :calls: `GET listFieldDefinitions`
        """
        return self._requester.request(
            method_name="listFieldDefinitions", params=cleanup_args(locals()), **kwargs
        )


class ListQuickTemplatesMixin:
    """Add basic `listQuickTemplates` functionality to Footprints object."""

    def get_quick_templates(
        self,
        item_definition_id: Union[str, int],
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrieve a list of templates and ids.

        :param item_definition_id: The id of an item.

        :param submitter: Userid/username of submitter.
        """
        return self._requester.request(
            method_name="listQuickTemplates", params=cleanup_args(locals()), **kwargs
        )


class ListSearchesMixin:
    """Add basic `listSearches` functionality to Footprints object."""

    def get_searches(
        self,
        item_type_name: Optional[str] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrive searches.

        :param item_type_name: Item name from which one can retrieve existing Saved Searches in the FootPrints application.

        :param submitter: Userid/username of submitter.
        """
        return self._requester.request(
            method_name="listSearches", params=cleanup_args(locals()), **kwargs
        )


class RunSearchMixin:
    """Add basic `runSearch` functionality to Footprints object."""

    def get_search(
        self, search_id: Union[str, int], submitter: Optional[str] = None, **kwargs
    ) -> list:
        """Retrive searches.

        :param search_id: You can retrieve the item_type_name parameter to get the item
        ID to run the search query from the existing Saved Searches only.

        :param submitter: Userid/username of submitter.
        """
        return self._requester.request(
            method_name="runSearch", params=cleanup_args(locals()), **kwargs
        )


class CreateCIMixin:
    """Add basic `createCI` functionality to Footprints object."""

    def create_ci(
        self,
        cmdb_definition_id: str,
        cifields: Optional[list] = None,
        status: Optional[str] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create a CI.

        :param cmdb_definition_id: The cmdb definition id.

        :param cifields: List of dicts with itemFields and itemValues.

        :param status: The status.

        :param submitter: Userid/username of submitter.

        :calls: `POST createCI`
        """
        return self._requester.request(
            method_name="createCI", params=cleanup_args(locals()), **kwargs
        )


class CreateContactMixin:
    """Add basic `createContact` functionality to Footprints object."""

    def create_contact(
        self,
        address_book_definition_id: Union[str, int],
        contact_fields: list,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create a contact.

        :param address_book_definition_id: The address book to add the contact in.

        :param contact_fields: List of dicts with itemFields and itemValues.

        :param submitter: Userid/username of submitter.

        :calls: `POST createContact`
        """
        return self._requester.request(
            method_name="createContact", params=cleanup_args(locals()), **kwargs
        )


class CreateItemMixin:
    """Adds basic `createItem` functionality to Footprints object."""

    def create_item(
        self,
        item_definition_id: Union[str, int],
        item_fields: list,
        quick_template_id: Union[str, int] = None,
        assignees: list = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create an item.

        :param item_definition_id: The global item definition.

        :param item_fields: List of dicts with itemFields and itemValues.

        :param quick_template_id: The quick template id to use.

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `POST createItem`
        """
        return self._requester.request(
            method_name="createItem", params=cleanup_args(locals()), **kwargs
        )


class CreateOrEditContactMixin:
    """Adds basic `createOrEditContact` functionality to Footprints object."""

    def create_or_edit_contact(
        self,
        address_book_definition_id: Union[str, int],
        contact_fields: list,
        contact_id: Union[str, int] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create or edit a contact.

        :param address_book_definition_id: The address book to create/edit the contact in.

        :param contact_fields: List of dicts with itemFields and itemValues.

        :param contact_id: The contact id if contact exists.

        :param submitter: Userid/username of submitter.

        :calls: `POST createOrEditContact`

        :return: Contact id.
        """
        return self._requester.request(
            method_name="createOrEditContact", params=cleanup_args(locals()), **kwargs
        )


class CreateTicketAndLinkAssets:
    """Adds basic `createTicketAndLinkAssets` functionality to Fooprints object."""

    def create_ticket_and_link_assets(
        self,
        ticket_definition_id: Union[str, int],
        ticket_fields: list,
        assets_list: Optional[list] = None,
        quick_template_id: Union[str, int] = None,
        assignees: Optional[list] = None,
        submitter: Optional[str] = None,
        **kwargs,
    ) -> str:
        """Create a ticket and link assets at the same time.

        :param ticket_definition_id: The organization ticket definition identifier.

        :param ticket_fields: List of dicts with itemFields and itemValues.

        assets_list: List of dicts with fieldNames and fieldValues.

        :param quick_template_id: The quick template id to use.

        :param assignees: The people to assign to the item.

        :param submitter: Userid/username of submitter.

        :calls: `POST createTicketAndLinkAssets`

        :return: Ticket id.
        """
        return self._requester.request(
            method_name="createTicketAndLinkAssets",
            params=cleanup_args(locals()),
            **kwargs,
        )


class LinkItems:
    """Adds basic `linkItems` functionality to Fooprints object."""

    def link_items(
        self,
        first_item_definition_id: Union[str, int],
        first_item_id: Union[str, int],
        second_item_definition_id: Union[str, int],
        second_item_id: Union[str, int],
        link_type_name: str,
        submitter: Optional[str] = None,
        **kwargs,
    ):
        """Create a ticket and link assets at the same time.

        :param first_item_definition_id: The first item definition identifier.

        :param first_item_id: The first item identifier.

        :param second_item_definition_id: The second item definition identifier.

        :param second_item_id: The second item identifier.

        :param link_type_name: The list of values are as follow:

        `Ticket/Contact
            Related Tickets
            Master/Subtask
            Global Link
            Ticket/CI
            Related CIs
            Contract/Service Level Target
            Service/Service Level Target
            Work Target/Service Level Target
            Ticket/Work Target
            Ticket/Service
            Ticket/Asset
            Ticket/Solution
            Ticket/Survey
            Contact/CI
            Related Tickets (Dynamic)
            Connects
            Contains
            Depends
            Exchanges data with
            Hosts
            In Rack
            Instance Of
            Location
            Member
            Powers
            Received data from
            Runs
            Virtualises
            Documents
            Manages
            Backs Up
            Application Installed
        `

        :param submitter: Userid/username of submitter.

        :calls: `POST linkItems`

        :return: Dynamic Item Link ID.
        """
        return self._requester.request(
            method_name="linkItems", params=cleanup_args(locals()), **kwargs
        )


class LinkTickets:
    """Adds basic `linkTickets` functionality to Fooprints object."""

    def link_tickets(
        self,
        first_ticket_definition_id: Union[str, int],
        first_ticket_id: Union[str, int],
        second_ticket_definition_id: Union[str, int],
        second_ticket_id: Union[str, int],
        link_type_name: str,
        submitter: Optional[str] = None,
        **kwargs,
    ):
        """Create a ticket and link assets at the same time.

        :param first_ticket_definition_id: The first ticket definition identifier.

        :param first_ticket_id: The first ticket identifier.

        :param second_ticket_definition_id:ticket second item definition identifier.

        :param second_ticket_id: The second ticket identifier.

        :param link_type_name: The list of values are as follow:

        `Ticket/Contact
            Related Tickets
            Master/Subtask
            Global Link
            Ticket/CI
            Related CIs
            Contract/Service Level Target
            Service/Service Level Target
            Work Target/Service Level Target
            Ticket/Work Target
            Ticket/Service
            Ticket/Asset
            Ticket/Solution
            Ticket/Survey
            Contact/CI
            Related Tickets (Dynamic)
            Connects
            Contains
            Depends
            Exchanges data with
            Hosts
            In Rack
            Instance Of
            Location
            Member
            Powers
            Received data from
            Runs
            Virtualises
            Documents
            Manages
            Backs Up
            Application Installed
        `

        :param submitter: Userid/username of submitter.

        :calls: `POST linkTickets`

        :return: Dynamic Item Link ID.
        """
        return self._requester.request(
            method_name="linkTickets", params=cleanup_args(locals()), **kwargs
        )


class EditCIMixin:
    """Adds basic `editCI` functionality to Footprints object."""

    def update_ci(
        self,
        cmdb_definition_id: str,
        ci_id: Union[str, int],
        ci_fields=list,
        status: str = None,
        submitter: Optional[str] = None,
        **kwargs,
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
        **kwargs,
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
        **kwargs,
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
        **kwargs,
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
