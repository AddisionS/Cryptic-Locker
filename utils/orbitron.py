from tkextrafont import Font

_loaded = False
_font_family = "Orbitron"
_font_path = "../assets/fonts/Orbitron-VariableFont_wght.ttf"
_font_cache = {}

def orbitron(size):
    global _loaded

    if not _loaded:
        # Load only once globally (no need to cache with size here)
        Font(file=_font_path, family=_font_family)
        _loaded = True

    if size not in _font_cache:
        _font_cache[size] = (_font_family, size)

    return _font_cache[size]
