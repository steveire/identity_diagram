#!/usr/bin/env python

import os, sys

with open("identity-standalone.html", "w") as f:
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
</html>
""")

with open("iat-standalone.html", "w") as f:
    with open("unipark-iat.html") as g:
        f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>IAT test</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
</head>
<body>""")

        f.writelines(g.readlines()[:-3])

        f.write("""
<textarea id="jsonInput" name="v_1" cols="80" rows="10"></textarea>
</body>
</html>
""")
