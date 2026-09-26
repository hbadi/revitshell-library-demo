# /// revitshell
# id = "demo.model-summary"
# version = "1.0.0"
# name = "Model summary"
# description = "Counts walls, doors, windows, floors and sheets in the active model."
# icon = "google:analytics:#00838F"
# author = "hbadi"
# run = "revit"
# tags = ["model", "report"]
# requires = ["document"]
# ///
"""Counts the main element categories of the active model."""
from Autodesk.Revit.DB import BuiltInCategory, FilteredElementCollector

doc = __revit__.ActiveUIDocument.Document

CATEGORIES = [
    ("Walls", BuiltInCategory.OST_Walls),
    ("Doors", BuiltInCategory.OST_Doors),
    ("Windows", BuiltInCategory.OST_Windows),
    ("Floors", BuiltInCategory.OST_Floors),
    ("Sheets", BuiltInCategory.OST_Sheets),
]

print("Model:", doc.Title)
for label, category in CATEGORIES:
    count = (FilteredElementCollector(doc).OfCategory(category)
             .WhereElementIsNotElementType().GetElementCount())
    print(f"  {label:<10}{count:>7}")
