
class Formatting:
    @staticmethod
    def delete_spaces_in_text(stroke):
            return ''.join(stroke.split())

    @staticmethod
    def normalize_text(text):
        return text.strip()