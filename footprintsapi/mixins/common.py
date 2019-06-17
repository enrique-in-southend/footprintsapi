"""Collection of common mixins."""

from ..utils import get_attributes
from footprintsapi.requester import Requester
from typing import Tuple, Optional

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
    "Full Name",
    "CC Email",
    "Internal",
    "Service",
    "Details",
]


class CommonMixin:
    """Common mixin class."""

    def _obj_data(
        self, method_name: str, params: dict, **kwargs
    ) -> Tuple[Requester, dict]:
        """Will wrap data within a FootprintsObject."""
        return (
            self._requester,
            self._requester.request(method_name, params, **kwargs),
        )


class CustomAttributesMixin:
    """Mixin class to get custom attributes."""

    def __init__(
        self, custom_attributes: Optional[list] = CUSTOM_ATTRS
    ) -> None:
        """Find custom attributes relevant to your organization."""
        try:
            attributes = get_attributes(
                fields_to_iterate=self.attributes.get("custom_fields")[
                    "itemFields"
                ],
                attributes_to_fetch=custom_attributes,
            )
        except TypeError:
            pass
