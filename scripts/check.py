"""Checks the guide: no dashes, no emoji, source ids exist, pin matches the guide."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
bad = 0
def fail(m):
    global bad; bad += 1; print("FAIL:", m)
for name in ["index.html", "GUIDE.md", "SOURCES.md", "pin.txt", "README.md"]:
    t = (root / name).read_text(encoding="utf8")
    for ch in set(t):
        o = ord(ch)
        if o in (0x2013, 0x2014): fail(f"{name}: en or em dash")
        if o >= 0x1F300 or 0x2600 <= o <= 0x27BF or 0x2190 <= o <= 0x21FF: fail(f"{name}: emoji or arrow {hex(o)}")
html = (root / "index.html").read_text(encoding="utf8")
defined = set(re.findall(r'<tr id="([se]\d+)"', html))
cited = set(i.lower() for i in re.findall(r'\[([SE]\d+)\]', re.sub(r'<[^>]+>', '', html)))
for i in sorted(cited - defined): fail(f"cited but not listed: {i}")
for i in sorted(defined - cited): print("note: listed but never cited:", i)
pin = (root / "pin.txt").read_text(encoding="utf8"); guide = (root / "GUIDE.md").read_text(encoding="utf8")
for need in ["few minutes", "few days", "10 per verified identity", "Account allocation exhausted", "18 listed jurisdictions", "tickets/new"]:
    if need not in pin: fail(f"pin missing: {need}")
for need in ["few minutes", "Account allocation exhausted", "tickets/new", "Begin identity verification", "Enable account"]:
    if need not in guide: fail(f"guide missing: {need}")
if "support/login" in html + pin + guide: fail("Averer login link still present")
if "No fixed time" in html: fail("old Q3 answer still present")
print("OK" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
