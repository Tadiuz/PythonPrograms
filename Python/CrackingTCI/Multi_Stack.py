class Multistack:
    def __init__(self, num_stack, size_stack):
        self.num_stack = num_stack
        self.size_stack = [size_stack] * num_stack
        self.stack = [0] * (num_stack * size_stack)
        self.size = [0] * num_stack

    def offset(self, stack_num):
        offset_val = (stack_num-1) * self.size_stack[stack_num-1] + self.size[stack_num -1]
        return offset_val

    def is_full(self, stack_num):
        if self.size[stack_num - 1] == self.size_stack[stack_num-1]:
            return True
        return False



    def increase_capacity(self, offset_val, stack_num):

        increment = 3

        var = self.size[stack_num - 1]
        print("var is ", var)

        self.stack[offset_val:offset_val] = [0] * increment

        for i in range(stack_num - 1, self.num_stack):
            self.size_stack[i] +=increment

    def push(self, value, stack_num):
        offset_value = self.offset(stack_num)


        if self.is_full(stack_num):
            print("Offset", offset_value)
            self.increase_capacity(offset_value, stack_num)
            #print("Here")



        self.stack[offset_value] = value
        self.size[stack_num - 1] += 1

    def print_stack(self):

        print(self.stack)
        print("Size is: ", self.size)

        print("Size sStack is: ", self.size_stack)


        

    
multi_stack = Multistack(3, 3)

multi_stack.push(3, 3)
multi_stack.print_stack()

multi_stack.push(2, 3)
multi_stack.print_stack()


multi_stack.push(1, 1)
multi_stack.print_stack()

multi_stack.push(2, 2)
multi_stack.print_stack()

multi_stack.push(25, 3)
multi_stack.print_stack()

multi_stack.push(25, 3)
multi_stack.print_stack()


multi_stack.push(65, 2)
multi_stack.print_stack()

multi_stack.push(65, 2)
multi_stack.print_stack()
multi_stack.push("Stack 3", 2)
multi_stack.print_stack()