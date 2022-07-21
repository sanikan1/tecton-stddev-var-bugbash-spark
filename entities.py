from tecton import Entity


user = Entity(
    name='user',
    join_keys=['user_id'],
    description='A user of the platform',
    owner='david@tecton.ai',
    tags={'release': 'production'}
)
