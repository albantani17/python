import re

txt = "Hujan di Pandeglang"
x = re.search("\s", txt)

print("spasi pertama terletak di",x.start())