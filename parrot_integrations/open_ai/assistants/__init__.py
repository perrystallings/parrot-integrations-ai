OBJECT_SCHEMA = dict(
    type='object',
    additional_properties=False,
    properties=dict(
        assistant_id=dict(type='string', readOnly=True),
        model_id=dict(type='string'),
        name=dict(type='string'),
        description=dict(type='string'),
        instructions=dict(type='string'),
        file_ids=dict(
            type='array',
            items=dict(
                type='string'
            )
        )
    )
)


def format_assistant(assistant):
    return dict(
        assistant_id=assistant.id,
        description=assistant.description,
        name=assistant.name,
        model_id=assistant.model,
        instructions=assistant.instructions,
        file_ids=assistant.file_ids,
        tools=[str(i) for i in assistant.tools]
    )
