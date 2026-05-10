
class Formatting:
    # Утилита для удаления всех пробелов в строке
    @staticmethod
    def delete_spaces_in_text(stroke):
            return ''.join(stroke.split())

    # Утилита для удаления пробелов в начале или конце строки
    @staticmethod
    def normalize_text(text):
        return text.strip()