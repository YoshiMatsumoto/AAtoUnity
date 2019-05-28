import rhinoscriptsyntax as rs
import re

def main():
    # prompt the user for a file to import
    filter = "mif file (*.mif)|*.mif|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open shape File", filter)
    if not filename:
        return
    # make line list
    lineLn = []

    with open(filename, "r") as f:
        r = re.compile("LINE (.+)")
        for ln in f:
            m = r.search(ln)
            if m != None:
                ln = m.group(1)
                lineLn.append(ln)

    # line to rhinoLine
    sgLn = []
    for i in lineLn:
        i = i.split()
        startPn = rs.AddPoint((i[0], i[1], 0))
        endPn = rs.AddPoint((i[2], i[3], 0))
        segment = rs.AddLine(startPn, endPn)
        sgLn.append(segment)


if __name__ == '__main__':
    main()
