def get_cookie(cookie, name):
    return "value"




get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light'
get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true'
