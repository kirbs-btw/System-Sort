import sqlite3

class colorPal:
    """
    color pal obj change values for color mode
    """
    def __init__(self, main="#ffffff", sec="#ffffff", accent="#ffffff", colLight="#ffffff", colDark="#ffffff", text="#000000"):
        self.main = main
        self.sec = sec
        self.accent = accent
        self.colLight = colLight
        self.colDark = colDark
        self.text = text

colPal = colorPal()

def main():
    """
    check for mode in table
    :return:
    """

    conn = sqlite3.connect("mode.sql")
    cur = conn.cursor()

    command = "SELECT * FROM mode"
    table = cur.execute(command).fetchall()[0]

    mode = table[0]

    if mode == "nrml":
        mainCol = "#ededed"
        mainColBlue = "#599fd7"
        accentColor = "#ea498b"
        lightBlue = "#a3d8e6"

    elif mode == "drkmd":
        # new color pal
        mainColor = "#0F0F0F"  # dark black
        secColor = "#202020"  # light dark grey
        terzColor = "#8E8E8E"  # light grey
        accentColor = "#599FD7"  # accent blue


if __name__ == '__main__':
    main()