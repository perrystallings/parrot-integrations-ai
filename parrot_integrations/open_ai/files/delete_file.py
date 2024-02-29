from parrot_integrations.open_ai.files import OBJECT_SCHEMA
def get_details():
    return dict(
        name='',
        description='',
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
                        'file_id'
                    ],
                    properties=dict(
                        file_id=dict(
                            type='string'
                        )
                    )
                ),
                outputs=dict(
                    type='object',
                    additionalProperties=True,
                    required=['file_id'],
                    properties=dict(
                        file_id=dict(
                            type='string'
                        ),
                        deleted=dict(
                            type='boolean'
                        )
                    )
                ),
            )
        )
    )


def process(inputs, integration, **kwargs):
    from parrot_integrations.open_ai import get_client
    client = get_client(integration=integration)
    resp = client.files.delete(file_id=inputs['file_id'])
    return dict(file_id=resp.id, deleted=resp.deleted)
