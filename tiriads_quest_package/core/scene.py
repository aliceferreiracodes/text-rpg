class Scene:

    def __init__(self, text, answer_a, answer_b, answer_c, req_skill):
        self._text = text
        self._answer_a = answer_a
        self._answer_b = answer_b
        self._answer_c = answer_c
        self._req_skill = req_skill

    @property
    def text(self):
        return self._text

    @property
    def answer_a(self):
        return f"a. {self._answer_a}"

    @property
    def answer_b(self):
        return f"b. {self._answer_b}"

    @property
    def answer_c(self):
        return f"c. {self._answer_c}"