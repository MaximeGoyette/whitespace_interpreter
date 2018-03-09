#TODO
def stack_manipulation(arg):
    #TODO
    def push(args):
        pass
        
    #TODO
    def duplicate_n(arg):
        pass
        
    #TODO
    def discard_top_n(arg):
        pass
        
    #TODO
    def duplicate_top(arg):
        pass
        
    #TODO
    def swap(arg):
        pass
        
    #TODO
    def discard_top(arg):
        pass
    
    CMD = {
        's': push,
        'ts': duplicate_n,
        'tn': discard_top_n,
        'ns': duplicate_top,
        'nt': swap,
        'nn': discard_top
    }
    
#TODO
def arithmetic(arg):
    #TODO
    def add(arg):
        pass
        
    #TODO
    def substract(arg):
        pass
    
    #TODO
    def multiply(arg):
        pass
        
    #TODO
    def divide(arg):
        pass
    
    #TODO
    def modulo(arg):
        pass
    
    CMD = {
        'ss': add,
        'st': substract,
        'sn': multiply,
        'ts': divide,
        'tt': modulo
    }

#TODO
def heap_access(arg):
    #TODO
    def pop_from_stack_and_add_to_heap(arg):
        pass
        
    #TODO
    def remove_from_heap_and_push_to_stack(arg):
        pass
    
    CMD = {
        's': pop_from_stack_and_add_to_heap,
        't': remove_from_heap_and_push_to_stack
    }
    
#TODO
def io(arg):
    #TODO
    def output_char(arg):
        pass
    
    #TODO
    def output_number(arg):
        pass
        
    #TODO
    def input_char(arg):
        pass
        
    #TODO
    def input_number(arg):
        pass

    CMD = {
        'ss': output_char,
        'st': output_number,
        'ts': input_char,
        'tt': input_number
    }
    
#TODO
def flow_control(arg):
    #TODO
    def mark_with_label(arg):
        pass
        
    #TODO
    def call_subroutine(arg):
        pass
        
    #TODO
    def jump(arg):
        pass
        
    #TODO
    def jump_if_zero(arg):
        pass
        
    #TODO
    def jump_if_lt_zero(arg):
        pass
        
    #TODO
    def exit_subroutine(arg):
        pass
        
    #TODO
    def exit_program(arg):
        pass

    CMD = {
        'ss': mark_with_label,
        'st': call_subroutine,
        'sn': jump,
        'ts': jump_if_zero,
        'tt': jump_if_lt_zero,
        'tn': exit_subroutine,
        'nn': exit_program
    }

IMP = {
    's': stack_manipulation,
    'ts': arithmetic,
    'tt': heap_access,
    'tn': io,
    'n': flow_control
}

# to help with debugging
def unbleach(n):
    return n.replace(' ', 's').replace('\t', 't').replace('\n', 'n')

# solution
def whitespace(code, inp = ''):
    code = unbleach(code)
    output = ''
    stack = []
    heap = {}
    #...
    return output