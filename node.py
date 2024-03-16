import sys
import os

sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)

class ShowText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "text": ("STRING"),
            },
        }

    FUNCTION = "show_text"
    CATEGORY = "MK/text"

    def show_text(self, text):
        return {"ui": {"text": [text,]}}

class CombinationText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True}),
                "text2": ("STRING", {"multiline": True}),
                "connector": ("STRING", {"default": ","}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "combination_text"

    CATEGORY = "MK/text"

    def combination_text(self, text1, text2, connector):
        texts = [text1, text2]
        combined_text = connector.join(texts)
        return (combined_text,)

class PlaceholderText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text1": ("STRING", {"multiline": True}),
                "text2": ("STRING", {"multiline": True}),
                "placeholder": ("STRING", {"default": "$1,$2"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "placeholder_text"

    CATEGORY = "MK/text"

    def placeholder_text(self, text1, text2, placeholder):
        replacements = {"$1": text1, "$2": text2}

        for old, new in replacements.items():
            placeholder = placeholder.replace(old, new)

        return (placeholder,)


class ReplaceText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "old_string": ("STRING",),
                "new_string": ("STRING",),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    FUNCTION = "replace_text"

    CATEGORY = "MK/text"

    def replace_text(self, text, old_string, new_string):

        text = text.replace(old_string, new_string)

        return (text,)