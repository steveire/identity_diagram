#!/usr/bin/env python

import os, sys

with open("standalone.html", "w") as f:
	with open("unipark-question.html") as g:
		f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Draw your identity</title>
</head>
<body>""")

		f.write(g.read())

		f.write("""
</body>
</html>""")
