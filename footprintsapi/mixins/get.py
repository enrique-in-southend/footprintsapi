"""Collection of pure get mixins."""

from typing import Union, Optional
from ..utils import cleanup_args


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
            method_name="getItemDetails",
            params=cleanup_args(locals()),
            **kwargs,
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
            method_name="listItemDefinitions",
            params=cleanup_args(locals()),
            **kwargs,
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
            method_name="listFieldDefinitions",
            params=cleanup_args(locals()),
            **kwargs,
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
            method_name="listQuickTemplates",
            params=cleanup_args(locals()),
            **kwargs,
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
        self,
        search_id: Union[str, int],
        submitter: Optional[str] = None,
        **kwargs,
    ) -> list:
        """Retrive searches.

        :param search_id: You can retrieve the item_type_name parameter to get the item
        ID to run the search query from the existing Saved Searches only.

        :param submitter: Userid/username of submitter.
        """
        return self._requester.request(
            method_name="runSearch", params=cleanup_args(locals()), **kwargs
        )
