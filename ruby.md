# Ruby cheat sheet.

### Base level:
1) Difference between proc and lambda
	Procs are the fist-class objects (can be created, destroyes dynamically). Lambda similar to Proc (is' proc), but have several diffs:
	1 - Proc doesnt check arguments count when called
	2 - Proc return work like block return. but Lambda will just return from themself.
2) Difference between `String` and `Symbol` ??? ( символы гарбедж коллектинг с версии 2.2.1)
	Symbol doesn't copying in memory. If you use :example in several places it will reference to the sam object
3) Explain duck-typing
	DYnamic lng without stron typing. In ruby case, that mean that object can be evetyrhing that you wann. Ruby hasa high reflection level, so you can change object on the fly. Here is working Duck rule. "If something quacks like duck and looking like duck, that mean it is duck."
4) Difference between class and Module
	In low technical level it's working in the same manner. Difference in the next:
	1 - Module can't be instantiate, so it doesn' have methods new, 
	2 - Module superclass is a Class,  
	3 - Module don't used in inheritance chain. formally. But on low level modules includes in inheritance chain

5) What will output
	val1 = true and false
	val2 = true && false

	p val1 == true
	p val2 == false

	output:
	true
	true

	`=` priority > then `and` priority

	Operator	Description
	Yes	[ ] [ ]=	Element reference, element set
	Yes	**	Exponentiation (raise to the power)
	Yes	! ~ + -	Not, complement, unary plus and minus (method names for the last two are +@ and -@)
	Yes	* / %	Multiply, divide, and modulo
	Yes	+ -	Addition and subtraction
	Yes	>> <<	Right and left bitwise shift
	Yes	&	Bitwise `AND'
	Yes	^ |	Bitwise exclusive `OR' and regular `OR'
	Yes	<= < > >=	Comparison operators
	Yes	<=> == === != =~ !~	Equality and pattern match operators (!= and !~ may not be defined as methods)
	&&	Logical `AND'
	||	Logical `AND'
	.. ...	Range (inclusive and exclusive)
	? :	Ternary if-then-else
	= %= { /= -= += |= &= >>= <<= *= &&= ||= **=	Assignment
	defined?	Check if specified symbol defined
	not	Logical negation
	or and	Logical composition
	if unless while until	Expression modifiers
	begin/end	Block expression

6) Output
	true    ? "true" : "false" # true
	false   ? "true" : "false" # false
	nil     ? "true" : "false" # false
	1       ? "true" : "false" # true
	0       ? "true" : "false" # true
	"false" ? "true" : "false" # true
	""      ? "true" : "false" # true
	[]      ? "true" : "false" # true

7) Write a function that sorts the keys in a hash by the length of the key as a string. For instance, the hash

def sort_hsh_keys(i)
	i.keys.map(&:to_s).sort_by &:length
end

8) Consider the following two methods:

	def times_two(arg1);
	  puts arg1 * 2;
	end

	def sum(arg1, arg2);
	  puts arg1 + arg2;
	end
What will be the result of each of the following lines of code:

	times_two 5 # 10
	times_two(5) # 10
	times_two (5) # 10
	sum 1, 2 # 3
	sum(1, 2) # 3
	sum (1, 2) # Syntax error


		times_two 5 
	times_two(5) 
	times_two (5) 
	sum 1, 2 
	sum(1, 2) 
	sum (1, 2) 

8) Consider the following code:

VAL = 'Global'
 
module Foo
  VAL = 'Foo Local'
 
  class Bar
    def value1
      VAL
    end
  end
end
 
class Foo::Bar
  def value2
    VAL
  end
end
What will be the value of each of the following:

Foo::Bar.new.value1 # Foo Local
Foo::Bar.new.value2 # Global
Explain your answer.

Second Foo::Bar is an independent lexical context from first.

9) -> (a) {p a}["Hello world"] what is it?

This is lambda which print passed parameter. [] - mean call lambda with param "Hello world"

10) Explain each of the following operators and how and when they should be used: ==, ===, eql?, equal?

== - Checks if the value of two operands are equal (often overridden to provide a class-specific definition of equality).
=== - Used in case^ it's like ~~~
eql? the same like ==, but check type, redefined for hash
equal? check object id

11) What is the differnece between extend and include in ruby?

extend - add class methods
include - add object methods

12) In Ruby code, you quite often see the trick of using an expression like array.map(&:method_name) as a shorthand form of array.map { |element| element.method_name }. How exactly does it work?

proc_to_sym method!

13) while readline
 print if ~ /^ERROR:/
end

Why is it work?
What does it do?

All work through  $_ 

print $_ if $_ = $_.match /^EROOR:/

14) What will in output
```
class Parent
  @@var1 = "Parent 1"
  @var2 = "Parent 2"
  def self.vars
    "var1: #{@@var1}, var2: #{@var2}"
  end
end
   
class Child < Parent
  @@var1 = "Child 1"
  @var2 = "Child 2"
end

puts Parent.vars
puts Child.vars

# var1: Child 1, var2: Parent 2
# var1: Child 1, var2: Child 2
```

15) What will in output?

module M1
	def m_method; end
end

class C
	include M1
	def c_method; end
end

module M2
	def m2_method; end
end

module M1
	include M2
	def m1_add_method; end
end

c = C.new
p c.methods.sort #[:c_method, :m1_add_method, :m_method] 

Because ruby ignore submodules included later major include

16) What will in output?

class Test
	def test
		call_method
	end
end

def call_method
	p "I have been called"
end

call_method
Test.call_method
Test.new.test
Test.new.call_method

Will called 4 times, because we added method n global scope to 	Object, which everywhere parent

17) What is class.

In ruby class is an object, which have methods table, constant table, link to super class, list of variables names. In general sence class is a blueprint for objects

18) What is the difference between a class and a module?

internally it looks similarly, but has several differences. You can't instantiate object from module. 

19) What is an object.

In Ruby object is a structure, which hold variables array and pointer to class. In general sence is a class instance.

20) How would you declare and use a constructor in Ruby?

class Test
	def initialize

	end
end

21) How would you create getter and setter methods in Ruby?

class Test
	def test()
		@test
	end

	def test=(value)
		@test = value
	end
end

or

class Test
	attr_accessor :test
end

or 

class Test
	attr_reader :test
	attr_writer :test
end

22) Describe the difference between class and instance variables?

Instance variables data saved in special array inside instance object. Class variables and  class instance variables saved in RClass strcuture (or object if we talk about Rubinius/JRuby). @@ and @ have different algo to set and get, but saved in one table for class!

23) What are the three levels of method access control for classes and what do they signify?

public - everybody can call method, by default methods have this access level
protected - might be called by objects of class and for objects of sublcasses
private - can be called just from receiver, mean self

also exists private_class, the same but in class context

24) What does ‘self’ mean?

Self is a pointer to `current object`. it's a object in which context we currently work, and depend on current lexical scope. For example self for empty main.rb script is a `main` object for program. In object method self is instance of object. Inside class method self is a current class. Inside class lexical scope, self is a class. Inside class << self , self is metaclass. For blocks and lambdas self is self for parent lexiacal scope

25) Explain how (almost) everything is an object in Ruby.

26) Explain what singleton methods are. What is Eigenclass in Ruby?

Singlrton methods are methods which added to object. Eigenclass is a singleton class, which will be created for objects with singleton methods. It's because all methods saved in class.

27) Describe Ruby method lookup path.

Ruby go through methods tables of class. If methods didn' find, ruby see to parent class and moving up trhough inheritance heirarchy. Also, all modules when included will be injected in inhertiance chain in include order. 

28) Describe available Ruby callbacks. How can we use them in practice?

Hook methods onRuby objects, like included, extended, method_missing, const_missing, method_removed, inherited, that all used for pathicng, dsl , etc

29) What is the difference between Proc and lambda?

Proc and lambda are instances of Proc object. Proc doesnt check count of input params and work like block. Lambda doesn't check count of params and doesn't work like a block

30) What difference between ==, equal?, eql? and ===

== Behavior depend on Object Class. By default for example Object#== use equal? method. Strings for example check that string equaivalent, numbers too. So this method check that objects are equal by values

equal? Check that objects id's are equal, check that this are the same objects

eql? check that result of #has are equal

=== - it's separate method. It behavior depend and method receiver class. Also often called case equality. "If a is a drawer then we check would it take make sense if we put b in the drawer".

31) Given this input:

x = [{"a" => 10},{"b" => 20},{"c" => 30}]
How can you obtain the following?

one array containing all keys
another containing all values
the sum of all the values

x.flat_map {|i| i.keys }
x.flat_map {|i| i.values }
x.flat_map {|i| i.values }.reduce :+ 

32) What is the difference between the Object methods clone and dup?

dup create shallow copy, for example without incuded modules

33) What is singleton class?

This is a class which create when we define methods on objects, like


```
some_object.def new_method

end

```

Or when we do extend - it creates a class in inheritance chain between our class and Class and put there all methods

33) default ancestors: Object < Kernel < BasicObject

