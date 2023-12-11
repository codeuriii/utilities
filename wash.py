
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
    "\n": ""
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
    if len(chain) != 1:
        chain = chain[0: len(chain) - 1]

        retemp = ""

        for temp in chain:
            retemp += temp
            retemp += "-"
        
        retemp = retemp[0: len(retemp) - 1]

        chain = "".join(retemp)
    
    else:
        chain = "".join(chain)
    
    if chain[0] == " ":
        chain = chain[1:]

    if chain[len(chain) - 1] == " ":
        chain = chain[:len(chain) - 1]

    return chain
