program
    :statement+
    ;

statement
    :print out_expr
    | 

paren_expr
   : '(' expr ')'
   ;

out_expr
    : '(' id ')'
    | '(' bool ')'
    | '(' expr ')'

expr
   : test
   | id '=' expr
   | test 'and' test
   | test 'or' test
   ;


test
   : sum
   | sum '<' sum
   | sum '>' sum
   | sum '<=' sum
   | sum '>=' sum
   | sum '!=' sum
   ;

sum
   : term
   | sum '+' term
   | sum '-' term
   ;

term
   : id
   | integer
   | paren_expr
   ;

id
   : '"' STRING '"'
   ;

float
   : INT '.' INT

integer
   : INT
   ;


STRING
   : [a-z]+
   ;


INT
   : [0-9]+
   ;