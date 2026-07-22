from jsonschema import validate

class SchemaValidator:

    @staticmethod
    def validate_schema(data, schema):
        validate(instance=data, schema=schema)