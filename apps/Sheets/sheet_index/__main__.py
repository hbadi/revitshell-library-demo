"""Prints the sheet list with the parameters named in columns.csv."""
from pathlib import Path

from Autodesk.Revit.DB import FilteredElementCollector, ViewSheet

doc = __revit__.ActiveUIDocument.Document

# One parameter name per line; the column header is the parameter name.
columns = [line.strip() for line in (Path(__file__).parent / "columns.csv").read_text().splitlines()
           if line.strip() and not line.startswith("#")]


def value(sheet, name):
    p = sheet.LookupParameter(name)
    return (p.AsValueString() or p.AsString() or "") if p else ""


sheets = sorted(FilteredElementCollector(doc).OfClass(ViewSheet), key=lambda s: s.SheetNumber)
print("Number".ljust(10) + "Name".ljust(40) + "".join(c.ljust(20) for c in columns))
for s in sheets:
    print(s.SheetNumber.ljust(10) + s.Name[:38].ljust(40) + "".join(value(s, c)[:18].ljust(20) for c in columns))
print(f"{len(sheets)} sheets")
