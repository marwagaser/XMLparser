import pandas as pd
import numpy as np
import xml.etree.cElementTree as et

#tree=et.parse('/home/marwagaser/corpora/12_8/LDC2012T09/ara-dialect_eng_para/data/BBN-Dialect_Arabic-English-Web.xml')

tree=et.parse('/home/marwagaser/corpora/12_8/LDC2012T09/ara-dialect_eng_para/data/c.xml')
root=tree.getroot()

src = []
tgt = []
for target in root.iter('TARGET'):
   tgt.append(target.text)
for source in root.iter('SOURCE'):
   src.append(source.text)
with open("/home/marwagaser/corpora/12_8/LDC2012T09/ara-dialect_eng_para/data/LDC2012T09.src", "w") as output:
    output.write("\n".join(map(str, src)))
with open("/home/marwagaser/corpora/12_8/LDC2012T09/ara-dialect_eng_para/data/LDC2012T09.tgt", "w") as output:
    output.write("\n".join(map(str, tgt)))