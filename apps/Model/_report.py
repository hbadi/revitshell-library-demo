"""Plain-text tables shared by the report apps of this folder."""


def print_table(headers, rows, max_width=90):
    rows = [[str(c) for c in row] for row in rows]
    widths = [len(h) for h in headers]
    for row in rows:
        widths = [max(w, len(c)) for w, c in zip(widths, row)]
    widths[-1] = min(widths[-1], max_width)

    def line(cells):
        return "  ".join(c[:w].ljust(w) for c, w in zip(cells, widths))

    print(line(headers))
    print("  ".join("-" * w for w in widths))
    for row in rows:
        print(line(row))
