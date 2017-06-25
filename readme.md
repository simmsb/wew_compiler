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
  } else {
	*b := dothis(1*2, that(4+test, else));
	(*(wew+3))(this, 3);
  }
}


```

is parsed into:
```
<FUNCTION:
  <return:
    <POINTER to
      <INTEGER>>>
  <name:
    <IDENTIFIER:
      <NAME: main>>>
  <params:
    <PARAM VARIABLE
      <NAME:
        <IDENTIFIER:
          <NAME: that>>>
      <TYPE:
        <INTEGER>>>
    <PARAM VARIABLE
      <NAME:
        <IDENTIFIER:
          <NAME: this>>>
      <TYPE:
        <POINTER to
          <POINTER to
            <POINTER to
              <INTEGER>>>>>>>
  <code:
    <SCOPE:
      <IF STATEMENT:
        <EXPR
          <LITERAL:
            <VALUE: 1>
            <TYPE: int>>>
        <STATEMENTS:
          <SCOPE:
            <EXPRESSION STMT:
              <FUNCTION_CALL:
                <NAME:
                  <IDENTIFIER:
                    <NAME: print>>>
                <VARS:
                  <IDENTIFIER:
                    <NAME: this>>>>>
            <LOOP:
              <TYPE: while>
              <EXPR:
                <RelExpr:
                  <LEFT:
                    <IDENTIFIER:
                      <NAME: i>>>
                  <OP: le>
                  <RIGHT:
                    <LITERAL:
                      <VALUE: 2>
                      <TYPE: int>>>>>
              <STATEMENTS:
                <SCOPE:
                  <EXPRESSION STMT:
                    <AssignExpr:
                      <LEFT:
                        <IDENTIFIER:
                          <NAME: a>>>
                      <OP: :=>
                      <RIGHT:
                        <LITERAL:
                          <VALUE: 2>
                          <TYPE: int>>>>>>>>>>
        <ELSE:
          <SCOPE:
            <EXPRESSION STMT:
              <AssignExpr:
                <LEFT:
                  <PreFixOp:
                    <OP: *>
                    <EXPR:
                      <IDENTIFIER:
                        <NAME: b>>>>>
                <OP: :=>
                <RIGHT:
                  <FUNCTION_CALL:
                    <NAME:
                      <IDENTIFIER:
                        <NAME: dothis>>>
                    <VARS:
                      <MulExpr:
                        <LEFT:
                          <LITERAL:
                            <VALUE: 1>
                            <TYPE: int>>>
                        <OP: *>
                        <RIGHT:
                          <LITERAL:
                            <VALUE: 2>
                            <TYPE: int>>>>
                      <FUNCTION_CALL:
                        <NAME:
                          <IDENTIFIER:
                            <NAME: that>>>
                        <VARS:
                          <AddExpr:
                            <LEFT:
                              <LITERAL:
                                <VALUE: 4>
                                <TYPE: int>>>
                            <OP: +>
                            <RIGHT:
                              <IDENTIFIER:
                                <NAME: test>>>>
                          <IDENTIFIER:
                            <NAME: else>>>>>>>>>
            <EXPRESSION STMT:
              <FUNCTION_CALL:
                <NAME:
                  <PreFixOp:
                    <OP: *>
                    <EXPR:
                      <AddExpr:
                        <LEFT:
                          <IDENTIFIER:
                            <NAME: wew>>>
                        <OP: +>
                        <RIGHT:
                          <LITERAL:
                            <VALUE: 3>
                            <TYPE: int>>>>>>>
                <VARS:
                  <IDENTIFIER:
                    <NAME: this>>
                  <LITERAL:
                    <VALUE: 3>
                    <TYPE: int>>>>>>>>>>
```
