from parrot_integrations.open_ai.runs import OBJECT_SCHEMA, format_run

def get_details():
    return dict(
        name='Get Run',
        description='Get an OpenAI Run details',
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
                        'run_id',
                    ],
                    properties=dict(
                        run_id=dict(
                            type='string',
                        )
                    )
                ),
                outputs=OBJECT_SCHEMA,
            )
        )
    )


def process(inputs, integration, **kwargs):
    from parrot_integrations.open_ai import get_client
    client = get_client(integration=integration)
    run = client.beta.threads.runs.retrieve(run_id=inputs['run_id'])
    return format_run(run=run)
