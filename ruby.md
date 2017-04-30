# Ruby cheat sheet.

### Base level:
1) Difference between proc and lambda
	Procs are the fist-class objects (can be created, destroyes dynamically). Lambda similar to Proc (is' proc), but have several diffs:
	1 - Proc check arguments count when called
	2 - Proc return work like block return. but Lambda will just return from themself.
2) Difference between `String` and `Symbol`
	Symbol doesn't copying in memory. If you use :example in several places it will reference to the sam object
3) Explain duck-typing
	DYnamic lng without stron typing. In ruby case, that mean that object can be evetyrhing that you wann. Ruby hasa high reflection level, so you can change object on the fly. Here is working Duck rule. "If something quacks like duck and looking like duck, that mean it is duck."
4) Difference between class and Module
	Classes


5) What will output
	val1 = true and false
	val2 = true && false

	val1 == true
	val2 == false

	output:
	false
	false

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
eql? the same like ==, but check type
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

14) 
