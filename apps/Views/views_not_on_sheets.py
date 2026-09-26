# /// revitshell
# id = "demo.views-not-on-sheets"
# version = "1.0.0"
# name = "Views not on sheets"
# description = "Lists the views placed on no sheet, skipping templates and the view types in skip_types.csv."
# icon = "google:visibility_off:#6A1B9A"
# author = "hbadi"
# run = "revit"
# tags = ["views", "cleanup"]
# requires = ["document"]
# files = ["skip_types.csv"]
# ///
"""Lists the views that are not placed on any sheet."""
from pathlib import Path

from Autodesk.Revit.DB import FilteredElementCollector, View, ViewSheet

doc = __revit__.ActiveUIDocument.Document

# View types to leave out, one ViewType name per line (read next to this file).
skip = {line.strip() for line in (Path(__file__).parent / "skip_types.csv").read_text().splitlines()
        if line.strip() and not line.startswith("#")}



def key(element_id):
    # ElementId.Value since Revit 2024, IntegerValue before.
    return element_id.Value if hasattr(element_id, "Value") else element_id.IntegerValue


placed = set()
for sheet in FilteredElementCollector(doc).OfClass(ViewSheet):
    placed.update(key(i) for i in sheet.GetAllPlacedViews())

orphans = []
for view in FilteredElementCollector(doc).OfClass(View):
    if view.IsTemplate or str(view.ViewType) in skip or key(view.Id) in placed:
        continue
    orphans.append((str(view.ViewType), view.Name))

print(f"{len(orphans)} views on no sheet")
for view_type, name in sorted(orphans):
    print(f"  {view_type:<16}{name}")
