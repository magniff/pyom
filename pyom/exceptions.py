class BoundaryError(Exception):

    def __init__(self, entity, index):
        self.value = entity
        self.index = index
        super().__init__()

    def __str__(self):
        template = 'Invalid memory lookup for entity %s in index %s'
        return template % (self.value, self.index)
