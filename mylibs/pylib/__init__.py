from __future__ import absolute_import
from __future__ import print_function
import six

def pritty_print(dictObj, indent=0, space=4, maxchars=80, isValue=False, isKey=False, noIndent=False):
    blank = ' ' * indent * space
    start_symbol, end_symbol = '', ''
    start = lambda: '%s%s' %(blank, start_symbol) if not noIndent else ' %s' % start_symbol
    end = lambda: '%s%s,' % (blank, end_symbol) if indent else '%s%s' % (blank, end_symbol)

    if isinstance(dictObj, dict):
        start_symbol, end_symbol = '{', '}'
        if not dictObj:
            print(start() + end())
            return

        print(start())
        for key, value in dictObj.items():
            pritty_print(key, indent=indent+1, isValue=False, isKey=True)
            pritty_print(value, indent=indent+1, isValue=True, noIndent=True)
        print(end())
        return

    if isinstance(dictObj, list):
        start_symbol, end_symbol = '[', ']'
        if not dictObj:
            print(start() + "],")
            return

        print(start())
        for value in dictObj:
            pritty_print(value, indent=indent+1, isValue=True)
        print(end())
        return

    blank = ' ' if noIndent else blank
    fmt = blank + '{0}' + (',\n' if isValue else ':')

    def truncate(strObj, length):
        if isKey or strObj is None:
            return strObj
        if length == -1 or len(strObj) < length:    # show all
            return strObj
        return (strObj[:30] + " ... " + strObj[-30:])

    m = ''
    while True:
        if isinstance(dictObj, six.integer_types):
            m = int(dictObj)
            break

        if dictObj is None or isinstance(dictObj, six.string_types):
            m = "\"%s\"" % truncate(dictObj, maxchars)
            break

        try:
            m = str(dictObj)
        except:
            m = "%s" % type(dictObj)
        break

    print(fmt.format(m), end='')
    return
