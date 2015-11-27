class MyArray(object):

    def flat(self, an_array):
        return self.flat_rec(an_array)

    def flat_rec(self, an_array):
        if not an_array:
            return []
        elif isinstance(an_array, list):
            head, *tail = an_array
            return self.flat(head) + self.flat(tail)
        else:
            return [an_array]
