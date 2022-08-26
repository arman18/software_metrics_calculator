import ast
class hal_vis:
    # uniq_oprts = {}
    # uniq_oprds = {}
    # total_oprts ={}
    # total_oprds ={}
    # cyclomatic = {}
    
    def __init__(self):
        self.uniq_oprts = {}
        self.uniq_oprds = {}
        self.total_oprts ={}
        self.total_oprds ={}
        self.cyclomatic = {}
        
    
    def initiate_context(self,context):
        if context not in self.uniq_oprts:
            self.uniq_oprts[context] = set()
        
        if context not in self.uniq_oprds:
            self.uniq_oprds[context] = set()
        
        if context not in self.total_oprts:
            self.total_oprts[context] = 0
        
        if context not in self.total_oprds:
            self.total_oprds[context] = 0
        
        if context not in self.cyclomatic:
            self.cyclomatic[context] = 1
        
        
    def update_operand(self,lst,context):
        for item in lst:
            if type(item) != list:
                item = [item]
            for el in item:
                if type(el) == ast.Name:
                    self.uniq_oprds[context].add(el.id)
                    self.total_oprds[context] +=1
                if type(el) == str:
                    self.uniq_oprds[context].add(el)
                    self.total_oprds[context] +=1
                elif type(el) == ast.Constant:
                    self.uniq_oprds[context].add(el.value)
                    self.total_oprds[context] +=1
                
    def update_operator(self,lst,context):
        for el in lst:
            self.uniq_oprts[context].add(el)
            self.total_oprts[context] +=1
            
    def visit_single(self,node,context):
        
        if type(node) == ast.BinOp:
            self.initiate_context(context)
            self.update_operator([node.op.__class__.__name__],context)
            self.update_operand((node.left, node.right),context)
        if type(node) == ast.UnaryOp:
            self.initiate_context(context)
            self.update_operator([node.op.__class__.__name__],context)
            self.update_operand((node.operand,),context)
        if type(node) == ast.BoolOp:
            self.initiate_context(context)
            self.update_operator([node.op.__class__.__name__],context)
            self.update_operand((node.values,),context)
        if type(node) == ast.AugAssign:
            self.initiate_context(context)
            self.update_operator([node.op.__class__.__name__],context)
            self.update_operand((node.target, node.value),context)
        if type(node) == ast.Compare:
            self.initiate_context(context)
            ops = []
            if type(node.ops) == list:
                for i in node.ops:
                    ops.append(i.__class__.__name__)
                    
            self.update_operator(ops,context)
            self.update_operand(node.comparators + [node.left],context)
            
        if type(node) == ast.Assign:
            self.initiate_context(context)
            self.update_operator(["Assign"],context)
            self.update_operand((node.targets, node.value),context)
        if type(node) == ast.Call:
            self.initiate_context(context)
            self.update_operator([node.func.id],context)
            self.update_operand((node.args),context)
        if type(node) == ast.If:
            self.initiate_context(context)
            self.update_operator(["If"],context)
            self.update_operand((node.test,),context)
            self.cyclomatic[context] +=1
        if type(node) == ast.While:
            self.initiate_context(context)
            self.update_operator(["While"],context)
            self.update_operand((node.test,),context)
            self.cyclomatic[context] +=1
        if type(node) == ast.Return:
            self.initiate_context(context)
            self.update_operator(["Return"],context)
            self.update_operand((node.value,),context)
        if type(node) == ast.Yield:
            self.initiate_context(context)
            self.update_operator(["Yield"],context)
            self.update_operand((node.value,),context)
        if type(node) == ast.For:
            self.initiate_context(context)
            self.update_operator(["For","In"],context)
            self.update_operand((node.target,node.iter),context)
            self.cyclomatic[context] +=1
        if type(node) == ast.FunctionDef:
            self.initiate_context(context)
            self.update_operator(["def",node.name],context)
            args = []
            for arg in node.args.args:
                args.append(arg.arg)
            self.update_operand(args,context)
        
        
        # print(context,type(node))
    def visit(self,node,context="NONE"):
        self.visit_single(node,context)
        if not hasattr(node, "_fields"):
            return 
        for field in node._fields:
            fields_value = getattr(node,field)
            if type(fields_value) == list:
                for value in fields_value:
                    if type(value) == ast.FunctionDef:
                        self.visit(value,value.name)
                    else:
                        self.visit(value,context)
            else:
                if type(fields_value) == ast.FunctionDef:
                    self.visit(fields_value,fields_value.name)
                else:
                    self.visit(fields_value,context)
           