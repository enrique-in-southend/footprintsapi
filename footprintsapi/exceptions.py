"""Footprints exceptions.

Contains all expected exceptions returned directly by the API. This does
not necessarily include networking errors, such as a timeout.
"""

from typing import Optional, Union
from http import HTTPStatus


class FootprintsBaseException(Exception):
    """Base class for all errors returned by the Footprints API."""

    def __init__(self, message: Optional[dict] = None):
        """Init function.

        :param message: The message string, dictionary or object containing
        more information about the exception.
        """
        parsed_message = "An unspecified error occured."
        parsed_status_code = HTTPStatus.NOT_ACCEPTABLE

        if message and isinstance(message, dict):
            parsed_message = message.get("message", None)
            parsed_status_code = message.get("status_code", None)

        self.message = parsed_message
        self.status_code = parsed_status_code

    def __str__(self) -> str:
        """Will display string representation."""
        return f"{self.status_code} {self.message}"


class FootprintsException(FootprintsBaseException):
    """Main class for all errors returned by the Footprints API."""

    status_code = HTTPStatus.NOT_IMPLEMENTED
    message = "An unexpected error occured."

    def __init__(
        self,
        message: Union[str, dict, object] = None,
        status_code: Union[str, int] = None,
    ) -> None:
        """Init function."""
        if message and isinstance(message, object):
            try:
                message = dict(
                    message=message.__dict__.get("message", self.message)
                )
            except AttributeError:
                pass

        if isinstance(message, str):
            message = dict(message=message)

        if isinstance(message, dict):
            if "status_code" not in message:
                message["status_code"] = self.status_code

        if not message:
            message = dict(message=self.message, status_code=self.status_code)

        super(FootprintsException, self).__init__(message)


class ItemDefinitionDoesNotExist(FootprintsException):
    """The item definition was not found."""

    status_code = HTTPStatus.BAD_REQUEST
    message = (
        "The item definition was not found. "
        "Please check the item definition."
    )


class BadRequest(FootprintsException):
    """Footprints was unable to understand the request. More information may be needed."""

    status_code = HTTPStatus.BAD_REQUEST
    message = (
        "Footprints was unable to understand the request. "
        "Please check the attributes sent to Footprints."
    )


class Unauthorized(FootprintsException):
    """Footprints API's key is valid, but is unauthorized to access the requested resource."""

    status_code = HTTPStatus.UNAUTHORIZED
    message = "Unauthorized to access the requested resource."


class ResourceDoesNotExist(FootprintsException):
    """Footprints could not locate the requested resource."""

    status_code = HTTPStatus.NOT_FOUND
    message = "Footprints could not locate the requested resource."


class RequiredFieldMissing(FootprintsException):
    """A required field is missing."""

    status_code = HTTPStatus.NOT_ACCEPTABLE
    message = "Required parameter(s) missing."


class Forbidden(FootprintsException):
    """Footprints has denied access to the resource for this user."""

    status_code = HTTPStatus.FORBIDDEN
    message = (
        "Footprints has denied access to the resource. "
        "This is most likely due to a permission issue. "
        "Please check your credentials before proceeding."
    )
