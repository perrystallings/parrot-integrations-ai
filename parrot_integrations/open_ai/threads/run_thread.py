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
                        'assistant_id'
                    ],
                    properties=dict(
                    )
                ),
                outputs=dict(
                    type='object',
                    additionalProperties=True,
                    required=[],
                    properties=dict()
                ),
            )
        )
    )


def process(workflow_uuid, node_uuid, processed_ts, inputs, integration, **kwargs):
    from parrot_integrations.open_ai import get_client
    client = get_client(integration=integration)
    run = client.beta.threads.runs.create(
        thread_id=inputs['thread_id'],
        assistant_id=inputs['assistant_id']
    )
