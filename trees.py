# Illustrates how python trees work using a mathematical experisson and implemets one
class expression():
    pass

class Times(expression):
    def __init__(self, l, r):
        self.l = l
        self.r = r
        
    def __str__(self):
        return '(' + str(self.l) + '*' + str(self.r) + ')'
    
    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)
    
class Plus(expression):
    
    def __init__(self, l, r):
        self.l = l 
        self.r = r
    
    def __str__(self):
        return '(' + str(self.l) + '+' + str(self.r) + ')'
    
    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)

class Const(expression):
    
    def __init__(self, val):
        self.val = val
        
    def __str__(self):
        return str(self.val)
    
    def eval(self, env):
        return self.val
    
class Var(expression):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def eval(self, env):
        return env[self.name]

e1 = Times(Const(3), Plus(Var('y'), Var('x')))
e2 = Plus(Times(Var('y'),Const(3)),  Var('x'))
env = {'x':2, 'y':4}
print(e1)
print(e2)
print(e1.eval(env))
print(e2.eval(env))