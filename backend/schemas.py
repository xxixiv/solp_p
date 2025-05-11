from marshmallow import Schema, fields

class ExecuteSchema(Schema):
    source  = fields.Str(required=True)
    lang_id = fields.Int(required=True)
    stdin   = fields.Str(missing="")

class SnippetSchema(Schema):
    id       = fields.Int(dump_only=True)
    source   = fields.Str(required=True)
    lang_id  = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
