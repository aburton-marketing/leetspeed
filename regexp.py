import re

# ---- find spaces only
spaces_p = "[' '][^A-Za-z0-9.()\\{},=<>;:+-]"
spaces_c = re.compile(spaces_p)
# ---- find variables only
params_p = r"\b(?!self,|int|str|bool|tuple|List\b)[^\s,{}: -]\w*"
params_c = re.compile(params_p)
# ---- find name of main function
defname_p = r"[^def ]*\w*\b[$(]"
defname_c = re.compile(defname_p)
# ---- find filename
filename_p = ""
filename_c = re.compile(filename_p)