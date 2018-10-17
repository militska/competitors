class ContextStrategy:
    strategy = None

    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, **kwargs):
        return self.strategy.execute(**kwargs)
