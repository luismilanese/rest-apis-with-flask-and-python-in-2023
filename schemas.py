from marshmallow import Schema, fields


class ItemSchema(Schema):
    # dump_only só é usado no retorno da API. No save não será mandado o ID.
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    # Não são required pois usuário pode mandar só um ou outro
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    # dump_only só é usado no retorno da API. No save não será mandado o ID.
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
