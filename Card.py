import json

class Card:
    KINDS: ['pineapple', 'coconut', 'fig', 'orange', 'rambutan', 'pomegranate',
            'lime', 'avocado', 'carambola', 'acai berry', 'papaya', 'lychee', 'banana']
    CARD_COUNTS: {'pineapple': 3, 'coconut': 6, 'fig': 4, 'orange': 4, 'rambutan': 5,
                  'carambola': 5, 'pomegranate': 6, 'avocado': 5, 'lime': 2, 'acai berry': 6,
                  'papaya': 4, 'lychee': 2, 'banana': 5}
    CARD_BONUS =  {'pineapple': (0, -2, -4), 'coconut': (8, 6, 4, 2, 0, -2), 'fig': (-2, 0, 9, 16),'orange': (4 , 8, 12, 0),
                  'rambutan': (3, 6, 9, 12 ,15), 'lime': (-2, -8), 'carambola': (1, 3, 6, 10, 15),
                  'acai berry': (1, 2, 3, 5, 8, 13), 'lychee': (5, 12)}

    SPETSCARDS = {'banana': (0, 2), 'pomegranate': (-1, 1), 'avocado': (1, 3)}

    def __init__(self, kind):
        if kind not in self.KINDS:
            raise ValueError(f"Invalid card kind: {kind}")
        self.kind = kind

    def __str__(self):
        return f"Card(kind={self.kind})"

    def score(self, kind, multiplier):
        if kind not in self.KINDS:
            raise ValueError(f"Invalid card kind: {kind}")
        return self.CARD_COUNTS[kind] * multiplier

    def save(self):
        return json.dumps({'kind': self.kind})

    @staticmethod
    def load(json_str):
        data = json.loads(json_str)
        return Card(data['kind'])
