"""HTML → clean text preprocessing module.

Uses Trafilatura (main-content extraction) with BeautifulSoup fallback.
Strips boilerplate, nav, ads, and other noise before passing to LLMs.
"""

try:
    import trafilatura
    _TRAFILATURA_AVAILABLE = True
except ImportError:
    _TRAFILATURA_AVAILABLE = False

try:
    from bs4 import BeautifulSoup
    _BS4_AVAILABLE = True
except ImportError:
    _BS4_AVAILABLE = False

MAX_CHARS = 3000


def html_to_main_text(html: str, url: str | None = None) -> str:
    """Extract main content from HTML.

    Tries Trafilatura first for article-quality extraction.
    Falls back to BeautifulSoup stripping of boilerplate tags.
    Returns plain text suitable for passing to an LLM.
    """
    if _TRAFILATURA_AVAILABLE:
        main = trafilatura.extract(
            html,
            url=url,
            include_comments=False,
            include_tables=False,
            favor_recall=False,
        )
        if main and main.strip():
            return main.strip()

    if _BS4_AVAILABLE:
        soup = BeautifulSoup(html, "lxml")
        for tag in soup(["script", "style", "noscript", "nav", "footer", "header", "aside"]):
            tag.decompose()
        text = soup.get_text(separator="\n")
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return "\n".join(lines)

    # Last resort: strip tags with basic string ops
    import re
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate_text(text: str, max_chars: int = MAX_CHARS) -> str:
    """Truncate text to max_chars characters."""
    return text[:max_chars]
