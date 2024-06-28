import json

class Card:
    KINDS: ['pineapple', 'coconut', 'fig', 'orange', 'rambutan', 'pomegranate',
            'lime', 'avocado', 'carambola', 'acai berry', 'papaya', 'lychee', 'banana']
    CARD_COUNTS: {'pineapple': 3, 'coconut': 6, 'fig': 4, 'orange': 4, 'rambutan': 5,
                  'carambola': 5, 'pomegranate': 6, 'avocado': 5, 'lime': 2, 'acai berry': 6,
                  'papaya': 4, 'lychee': 2, 'banana': 5}
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
