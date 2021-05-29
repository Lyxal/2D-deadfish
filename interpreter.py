import random

EOF = 'EOF'
codepage = 'iodcswh<>^v!~(){}'
directions = {'<':'left','>':'right','^':'up','v':'down'}
commands={
'i':"acc+=1",
'o':"stdout['out'] += str(acc)",
'd':"acc-=1",
'c':"stdout['out'] += chr(acc)",
's':"acc**=2",
'w':"stdout['out'] += 'Hello, World!'",
'h':"exit(1)",
'<':"direction='left'",
'>':"direction='right'",
'^':"direction='up'",
'v':"direction='down'",
'~':"acc=0",
'{':"times*=10",
'}':"times//=10",
'(':"direction='right';execute=not(acc)",
')':"execute=True",
'!':"Y=random.choice(range(len(box[X])))"
}
def execute(code, stdin, stdout):
  lines = code.replace("\r", "").split("\n") # Because I don't remember how PA does newlines
  i = stdin
  i=input('Input: ')
  stdout["out"] = ""
  if i.isdigit():
    acc=int(i)
  else:
    acc=0

  direction='right'
  X=1
  Y=1
  n=0
  lines=s.split("\n")
  wall=[[EOF]*len(lines[0])]
  box=wall+[[EOF]+[*x]+[EOF]for x in lines]+wall
  times=1
  execute=True

  token=box[X][Y]

  while token!=EOF:
    token=box[X][Y]
    if token==')':execute=True
    if (token in codepage) and execute and (token not in '{}()'):
      for _ in range(times):
        exec(commands[token])
    if token in '{}()':
      exec(commands[token])
    if direction=='right':Y+=1
    if direction=='left':Y-=1
    if direction=='up':X-=1
    if direction=='down':X+=1
