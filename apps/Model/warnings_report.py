"""Groups the warnings of the active model by message."""
from collections import Counter

from _report import print_table

doc = __revit__.ActiveUIDocument.Document

warnings = list(doc.GetWarnings())
counts = Counter(w.GetDescriptionText() for w in warnings)

print(f"{doc.Title}: {len(warnings)} warnings, {len(counts)} kinds")
print_table(["Count", "Warning"], [(n, text) for text, n in counts.most_common()])
