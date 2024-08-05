import uuid


def getUserId(length=10):
    uuid_v4 = uuid.uuid4().hex
    return uuid_v4.zfill(length)