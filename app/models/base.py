"""
base.py

Define the base model used by all application models.

Using a common base model provides:

- Shared configuration.
- Consistent validation.
- Easier future extensions.
"""

# Import the Pydantic BaseModel.
from pydantic import BaseModel

# Import ConfigDict.
#
# ConfigDict is used to configure every model.
from pydantic import ConfigDict


class BaseSchema(BaseModel):
    """
    Base class for every application model.
    """

    model_config = ConfigDict(
        # Ignore surrounding whitespace.
        str_strip_whitespace=True,

        # Validate values whenever they are assigned.
        validate_assignment=True,

        # Prevent unexpected extra fields.
        extra="forbid",

        # Freeze can be enabled later if needed.
        frozen=False,
    )