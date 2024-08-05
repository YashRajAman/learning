import uuid


def generate_fixed_length_uuid(length=22):
    uuid_v4 = uuid.uuid4().hex
    return uuid_v4.zfill(length)

