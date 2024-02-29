OBJECT_SCHEMA = dict(
    type='object',
    additionalProperties=False,
    required=[
        'content',
        'role'
    ],
    properties=dict(
        message_id=dict(
            type='string'
        ),
        content=dict(
            type='string'
        ),
        role=dict(
            type='string',
            enum=['user']
        ),
        file_ids=dict(
            type='array',
            items=dict(
                type='string'
            )
        ),
        metadata=dict(
            type='object'
        )
    )
)


def format_message(message):
    return dict(

    )
