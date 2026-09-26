# /// revitshell
# id = "demo.warnings-report"
# version = "1.0.0"
# name = "Warnings report"
# description = "Groups the model warnings by message, most frequent first."
# icon = "google:warning:#F9A825"
# author = "hbadi"
# run = "revit"
# tags = ["model", "qa", "report"]
# requires = ["document"]
# files = ["_report.py"]
# ///
"""Groups the warnings of the active model by message."""
from collections import Counter

from _report import print_table

doc = __revit__.ActiveUIDocument.Document

warnings = list(doc.GetWarnings())
counts = Counter(w.GetDescriptionText() for w in warnings)

print(f"{doc.Title}: {len(warnings)} warnings, {len(counts)} kinds")
print_table(["Count", "Warning"], [(n, text) for text, n in counts.most_common()])
