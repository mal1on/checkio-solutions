import unicodedata

def checkio(in_string):

   return ''.join(c for c in unicodedata.normalize('NFD', in_string) if unicodedata.category(c) != 'Mn')



checkio(u"préfèrent") == u"preferent"
checkio(u"loài trăn lớn") == u"loai tran lon"
checkio("完好無缺")
