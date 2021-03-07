def parse(input):
    stack = []
    state = 0x00
    ds = [] # data 
    ss = [] # string 
    es = [] # escape 
    for ch in input:
        cat = catcode[min(ord(ch), 0x7E)]
        state = parse_ch(cat, ch, stack, state, ds, ss, es)
    state = parse_ch(catcode[32], u'', stack, state, ds, ss, es)
    if state != 0x00:
        raise Exception("JSON decode error: truncated")
    if len(ds) != 1:
        raise Exception("JSON decode error: contem muitos objetos")
    return ds.pop()

def parse_ch(cat, ch, stack, state, ds, ss, es):
    while True:
        code = states[state][cat]
        action = code >> 8 & 0xFF
        code   = code      & 0xFF
        if action == 0xFF and code == 0xFF:
            raise Exception("JSON decode error: syntax")
        elif action >= 0x80: 
            stack.append(gotos[state])
            action -= 0x80
        if action > 0:
            do_action(action, ch, ds, ss, es)
        if code == 0xFF:
            state = stack.pop()
        else:
            state = code
            return state

# Esta tabela de ações é única para todas as linguagens ;).
# Também depende de quais estruturas você deseja
# gerando.
def do_action(action, ch, ds, ss, es):
    if action == 0x1:              # lista do push
        ds.append([])
    # Push 
    elif action == 0x2:            # push objeto
        ds.append({})
    elif action == 0x3:            # pop e append
        val = ds.pop()
        ds[len(ds)-1].append(val)
    elif action == 0x4:            # pop pop & setitem
        val = ds.pop()
        key = ds.pop()
        ds[len(ds)-1][key] = val
    elif action == 0x5:           # push null
        ds.append(None)
    elif action == 0x6:           # push true
        ds.append(True)
    elif action == 0x7:           # push false
        ds.append(False)
    elif action == 0x8:           # push string
        val = u"".join(ss)
        ds.append(val)
        ss[:] = [] # apaga ss e es stacks.
        es[:] = []
    elif action == 0x9:
        val = int(u"".join(ss))    # push int
        ds.append(val)
        ss[:] = [] # clear ss stack.
    elif action == 0xA:
        val = float(u"".join(ss))  # push float
        ds.append(val)
        ss[:] = []
    elif action == 0xB:            # push ch to ss
        ss.append(ch)
    elif action == 0xC:            # push ch to es
        es.append(ch)
    elif action == 0xD:            # push escape
        ss.append(unichr(escape_characters[ch]))
    elif action == 0xE:            # push unicode point
        ss.append(unichr(int(u"".join(es), 16)))
        es[:] = []
    else: # É muito improvável que isso aconteça. Mas faça
          # um ponto de colisão aqui, se possível.
          # Além disso, se você escrever em partes, deixe esta linha
          # seja o primeiro a escrever nesta rotina.
        assert False, "JSON BUG"

# Caracteres de escape não triviais. Na pior das hipóteses você pode
# 'switch' ou 'if / else' colcoar eles na função do_action.
escape_characters = {'b': 8, 't': 9, 'n': 10, 'f': 12, 'r': 13}