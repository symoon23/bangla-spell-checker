from main_app.spell_checker.spell import is_banan_correctly
from main_app.spell_checker.spell import suggested_word

class Main:
    def getResult(self, values):
        result = []
        for value in values.split(" "):
            if not is_banan_correctly(value):
                result.append({
                    'correct': False,
                    'query_word': value,
                    'correct_word': str(suggested_word(value))
                })
            else:
                result.append({
                    'correct': True,
                    'query_word': value,
                    'correct_word': value
                })
        return result
