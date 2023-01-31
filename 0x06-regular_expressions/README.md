# 0x06. Regular expression

## Background Context
Building regular expressions using `Oniguruma` ; a regular expression library which is used by `Ruby` by default.

The focus of this exercise is to play with regular expressions (regex). 

Here is the `Ruby` code that you should use, just replace the regexp part, meaning the code in between the **'//'**.

`example.rb`:

```
   #!/usr/bin/env ruby
   puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

## Tasks
---
0. Simply matching School
The regular expression must match:
```
   Any occurrence of `School`
```

1. Repetition Token #0
The regular expression must match:

```
   hbttn
   hbtttn
   hbttttn
   hbtttttn
```
2. Repetition Token #1
The regular expression must match:

```
   htn
   hbtn
```

3. Repetition Token #2
The regular expression must match:

```
   hbtn
   hbttn
   hbtttn
   hbttttn
   hbttttt...n
```

4. Repetition Token #3
The regular expression must match:

```
   hbn
   hbtn
   hbttn
   hbttt...n
```

5. Not quite HBTN yet
The regular expression must match:

```
   A string that starts with `h` ends with `n` and can have any single character in between
```
6. Call me maybe
The regular expression must match:

```
   A **10 digit phone number**:
   SHOULD REJECT:
      `" 4155049898"`
      `"415 504 9898"`
      `"415-504-9898"`
```

7. OMG WHY ARE YOU SHOUTING?
The Regular Expression must match:

```
   CAPITAL LETTERS
```
