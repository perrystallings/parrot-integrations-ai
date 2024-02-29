from parrot_integrations.open_ai.messages import OBJECT_SCHEMA, format_message

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
                        'thread_id',
                        'message_id'
                    ],
                    properties=dict(
                        thread_id=dict(type='string'),
                        message_id=dict(type='string'),
                    )
                ),
                outputs=OBJECT_SCHEMA
            )
        )
    )


def process(workflow_uuid, node_uuid, processed_ts, inputs, integration, **kwargs):
    from parrot_integrations.open_ai import get_client
    client = get_client(integration=integration)
    message = client.beta.threads.messages.retrieve(**inputs)
    return format_message(message=message)
