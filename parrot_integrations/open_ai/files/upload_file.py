from parrot_integrations.open_ai.files import OBJECT_SCHEMA, format_file


def get_details():
    return dict(
        name='Upload File',
        description='Upload File to OpenAI',
        is_trigger=False,
        schema=dict(
            type='object',
            additionalProperties=False,
            description='',
            required=['inputs', 'outputs'],
            properties=dict(
                inputs=dict(
                    type='object',
                    additionalProperties=False,
                    required=[
                        'purpose',
                        'file'
                    ],
                    properties=dict(
                        file=dict(
                            type='string',
                            format='binary'
                        ),
                        purpose=dict(
                            type='string',
                            enum=['assistants',
                                  'fine-tune']
                        )
                    )
                ),
                outputs=OBJECT_SCHEMA
            )
        )
    )


def process(inputs, integration, **kwargs):
    from parrot_integrations.open_ai import get_client
    client = get_client(integration=integration)
    file = client.files.create(
        purpose=inputs['purpose'],
        file=inputs['file']
    )
    return format_file(file=file)
