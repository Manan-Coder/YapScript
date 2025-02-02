'''YapScript - a fun toy programming language
   Made by - Manan
   CLI version - 1.0.0
   Drop me an email at manancoder@gmail.comm if you find any bug, or just to say hi ; )
    '''


import re
from enum import Enum
from math import sqrt, factorial

#---------------Tokenization
class TokenType(Enum):
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    OPERATOR = 'OPERATOR'
    EQUALS = 'EQUALS'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    SEMICOLON = 'SEMICOLON'
    COMMA = 'COMMA'
    EOF = 'EOF'


KEYWORDS = {
    'yap': 'PRINT',
    'kick_off': 'LET',
    'ohhReally': 'IF',
    'nahMan': 'ELSE',
    'tellMe': 'INPUT',
    'letHimCook': 'FUNCTION',
    'LoopyLoopy': 'FOR',
    'whileWeAt': 'WHILE',
    'gimme': 'RETURN',
    'solve': 'SOLVE',
    'solve_quad': 'SOLVE_QUAD',
    'convert': 'CONVERT',
    'resistance': 'RESISTANCE',
    'balance': 'BALANCE',
    'element_info': 'ELEMENT_INFO',
    'table': 'TABLE',
    'gas_law': 'GAS_LAW',
    'factorial': 'FACTORIAL'
}



OPERATORS = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    '<': 'LESS_THAN',
    '>': 'GREATER_THAN',
    '<=': 'LESS_THAN_OR_EQUAL',
    '>=': 'GREATER_THAN_OR_EQUAL',
    '==': 'EQUALS_EQUALS',
    '!=': 'NOT_EQUALS'
}



#-----------------lexer code
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.pos = 0
    def generate_tokens(self):
        while self.pos < len(self.source_code):
            char = self.source_code[self.pos]
            if char == '&':  
                self.pos += 1
                continue
            if char.isspace():
                self.pos += 1
            elif char.isdigit():
                self.tokens.append(self.generate_number())
            elif char == '"':
                self.tokens.append(self.generate_string())
            elif char.isalpha() or char == '_':
                self.tokens.append(self.generate_identifier_or_keyword())
            elif char in OPERATORS or (char in ['<', '>', '=', '!'] and self.pos + 1 < len(self.source_code) and self.source_code[self.pos + 1] == '='):
                self.tokens.append(self.generate_operator())
            elif char == '=':
                self.tokens.append(self.generate_equals())
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON))
                self.pos += 1
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, '('))
                self.pos += 1
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')'))
                self.pos += 1
            elif char == '{':
                self.tokens.append(Token(TokenType.LBRACE, '{'))
                self.pos += 1
            elif char == '}':
                self.tokens.append(Token(TokenType.RBRACE, '}'))
                self.pos += 1
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA))
                self.pos += 1
            else:
                raise ValueError(f"Cannot find anything like {char} , maybe make a new ASCII or Unicode character for it ; )")
        self.tokens.append(Token(TokenType.EOF))
        return self.tokens
    

    def generate_number(self):
        num_str = ''
        decimal_count = 0
        while self.pos < len(self.source_code) and (self.source_code[self.pos].isdigit() or self.source_code[self.pos] == '.'):
            if self.source_code[self.pos] == '.':
                decimal_count += 1
                if decimal_count > 1:
                    raise ValueError("Yo yo yo you son of a biscuit eater!!! you have entered more than one decimals!!")
            num_str += self.source_code[self.pos]
            self.pos += 1
        if decimal_count == 0:
            return Token(TokenType.NUMBER, int(num_str))
        return Token(TokenType.NUMBER, float(num_str))
    

    def generate_string(self):
        self.pos += 1  
        string = ''
        while self.pos < len(self.source_code) and self.source_code[self.pos] != '"':
            string += self.source_code[self.pos]
            self.pos += 1
        if self.pos >= len(self.source_code):
            raise ValueError("Cannot generate string thingy, you forgot to close the string with a double quote")
        self.pos += 1  
        return Token(TokenType.STRING, string)
    

    def generate_identifier_or_keyword(self):
        identifier = ''
        while self.pos < len(self.source_code) and (self.source_code[self.pos].isalnum() or self.source_code[self.pos] == '_'):
            identifier += self.source_code[self.pos]
            self.pos += 1
        if identifier in KEYWORDS:
            return Token(TokenType.KEYWORD, KEYWORDS[identifier])
        return Token(TokenType.IDENTIFIER, identifier)
    

    def generate_operator(self):
        op = self.source_code[self.pos]
        if (self.pos + 1 < len(self.source_code) and 
            self.source_code[self.pos:self.pos + 2] in ['==', '!=', '<=', '>=']):
            op = self.source_code[self.pos:self.pos + 2]
            self.pos += 2
        else:
            self.pos += 1
        return Token(TokenType.OPERATOR, OPERATORS[op])
    

    def generate_equals(self):
        if self.pos + 1 < len(self.source_code) and self.source_code[self.pos + 1] == '=':
            self.pos += 2
            return Token(TokenType.OPERATOR, OPERATORS['=='])
        self.pos += 1
        return Token(TokenType.EQUALS, '=')
    

    def peek(self):
        if self.pos < len(self.source_code):
            return self.source_code[self.pos]
        return None
    
    
#----------------astnode code
class ASTNode:
    pass
class PrintNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression
class AssignmentNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value
class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value
class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
class VariableNode(ASTNode):
    def __init__(self, name):
        self.name = name
class STEMFunctionNode(ASTNode):
    def __init__(self, func_name, arguments):
        self.func_name = func_name
        self.arguments = arguments
class IfNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition            
        self.then_branch = then_branch        
        self.else_branch = else_branch        
class ForNode(ASTNode):
    def __init__(self, initializer, condition, increment, body):
        self.initializer = initializer        
        self.condition = condition            
        self.increment = increment            
        self.body = body                      
class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition            
        self.body = body   
#-----------------parser code
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    def parse(self):
        statements = []
        while self.pos < len(self.tokens) and self.tokens[self.pos].type != TokenType.EOF:
            statements.append(self.parse_statement())
        return statements
    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    def advance(self):
        token = self.peek()
        self.pos += 1
        return token
    def expect(self, token_type):
        token = self.advance()
        if token.type != token_type:
            raise SyntaxError(f"I wanted {token_type}, you gave {token.type}")
        return token
    def parse_statement(self):
        token = self.peek()
        if token.type == TokenType.KEYWORD:
            if token.value == 'PRINT':
                return self.parse_print_statement()
            elif token.value == 'LET':
                return self.parse_variable_declaration()
            elif token.value in ['SOLVE', 'SOLVE_QUAD', 'CONVERT', 'RESISTANCE', 
                                'BALANCE', 'ELEMENT_INFO', 'TABLE', 'GAS_LAW', 'FACTORIAL']:
                node = self.parse_stem_function()
                self.expect(TokenType.SEMICOLON)
                return node
        raise SyntaxError(f"Cannot find anything like {token} , pls read the docs")
    def parse_print_statement(self):
        self.advance()  
        expression = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return PrintNode(expression)
    def parse_variable_declaration(self):
        self.advance()  
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.EQUALS)
        value = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        return AssignmentNode(name, value)
    def parse_stem_function(self):
        func_token = self.advance()
        self.expect(TokenType.LPAREN)
        args = self.parse_arguments()
        self.expect(TokenType.RPAREN)
        return STEMFunctionNode(func_token.value, args)
    def parse_arguments(self):
        args = []
        while self.peek() and self.peek().type != TokenType.RPAREN:
            args.append(self.parse_expression())
            if self.peek() and self.peek().type == TokenType.COMMA:
                self.advance()
        return args
    def parse(self):
        statements = []
        while self.pos < len(self.tokens) and self.tokens[self.pos].type != TokenType.EOF:
            statements.append(self.parse_statement())
        return statements
    def parse_block(self):
        self.expect(TokenType.LBRACE)
        statements = []
        while self.peek() and self.peek().type != TokenType.RBRACE:
            statements.append(self.parse_statement())
        self.expect(TokenType.RBRACE)
        return statements
    def parse_if_statement(self):
        self.advance()  
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        then_branch = self.parse_block()
        else_branch = None
        if self.peek() and self.peek().type == TokenType.KEYWORD and self.peek().value == 'ELSE':
            self.advance()  
            else_branch = self.parse_block()
        return IfNode(condition, then_branch, else_branch)
    def parse_for_statement(self):
        self.advance()  
        self.expect(TokenType.LPAREN)
        initializer = self.parse_statement()      
        condition = self.parse_expression()
        self.expect(TokenType.SEMICOLON)
        increment = self.parse_expression()
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        return ForNode(initializer, condition, increment, body)
    def parse_while_statement(self):
        self.advance()  
        self.expect(TokenType.LPAREN)
        condition = self.parse_expression()
        self.expect(TokenType.RPAREN)
        body = self.parse_block()
        return WhileNode(condition, body)

#----------stem code
class stem_ops:
    @staticmethod
    def solve_linear(exn):
        try:
            lhs, rhs = exn.split('=')
            lhs = lhs.strip().replace(' ', '')
            rhs = rhs.strip()
            coeff = 1
            const = 0
            var = 'x'
            if '+' in lhs:
                parts = lhs.split('+')
                var_part = parts[0]
                const_part = '-' + parts[1]
            elif '-' in lhs:
                parts = lhs.split('-')
                var_part = parts[0]
                const_part = parts[1]
            else:
                var_part = lhs
                const_part = '0'
            if 'x' in var_part:
                coeff = int(var_part.replace('x', '')) if var_part != 'x' else 1
            if const_part:
                const = int(const_part)
            rhs_val = int(rhs)
            result = (rhs_val - const) / coeff
            return f"{var} = {round(result, 2)}"
        except:
            return "Error solving equation"
    @staticmethod
    def solve_quadratic(exn): #exn ~ equation
        '''This thing solves basic quadratic equations of the form ax^2 + bx + c = 0
        It is still not able to handle anything too complex so don't play too hard with it plss
        For now this thing just splits the equation from the center or wherever the = sign is and evaluates according to the algorithm'''
        try:
            a = b = c = 0
            exn = exn.replace(' ', '').split('=')[0]
            parts = exn.split('x')
            a = int(parts[0]) if parts[0] else 1
            b = int(parts[1].split('+')[1]) if '+' in parts[1] else -int(parts[1].split('-')[1])
            c = int(parts[2]) if len(parts) > 2 else 0
            disc = b**2 - 4*a*c #disc ~ discriminant
            if disc < 0:
                return "This equation has no real roots"
            elif disc == 0:
                root = -b / (2*a)
                return f"x = {round(root, 2)}"
            else:
                root1 = (-b + sqrt(disc)) / (2*a)
                root2 = (-b - sqrt(disc)) / (2*a)
                return f"x = {round(root1, 2)} or {round(root2, 2)}"
        except:
            return "Something is wrong with the equation or your code, pls check the signs or smth else you'd like ; p" 
    @staticmethod
    def unit_conversion(value, from_unit, to_unit):
        convs = { #convs ~ conversions
            'meters': {'kilometers': 0.001, 'centimeters': 100},
            'kilograms': {'grams': 1000},
            'liters': {'milliliters': 1000}
        }
        return value * convs.get(from_unit, {}).get(to_unit, 1)
    @staticmethod
    def calculate_resistance(resistors, circuit_type):
        """code is pretty self-explanatory for this"""
        if circuit_type == "series":
            return sum(resistors)
        elif circuit_type == "parallel":
            return 1 / sum(1/r for r in resistors)
        return "Please enter either 'series' or 'parallel' for the circuit type."
    @staticmethod
    def get_element_info(symbol):
        """This thing just searches the particular element in the dict and returns the hard coded info nothing too AI or ML here"""
        periodic_table = {
            'H': {'name': 'Hydrogen', 'atomic_n': 1},
            'He': {'name': 'Helium', 'atomic_n': 2},
            'Li': {'name': 'Lithium', 'atomic_n': 3},
            'Be': {'name': 'Beryllium', 'atomic_n': 4},
            'B': {'name': 'Boron', 'atomic_n': 5},
            'C': {'name': 'Carbon', 'atomic_n': 6},
            'N': {'name': 'Nitrogen', 'atomic_n': 7},
            'O': {'name': 'Oxygen', 'atomic_n': 8},
            'F': {'name': 'Fluorine', 'atomic_n': 9},
            'Ne': {'name': 'Neon', 'atomic_n': 10},
            'Na': {'name': 'Sodium', 'atomic_n': 11},
            'Mg': {'name': 'Magnesium', 'atomic_n': 12},
            'Al': {'name': 'Aluminum', 'atomic_n': 13},
            'Si': {'name': 'Silicon', 'atomic_n': 14},
            'P': {'name': 'Phosphorus', 'atomic_n': 15},
            'S': {'name': 'Sulfur', 'atomic_n': 16},
            'Cl': {'name': 'Chlorine', 'atomic_n': 17},
            'Ar': {'name': 'Argon', 'atomic_n': 18},
            'K': {'name': 'Potassium', 'atomic_n': 19},
            'Ca': {'name': 'Calcium', 'atomic_n': 20},
            'Sc': {'name': 'Scandium', 'atomic_n': 21},
            'Ti': {'name': 'Titanium', 'atomic_n': 22},
            'V': {'name': 'Vanadium', 'atomic_n': 23},
            'Cr': {'name': 'Chromium', 'atomic_n': 24},
            'Mn': {'name': 'Manganese', 'atomic_n': 25},
            'Fe': {'name': 'Iron', 'atomic_n': 26},
            'Co': {'name': 'Cobalt', 'atomic_n': 27},
            'Ni': {'name': 'Nickel', 'atomic_n': 28},
            'Cu': {'name': 'Copper', 'atomic_n': 29},
            'Zn': {'name': 'Zinc', 'atomic_n': 30},
            'Ga': {'name': 'Gallium', 'atomic_n': 31},
            'Ge': {'name': 'Germanium', 'atomic_n': 32},
            'As': {'name': 'Arsenic', 'atomic_n': 33},
            'Se': {'name': 'Selenium', 'atomic_n': 34},
            'Br': {'name': 'Bromine', 'atomic_n': 35},
            'Kr': {'name': 'Krypton', 'atomic_n': 36},
            'Rb': {'name': 'Rubidium', 'atomic_n': 37},
            'Sr': {'name': 'Strontium', 'atomic_n': 38},
            'Y': {'name': 'Yttrium', 'atomic_n': 39},
            'Zr': {'name': 'Zirconium', 'atomic_n': 40},
            'Nb': {'name': 'Niobium', 'atomic_n': 41},
            'Mo': {'name': 'Molybdenum', 'atomic_n': 42},
            'Tc': {'name': 'Technetium', 'atomic_n': 43},
            'Ru': {'name': 'Ruthenium', 'atomic_n': 44},
            'Rh': {'name': 'Rhodium', 'atomic_n': 45},
            'Pd': {'name': 'Palladium', 'atomic_n': 46},
            'Ag': {'name': 'Silver', 'atomic_n': 47},
            'Cd': {'name': 'Cadmium', 'atomic_n': 48},
            'In': {'name': 'Indium', 'atomic_n': 49},
            'Sn': {'name': 'Tin', 'atomic_n': 50},
            'Sb': {'name': 'Antimony', 'atomic_n': 51},
            'Te': {'name': 'Tellurium', 'atomic_n': 52},
            'I': {'name': 'Iodine', 'atomic_n': 53},
            'Xe': {'name': 'Xenon', 'atomic_n': 54},
            'Cs': {'name': 'Cesium', 'atomic_n': 55},
            'Ba': {'name': 'Barium', 'atomic_n': 56},
            'La': {'name': 'Lanthanum', 'atomic_n': 57},
            'Ce': {'name': 'Cerium', 'atomic_n': 58},
            'Pr': {'name': 'Praseodymium', 'atomic_n': 59},
            'Nd': {'name': 'Neodymium', 'atomic_n': 60},
            'Pm': {'name': 'Promethium', 'atomic_n': 61},
            'Sm': {'name': 'Samarium', 'atomic_n': 62},
            'Eu': {'name': 'Europium', 'atomic_n': 63},
            'Gd': {'name': 'Gadolinium', 'atomic_n': 64},
            'Tb': {'name': 'Terbium', 'atomic_n': 65},
            'Dy': {'name': 'Dysprosium', 'atomic_n': 66},
            'Ho': {'name': 'Holmium', 'atomic_n': 67},
            'Er': {'name': 'Erbium', 'atomic_n': 68},
            'Tm': {'name': 'Thulium', 'atomic_n': 69},
            'Yb': {'name': 'Ytterbium', 'atomic_n': 70},
            'Lu': {'name': 'Lutetium', 'atomic_n': 71},
            'Hf': {'name': 'Hafnium', 'atomic_n': 72},
            'Ta': {'name': 'Tantalum', 'atomic_n': 73},
            'W': {'name': 'Tungsten', 'atomic_n': 74},
            'Re': {'name': 'Rhenium', 'atomic_n': 75},
            'Os': {'name': 'Osmium', 'atomic_n': 76},
            'Ir': {'name': 'Iridium', 'atomic_n': 77},
            'Pt': {'name': 'Platinum', 'atomic_n': 78},
            'Au': {'name': 'Gold', 'atomic_n': 79},
            'Hg': {'name': 'Mercury', 'atomic_n': 80},
            'Tl': {'name': 'Thallium', 'atomic_n': 81},
            'Pb': {'name': 'Lead', 'atomic_n': 82},
            'Bi': {'name': 'Bismuth', 'atomic_n': 83},
            'Po': {'name': 'Polonium', 'atomic_n': 84},
            'At': {'name': 'Astatine', 'atomic_n': 85},
            'Rn': {'name': 'Radon', 'atomic_n': 86},
            'Fr': {'name': 'Francium', 'atomic_n': 87},
            'Ra': {'name': 'Radium', 'atomic_n': 88},
            'Ac': {'name': 'Actinium', 'atomic_n': 89},
            'Th': {'name': 'Thorium', 'atomic_n': 90},
            'Pa': {'name': 'Protactinium', 'atomic_n': 91},
            'U': {'name': 'Uranium', 'atomic_n': 92},
            'Np': {'name': 'Neptunium', 'atomic_n': 93},
            'Pu': {'name': 'Plutonium', 'atomic_n': 94},
            'Am': {'name': 'Americium', 'atomic_n': 95},
            'Cm': {'name': 'Curium', 'atomic_n': 96},
            'Bk': {'name': 'Berkelium', 'atomic_n': 97},
            'Cf': {'name': 'Californium', 'atomic_n': 98},
            'Es': {'name': 'Einsteinium', 'atomic_n': 99},
            'Fm': {'name': 'Fermium', 'atomic_n': 100},
            'Md': {'name': 'Mendelevium', 'atomic_n': 101},
            'No': {'name': 'Nobelium', 'atomic_n': 102},
            'Lr': {'name': 'Lawrencium', 'atomic_n': 103},
            'Rf': {'name': 'Rutherfordium', 'atomic_n': 104},
            'Db': {'name': 'Dubnium', 'atomic_n': 105},
            'Sg': {'name': 'Seaborgium', 'atomic_n': 106},
            'Bh': {'name': 'Bohrium', 'atomic_n': 107},
            'Hs': {'name': 'Hassium', 'atomic_n': 108},
            'Mt': {'name': 'Meitnerium', 'atomic_n': 109},
            'Ds': {'name': 'Darmstadtium', 'atomic_n': 110},
            'Rg': {'name': 'Roentgenium', 'atomic_n': 111},
            'Cn': {'name': 'Copernicium', 'atomic_n': 112},
            'Nh': {'name': 'Nihonium', 'atomic_n': 113},
            'Fl': {'name': 'Flerovium', 'atomic_n': 114},
            'Mc': {'name': 'Moscovium', 'atomic_n': 115},
            'Lv': {'name': 'Livermorium', 'atomic_n': 116},
            'Ts': {'name': 'Tennessine', 'atomic_n': 117},
            'Og': {'name': 'Oganesson', 'atomic_n': 118}
        }
        element = periodic_table.get(symbol.upper())
        if element:
            return f"Name: {element['name']}, Atomic Number: {element['atomic_n']}"
        return "The particular element doesn't exist yet, pls get your noble prize if you think it is their ; )"
    @staticmethod
    def get_table(n):
        #simple
        return [n*i for i in range(1, 11)]
    @staticmethod
    def solve_gas_law(exn):
        #it solves the equation using the ideal gas law PV = nRT , give it three out of the four variables and it'll find the fourth , simplee :D

        try:
            exn = exn.replace(" ", "")
            parts = exn.split(',')
            values = {}
            unknown = None
            for part in parts:
                if '=' not in part:
                    continue
                var, val = part.split('=')
                var = var.upper()  
                if val == '?' or val.lower() == 'x':
                    if unknown is not None:
                        return "Error: More than one unknown variable. I can only find one at a time ; p"
                    unknown = var
                    values[var] = None
                else:
                    values[var] = float(val)
            if unknown is None:
                return "Error: TELL ME WHAT DO I HAVE TO FIND I CAN'T READ MINDS (pls mark the unknown with '?')."
            R = 0.0821
            if unknown == 'P':
                if any(values.get(v) is None for v in ['V', 'N', 'T']):
                    return "Error: all variables are not there for solving P."
                result = (values['N'] * R * values['T']) / values['V']
                return f"P = {round(result, 3)} atm"
            elif unknown == 'V':
                if any(values.get(v) is None for v in ['P', 'N', 'T']):
                    return "Error: all variables are not there for solving V."
                result = (values['N'] * R * values['T']) / values['P']
                return f"V = {round(result, 3)} L"
            elif unknown == 'N':
                if any(values.get(v) is None for v in ['P', 'V', 'T']):
                    return "Error: all variables are not there for solving n."
                result = (values['P'] * values['V']) / (R * values['T'])
                return f"n = {round(result, 3)} mol"
            elif unknown == 'T':
                if any(values.get(v) is None for v in ['P', 'V', 'N']):
                    return "Error: all variables are not there for solving T."
                result = (values['P'] * values['V']) / (values['N'] * R)
                return f"T = {round(result, 3)} K"
            else:
                return "Error: Unknown variable. Use P, V, n, or T. Or if you think you found a new metric claim your nobel prize plsss"
        except Exception as e:
            return f"Error: {str(e)}"
    @staticmethod
    def calculate_factorial(n):
        #simple
        return factorial(n)
    

#-------------interpreter code
    



class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}
        self.stem = stem_ops()
    def evaluate(self):
        for node in self.ast:
            self.evaluate_node(node)
    def evaluate_node(self, node):
        if isinstance(node, PrintNode):
            print(self.evaluate_node(node.expression))
#yoo bartosz i love fraud ; p imma commit it everyday, even more than my code
        elif isinstance(node, AssignmentNode):
            self.symbol_table[node.name] = self.evaluate_node(node.value)

        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, NumberNode):
            return node.value
        
        elif isinstance(node, VariableNode):
            return self.symbol_table.get(node.name, f"Undefined variable: {node.name}")
        
        elif isinstance(node, STEMFunctionNode):
            return self.evaluate_stem_function(node)
        elif isinstance(node, IfNode):
            condition = self.evaluate_node(node.condition)
            
            if condition:
                for stmt in node.then_branch:
                    self.evaluate_node(stmt)
            elif node.else_branch:
                for stmt in node.else_branch:
                    self.evaluate_node(stmt)
            return None
        elif isinstance(node, ForNode):
            self.evaluate_node(node.initializer)
            while self.evaluate_node(node.condition):
                for stmt in node.body:
                    self.evaluate_node(stmt)
                self.evaluate_node(node.increment)

            return None
        elif isinstance(node, WhileNode):
            
            while self.evaluate_node(node.condition):
                for stmt in node.body:
                    self.evaluate_node(stmt)
            
            return None
        

        else:
            raise ValueError(f"Unknown node type: {type(node)}")
    def evaluate_stem_function(self, node):
        func_name = node.func_name
        args = [self.evaluate_node(arg) for arg in node.arguments]
        try:
            if func_name == 'SOLVE':
                return self.stem.solve_linear(args[0])
            elif func_name == 'SOLVE_QUAD':
                return self.stem.solve_quadratic(args[0])
            elif func_name == 'CONVERT':
                return self.stem.unit_conversion(*args)
            elif func_name == 'RESISTANCE':
                return self.stem.calculate_resistance(args[0], args[1])
            elif func_name == 'ELEMENT_INFO':
                return self.stem.get_element_info(args[0])
            elif func_name == 'TABLE':
                return self.stem.get_table(args[0])
            elif func_name == 'BALANCE':
                return "Balancing is WIP" # this thing is under dev, pls don't touch it now 
            elif func_name == 'GAS_LAW':
                return self.stem.solve_gas_law(args[0])
            elif func_name == 'FACTORIAL':
                return self.stem.calculate_factorial(args[0])
            else:
                raise NameError(f"I've not made smth like : {func_name} yet, pls make a PR if you want it ; )")
        except Exception as e:
            return f"Error: {str(e)}"
#yooooooooooo bartosz this whole thing is ai generated :)))))) 
#cli code
def help_cmd():
    print()
def main():
    print("YapScript CLI. Type /help for instructions.")
    while True:
        try:
            source = input(">>> ")
            if source.strip() == "/help":
                help_cmd()
                continue
            elif source.strip() == "/exit":
                break
            lexer = Lexer(source)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            ast = parser.parse()
            interpreter = Interpreter(ast)
            interpreter.evaluate()
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()

