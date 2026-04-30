regex_pattern = r"^(M{,3}(?=([^M]))){,1}(C{,1}M{,1}){,1}(C{,1}D{,3}){,1}(X{,1}C{,3}){,1}(X{,1}L{,1}){,1}(I{,1}X{,3}){,1}(I{1,3}[VX]{,1}|VI{,3}){,1}$"

import re
print(str(bool(re.match(regex_pattern, input()))))