# CIS-524-Project-2

In this project you are asked to write an interpreter which uses the top-down recursive-descent method and inherited/synthesized attributes to parse and evaluate a very simple programming language. The tiny strong-typed language's grammar is given below.

                    <prog>          ::= <global-decl> <let-in-end> {<let-in-end>}

                    <global-decl>   ::= <type> <id-list> = <expr-list>  ;

                    <let-in-end>    ::= let <decl> in <type> (<expr>) end ;

                    <decl>          ::= <type> <id-list> = <expr-list> ;

                    <id-list>       ::= id {, id}

                    <expr-list>     ::= <expr> {, <expr>}

                    <type>          ::= int | real

                    <expr>          ::= <term> { + <term> | <term> }

                    <term>          ::= <factor> { * <factor> | / <factor> }

                    <factor>        ::= <base> ^ <factor> | <base>

                    <base>          ::= (<expr>) | id | num | <type> ( id )  
        
The input file name given from the command line. For example,
spirit % ./let.py sample.tiny

The interpreter let.py reads the program file sample.tiny, checks the syntax and outputs the result for each let-in-end if the it is legitimate; otherwise, the interpreter prints "Error". Note that global variables are declared at the beginning of a program, while local variables are declared and valid whithin a let-in-end block. 

Below is test example: 

        real m , n = 4.0 , 3.0 ;

        let

            int x = 5 ; 
        in

            int ( x + x * x )

        end ;  

        let 

            real m , pi = 10.0 , 3.1416 ; 

        in 

            real ( pi * m * m )

        end ;   


        let

            real x , y = m + n , m - n ; 
        in

            real ( x * y )

        end ; 

        output:

        30

        314.16

        7.0

For another example

        real y = 3.0 ;

        let

            int x = 7 ; 
        in

            real ( ( real ( x ) + y ) / ( real ( x ) - y ) )

        end ;  

        let 
             x = 8 ; 
        in 
             ( x + y )

        end ;   

        Output:

        2.5

        Error
       	
