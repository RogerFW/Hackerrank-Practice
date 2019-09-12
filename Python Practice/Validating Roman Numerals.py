regex_pattern = r""	# Do not delete 'r'.
regex_pattern += r"M{0,3}"                  # 0 à 3000
regex_pattern += r"(C[DM]|D?C{0,3})"        # 400,900 ou 0..300,500.. 800
regex_pattern += r"(X[LC]|L?X{0,3})"        # idem pour les dizaines
regex_pattern += r"(I[VX]|V?I{0,3})"        # idem pour les unités
regex_pattern += r"$"
import re
print(str(bool(re.match(regex_pattern, input()))))
