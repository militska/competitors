from Competition import Competition


class CompetitionsSgltn:
    instance = None

    def get_instance(self):
        if self.instance is None:
            self.instance = Competition()
        return self.instance
