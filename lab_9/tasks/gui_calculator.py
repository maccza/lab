import tkinter as tk
from functools import partial

from tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        master.bind("<Key>",self.key)
        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()
        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)
        

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)
        # klawiatura pamięci
        operation_pad_ = tk.Frame(bottom_pad)
        operation_pad_.pack(side=tk.LEFT)
        button_memory_label = ['MC','MR','M+']
        fun = [self.clear_memory,self.read_value_from_memory,self.save_to_memory]
        for ii, operation in enumerate(range(3,0,-1)):
            tk.Button(
                operation_pad_, text=button_memory_label[ii], width=5,
                command=fun[ii],
            ).grid(row=ii, column=0)
        tk.Button(
            operation_pad_, text='C', width=5,
            command=self.clear
        ).grid(row=ii+1, column=0)
        
        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2-ii) % 3)
        ii += 1
        tk.Button(
            num_pad, text='0', width=5,
            command=partial(self.update_var, '0')
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='.', width=5,
            command=self.to_float
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=ii // 3, column=ii % 3)

        # klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def to_float(self):
        state = self.state.get()
        if state:
            self.update_var(".")
            
        else:
            self.update_var(".")
        self.update_screen()

    def update_var(self, num):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()
    
    def save_to_memory(self):
        state = self.state.get()
        if state:
            self.calculator._short_memory =  self.variables['var_1']
            if not self.calculator._short_memory:
                self.calculator._short_memory = self.screen['text']
            self.calculator.memorize()
            self.calculator.in_memory()
        else:
            self.calculator._short_memory =  self.variables['var_2']
            if not self.calculator._short_memory:
                    self.calculator._short_memory = self.screen['text']
            self.calculator.memorize()
            self.calculator.in_memory()
    
    def read_value_from_memory(self):
        state = self.state.get()
        if state:
        
            self.variables['var_1'] = self.calculator.memory
            
        else:
            self.variables['var_2'] = self.calculator.memory
            
        self.update_screen()
    
    def clear_memory(self):
        self.calculator.clean_memory()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()
        if not self.variables['var_1'] and not self.variables['var_2'] and self.screen['text']:
            self.variables['var_1'] = self.screen['text']
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        if self.variables['var_1'] and self.variables['var_2']:
            try:
                var_1 = int(self.variables['var_1'])
            except ValueError:
                var_1 = float(self.variables['var_1'])
            try:
                var_2 = int(self.variables['var_2'])
            except ValueError:
                var_2 = float(self.variables['var_2'])
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()

    def key(self,event):
        
        if self.variables['var_1'] and not self.variables['var_2']:
            if event.char in ["+","-","/","*"]:
                self.variables['operator'] = event.char
                
                self.state.set(not self.state.get())

               
                self.update_screen()
        
        if not self.variables['var_1'] and not self.variables['var_2'] and self.screen['text']:
            
            if event.char in ["+","-","/","*"]:
                self.variables['var_1'] = self.screen['text']
                self.variables['operator'] = event.char
                self.state.set(not self.state.get())
                self.update_screen()


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    
    root.mainloop()
