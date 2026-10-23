"""Builds GUIDE.md, SOURCES.md and pin.txt from index.html, so all four always match."""
import re, html, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text(encoding="utf8")
main = src.split("<main")[1].split("</main>")[0]

def clean(s):
    s = re.sub(r'<a class="ref"[^>]*>(.*?)</a>', r' \1', s)
    s = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"[{re.sub('<[^>]+>','',m.group(2))}]({m.group(1)})", s)
    s = re.sub(r'<(?:b|strong|span class="btn")[^>]*>(.*?)</(?:b|strong|span)>', r'\1', s)
    s = re.sub(r'<[^>]+>', '', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

out = ["# KYC and Wallet Activation Explainer", "", "Generated from index.html by scripts/build.py. Edit index.html, not this file.", ""]
body = re.sub(r'<pre.*?</pre>', '', main, flags=re.S)
body = body.split('<h2 id="sources">')[0]
def number(m):
    n = [0]
    def f(_):
        n[0] += 1
        return f"<li>{n[0]}. "
    return re.sub(r"<li>", f, m.group(0))
body = re.sub(r"<ol.*?</ol>", number, body, flags=re.S)
for m in re.finditer(r'<h2[^>]*>(.*?)</h2>|<h3[^>]*>(.*?)</h3>|<table>(.*?)</table>|<(p|li)[^>]*>(.*?)</\4>', body, re.S):
    h2, h3, tab, tag, txt = m.groups()
    if h2: out += ["", "## " + clean(h2), ""]
    elif h3: out += ["", "### " + clean(h3), ""]
    elif tab:
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', tab, re.S)
        for i, r in enumerate(rows):
            cells = [clean(c) for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.S)]
            out.append("| " + " | ".join(cells) + " |")
            if i == 0: out.append("|" + "---|" * len(cells))
        out.append("")
    elif tag == "li": out.append(clean(txt) if re.match(r"\d+\. ", clean(txt)) else "- " + clean(txt))
    elif clean(txt): out += [clean(txt), ""]
(root / "GUIDE.md").write_text("\n".join(out) + "\n", encoding="utf8")

tab = main.split('<h2 id="sources">')[1].split("</table>")[0]
rows = ["# Sources", "", "Last verified: 23 October 2026. Official means published by Redbelly Network, Averer or the Redbelly DAO. Community means unconfirmed.", "", "| ID | Status | What it supports | Link |", "|---|---|---|---|"]
for r in re.findall(r'<tr id[^>]*>(.*?)</tr>', tab, re.S):
    c = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
    link = re.search(r'href="([^"]+)"', c[3]).group(1)
    rows.append(f"| {clean(c[0])} | {clean(c[1])} | {clean(c[2])} | {link} |")
(root / "SOURCES.md").write_text("\n".join(rows) + "\n", encoding="utf8")

pin = html.unescape(re.search(r'<pre class="pin"[^>]*>(.*?)</pre>', main, re.S).group(1))
(root / "pin.txt").write_text(pin.strip() + "\n", encoding="utf8")
print("built GUIDE.md, SOURCES.md, pin.txt")
