# This is the second revision of the 'wew' language, still pretty much C but worse

# What works:
+ Parsing
+ Generating ast and objects

# What isn't implemented
+ Compilation
+ Code generation


# example:

```
int *main(int that, int *** this) {
  if (1) {
    print(this);
    while (i < 2) {a := 2;}
  }
}
```

is parsed into:
```
<FUNCTION:
   <return:
      <POINTER to
         <INTEGER>
      >
   >
   <name:
      <IDENTIFIER:
         <NAME: main>
      >
   >
   <params:
      <PARAM VARIABLE
         <NAME:
            <IDENTIFIER:
               <NAME: that>
            >
         >
         <TYPE:
            <INTEGER>
         >
      >,
      <PARAM VARIABLE
         <NAME:
            <IDENTIFIER:
               <NAME: this>
            >
         >
         <TYPE:
            <POINTER to
               <POINTER to
                  <POINTER to
                     <INTEGER>
                  >
               >
            >
         >
      >
   >
   <code:
      <IF STATEMENT:
         <EXPR
            <LITERAL:
               <VALUE: 1>
               <TYPE: int>
            >
         >
         <STATEMENTS:
            <EXPRESSION STMT:
               <FUNCTION_CALL:
                  <NAME: None>
                  <VARS:
                     <IDENTIFIER:
                        <NAME: this>
                     >
                  >
               >
            >,
            <LOOP:
               <TYPE: while>
               <EXPR:
                  <RelExpr:
                     <LEFT:
                        <IDENTIFIER:
                           <NAME: i>
                        >
                     >
                     <OP: le>
                     <RIGHT:
                        <LITERAL:
                           <VALUE: 2>
                           <TYPE: int>
                        >
                     >
                  >
               >
               <STATEMENTS:
                  <EXPRESSION STMT:
                     <AssignExpr:
                        <LEFT:
                           <IDENTIFIER:
                              <NAME: a>
                           >
                        >
                        <OP: :=>
                        <RIGHT:
                           <LITERAL:
                              <VALUE: 2>
                              <TYPE: int>
                           >
                        >
                     >
                  >
               >
            >
         >
         <ELSE: None>
      >
   >
>
```
