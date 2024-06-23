



def is_instance_of_any(obj, classes):
    return any(isinstance(obj, cls) for cls in classes)
