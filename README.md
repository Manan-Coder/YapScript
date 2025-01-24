YapScript! is a toy-programming language made in JavaScript, it was supposed to be made in Python,but considering web implementation, I changed the language and translated the logic to Javascript.
It's website is pretty simple, the main page has all the links to About,Docs, and Playground page.

Main Page - https://manan-coder.github.io/YapScript/index.html
About Page - https://manan-coder.github.io/YapScript/about.html
Docs - https://manan-coder.github.io/YapScript/docs.html
Playground - https://manan-coder.github.io/YapScript/playground.html

It's Syntax is also really simple, inspired from famous GenZ slangs!

This is a lil tutorial to get started with YapScript!

1) Displaying on screen (yap)
   The 'yap' keyword is used to output text to the screen. It is similar to 'print' in other languages.

      ```yap ("Hello, YapScript!");```

3) Var declaration (kick off)
   Use 'kick off' to declare variables in YapScript. It's the language's way to introduce a variable.

      ```kick off num = 42;```
     ```kick off name = "YapScript";```

4) Input (tellMe)
    The 'tellMe' keyword takes user input and stores it in a variable.

      ```kick off x = tellMe("What's your name?")```

4)Functions (letHimCook)
  Define reusable blocks of code using the 'letHimCook' keyword.

                   letHimCook greet() {
                          yap ("Welcome to YapScript!");
                         }
                         greet();

5) If-Else (ohhReally, nahMan)
  'ohhReally' starts an if block, and 'nahMan' starts an else block. These are used for conditional logic.

                        ohhReally (num > 10) {
                            yap ("Number is greater than 10!");
                        } nahMan {
                            yap ("Number is 10 or less!");
                        }

6) Loops (LoopyLoopy)
'LoopyLoopy' is used for creating loops, similar to for or while loops in other languages.

                     LoopyLoopy (i = 0; i < 5; i++) {
                          yap ("Iteration: " + i);
                      }

7) Here’s a simple "Hello World" program in YapScript:

      ```yap ("Hello, World!");```

8) Greeting Function with Name Input
This program asks for a name and greets the user:

       letHimCook greet(L){
              yap("Hello "+L);
          }
          kick off x = tellMe("What's your name??")
          greet(x);


9)If-Else Example
Here’s a simple if-else function:
 
       kick off num = tellMe("Enter the number")
          ohhReally (num > 10) {
              yap ("Number is greater than 10!");
          } nahMan {
              yap ("Number is 10 or less!");
          }
                
      
                          
                    
