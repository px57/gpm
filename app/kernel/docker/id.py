
def get_container_id(container):
    """
        @description: 
    """
    return container.get("Id", container.get("ID", None))