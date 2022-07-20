"""

 ██▓    ▄▄▄    ██▒   █▓ ▄▄▄          ██▓    ▓█████ ▒██   ██▒▓█████  ██▀███  
▓██▒   ▒████▄ ▓██░   █▒▒████▄       ▓██▒    ▓█   ▀ ▒▒ █ █ ▒░▓█   ▀ ▓██ ▒ ██▒
▒██░   ▒██  ▀█▄▓██  █▒░▒██  ▀█▄     ▒██░    ▒███   ░░  █   ░▒███   ▓██ ░▄█ ▒
▒██░   ░██▄▄▄▄██▒██ █░░░██▄▄▄▄██    ▒██░    ▒▓█  ▄  ░ █ █ ▒ ▒▓█  ▄ ▒██▀▀█▄  
░██████▒▓█   ▓██▒▒▀█░   ▓█   ▓██▒   ░██████▒░▒████▒▒██▒ ▒██▒░▒████▒░██▓ ▒██▒
░ ▒░▓  ░▒▒   ▓▒█░░ ▐░   ▒▒   ▓▒█░   ░ ▒░▓  ░░░ ▒░ ░▒▒ ░ ░▓ ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░ ▒  ░ ▒   ▒▒ ░░ ░░    ▒   ▒▒ ░   ░ ░ ▒  ░ ░ ░  ░░░   ░▒ ░ ░ ░  ░  ░▒ ░ ▒░
  ░ ░    ░   ▒     ░░    ░   ▒        ░ ░      ░    ░    ░     ░     ░░   ░ 
    ░  ░     ░  ░   ░        ░  ░       ░  ░   ░  ░ ░    ░     ░  ░   ░     
                   ░                                                        
"""
import ply.lex as lex

class Lex(object): 
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'elif':'ELSEIF',
        'while': 'WHILE',
        'for' : "FOR",
        'int' : "INTEGER",
        "float" : "FLOAT",
        "str" : "STR",
        'input': 'INPUT',
        'print': 'PRINT',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'true': 'TRUE',
        'false': 'FALSE',
    }
    #tokens + reserved keywords
    tokens = ('NOTEQUAL',
                'GE',
                'LE',
                'ASSIGN',
                'SYMBOL',
                'FLOAT',
                'INT',
                'STRING',
                'NE',)+ tuple(reserved.values())
    #assigning the operator and assigner literals
    t_NOTEQUAL = r'<>'
    t_ASSIGN = r'='
    t_GE = r'>='
    t_LE = r'<='
    t_NE = r'!='

    literals = (
        '>',
        '<',
        '=',
        '+',
        '-',
        '*',
        '/',
        '^',
        '{',
        '}',
        '[',
        ']',
        '(',
        ')',
        ':',
        ';',
        ',',
    )

    #find collumn
    def find_column(self,t):
        last_cr = t.lexer.lexdata.rfind('\n', 0, t.lexpos)
        if last_cr < 0:
            last_cr = 0
        column = (t.lexpos - last_cr) + 1
        return column

    # Track line numbers
    def token_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    #error rule
    # Prints an error output for illegal token
    def token_error(self,t):
        print( "Illegal character '" , "{}" , "' in line {} column {}").format(t.value[0], t.lineno, self.find_column(t))
        t.lexer.skip(1)

    #simple single line comments
    def t_COMMENT(self,t):
        r'\//.*'
        pass


    # Read in a float. This rule has to be done before the int rule.
    def t_FLOAT(self,t):
        r'\d+\.\d*(e-?\d+)?'
        t.value = float(t.value)
        return t


    # Read in an int
    def t_INT(self,t):
        r'\d+'
        t.value = int(t.value)
        return t


    # Strings, It works, dont mess with it
    def t_STRING(self,t):
        r'\"([^\\"]|(\\.))*\"'
        escaped = 0
        # Remove first and last double quotations
        old_str = t.value[1:-1]
        new_str = ""
        for i in range(0, len(old_str)):
            c = old_str[i]
            if escaped:
                if c == "n":
                    c = "\n"
                elif c == "t":
                    c = "\t"
                new_str += c
                escaped = 0
            else:
                if c == "\\":
                    escaped = 1
                else:
                    new_str += c
        t.value = new_str
        return t


    # Read in a symbol. This rule must be practically last since there are so
    # few rules concerning what constitutes a symbol
    def t_SYMBOL(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        # See if symbol is a reserved keyword
        t.type = self.reserved.get(t.value, 'SYMBOL')
        return t

    #ignoring all the whitespaces + assiging the error thing

    t_ignore = '\n'
    t_error = token_error

    #Building the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    #testing the lexer
      # Test it output
    def run(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)