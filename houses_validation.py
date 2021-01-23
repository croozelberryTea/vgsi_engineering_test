from marshmallow import Schema, fields


class BaseSchema(Schema):
    """
    Simple marshmallow based schema validation primarily for the put method. All fields are required.
    """

    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    street = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    zip = fields.Int(required=True)
    propertyType = fields.Str(required=True)
    location = fields.Url(required=True)
