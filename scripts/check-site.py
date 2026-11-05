"""Build the site and check the homepage's local links and assets."""

from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import unquote, urlsplit
import subprocess
import sys


class Homepage(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.urls = set()
        self.canonical_host = ""

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        for name in ("href", "src"):
            if attributes.get(name):
                self.urls.add(attributes[name])
        for candidate in attributes.get("srcset", "").split(","):
            if candidate.strip():
                self.urls.add(candidate.split()[0])
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical_host = urlsplit(attributes.get("href", "")).netloc
        if tag == "meta" and attributes.get("property") == "og:image":
            if attributes.get("content"):
                self.urls.add(attributes["content"])


def check_homepage(site):
    site = site.resolve()
    index = site / "index.html"
    if not index.is_file():
        return ["Missing homepage: index.html"]

    page = Homepage()
    page.feed(index.read_text(encoding="utf-8"))
    errors = []
    for url in sorted(page.urls):
        parts = urlsplit(url)
        if parts.scheme not in ("", "http", "https"):
            continue
        if parts.netloc and parts.netloc != page.canonical_host:
            continue
        target = (site / (unquote(parts.path).lstrip("/") or "index.html")).resolve()
        if target.is_dir():
            target /= "index.html"
        if site not in target.parents or not target.is_file():
            errors.append(f"Missing local file: {url}")
        elif target == index and parts.fragment and unquote(parts.fragment) not in page.ids:
            errors.append(f"Missing homepage anchor: {url}")
    return errors


def main():
    repo = Path(__file__).resolve().parents[1]
    with TemporaryDirectory(prefix="homepage-check-") as destination:
        build = subprocess.run(
            ["bundle", "exec", "jekyll", "build", "--destination", destination],
            cwd=repo,
            check=False,
        )
        if build.returncode:
            return build.returncode
        errors = check_homepage(Path(destination))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Homepage links and assets passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
