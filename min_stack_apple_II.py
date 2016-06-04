//Test

/*
 * MinStack - All the same stuff that a regular stack does but always returns the minimum value when asked
 * Implement functions for push, pop, popMin
 */

[] popMin

main_stack = [6,5,10,11,15,16,17,18]
bookkeeping_stack = [6,5,5,5,5,5,5,5,5]  --> [6,6,6,6,6,6,6,6,6]

pop - 10 , 5
popMin ==

class MinStack:
	def __init__(self):
    self.mainStack = []
    self.mainStack_shadow = []
    self.minStack = []

	def push(self,x):
  	if len(self.mainStack) == 0:
    	self.mainStack.append(x)
      self.minStack.append(x)
    else:
    	self.mainStack.append(x)
      y = self.minStack[len(self.minStack)-1]
      if x < y:
      	self.minStack.append(x)
      else:
      	self.minStack.append(y)

  def pop(self):
  	self.mainStack.pop()
    self.minStack.pop()

  def popMin(self):
  	min_element = self.minStack[len(self.minStack)-1]
    main_top = self.mainStack.pop()

    while main_top != min_element :
    	self.mainStack_shadow.append(main_top)
      main_top = self.mainStack.pop()
    print main_top
    for i in xrange(len(self.mainStack_shadow)):
    	temp = self.mainStack_shadow.pop()
      self.mainStack.append(temp)

    main_top # element that I have removed
    count = 0
    temp_data = self.minStack.pop()
    while temp_data == main_top:
    	count +-1
      temp_data = self.minStack.pop()
    for i in xrange(count):
    	self.minStack.append(temp_data)


  ===================================
  import unittest
  class MinStack:
  	def __init__(self):
    	self.mainStack = [] # stack
    	self.mainStack_shadow = [] # stack
    	self.Array = [] # true list


    def push(self,x):
  		if len(self.mainStack) == 0:
    		self.mainStack.append(x)
        self.Array.append(x)
        sorted(self.array) # optimization - O(1) insert

    def pop(self):
    		temp_elem = self.mainStack.pop()  - O(1)
        array.remove(temp_elem)  - O(log n) / array_resize - O(n)

    def popMin(self)
    		if len(self.mainStack) == 0:
        	return -1
        else:
          min_element = sorted.pop(0)    // O(1)
          main_top = self.mainStack.pop()
          while main_top != min_element :     // O(n)
            self.mainStack_shadow.append(main_top)
            main_top = self.mainStack.pop()
        print main_top
        for i in xrange(len(self.mainStack_shadow)):   // O(n)
          temp = self.mainStack_shadow.pop()
          self.mainStack.append(temp)
