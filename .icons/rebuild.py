#!/usr/bin/env python3
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: chrysn <chrysn@fsfe.org>
# /// script
# dependencies = ["cairosvg"]
# ///

import urllib.request
import cairosvg

game_icons = {
        "board": ("lorc", "circuitry"),
        "app": ("delapouite", "keyboard"),
        "module": ("lorc", "jigsaw-piece"),
        }

for (outname, (author, iconname)) in game_icons.items():
    svg = urllib.request.urlopen(f"https://game-icons.net/icons/000000/ffffff/1x1/{author}/{iconname}.svg").read()
    outname = outname + ".png"
    cairosvg.svg2png(bytestring=svg, write_to=outname, output_width=20, output_height=20)
    with open(outname + ".license", "w") as licensefile:
        # String is split up because reuse tools would otherwise think this applies here
        print("SPDX-License" + "-Identifier: CC-BY-3.0", file=licensefile)
        print(f"SPDX-License-CopyrightText: {author}", file=licensefile)
        print(f"Original file from https://game-icons.net/1x1/{author}/{iconname}.html", file=licensefile)
