from Competition import Competition


class CompetitionsSgltn:
    instance = None

    def get_instance(self, n):
        print("line 14; param " + str(n))
        if self.instance is None:
            print("line 16; param " + str(n))
            self.instance = Competition()
        return self.instance
