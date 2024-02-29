OBJECT_SCHEMA = dict(
    type='object',
    additionalProperties=False,
    properties=dict(
        run_id=dict(
            type='string'),
        status=dict(
            type='string',
            enum=[
                "queued", "in_progress", "requires_action", "cancelling", "cancelled", "failed", "completed",
                "expired"
            ]
        ),
        thread_id=dict(
            type='string'
        ),
        assistant_id=dict(
            type='string'
        ),
        created_ts=dict(
            type='int'
        ),
        started_ts=dict(
            type='int'
        ),
        completed_ts=dict(
            type='int'
        ),
        failed_ts=dict(
            type='int'
        ),
        metadata=dict(
            type='object',
        )
    )
)


def format_run(run):
    return dict(
        run_id=run.id,
        status=run.status,
        thread_id=run.thread_id,
        assistant_id=run.assistant_id,
        created_ts=run.created_at,
        started_ts=run.started_at,
        completed_ts=run.created_at,
        failed_ts=run.failed_at,
        metadata=run.metadata,
    )
