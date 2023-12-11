
blackdict = {
    "ç": "c",
    "/": "-",
    ":": "-",
    "*": "-",
    "<": "",
    ">": "",
    '"': "",
    "'": "",
    "|": "-",
    "\\": "-",
    "²": "",
    "é": "e",
    "~": "-",
    "{": "(",
    "[": "(",
    "}": ")",
    "]": ")",
    "£": "",
    "$": "",
    "¤": "",
    "µ": "",
    "%": "",
    "ù": "u",
    "!": "",
    "§": "",
    "&": "",
    "#": "-",
    "à": "a",
    "=": "-",
    "°": "",
    "+": "-",
    "`": "",
    "@": "a",
    "è": "e",
    "^": "",
    "¨": "",
    "?": "",
    ",": "",
    ";": "-",
    "  ": " ",
}

def wash(chain: str):

    svgd = chain
    
    while True:
        for black, white in blackdict.items():
            chain = chain.replace(black, white)
        
        if svgd == chain:
            break
        else:
            svgd = chain


    chain = chain.split('.')
    chain = chain[0: len(chain) - 1]

    retemp = ""

    for temp in chain:
        retemp += temp
        retemp += "-"
    
    retemp = retemp[0: len(retemp) - 1]

    chain = "".join(retemp)
    
    if chain[0] == " ":
        chain = chain[1:]

    return chain

print(wash("    sal  ùù ut.dd.d"))
