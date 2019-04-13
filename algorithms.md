1) https://habrahabr.ru/post/188010/ - classic

2) What is BigO notation?

Tthis is measurement of algorithms complexity, where resulted function grow not faster then original function. Funcitons measure time/memory costs of algorithm. Absicssa of a function is a amount of input data. Described worst case.

3) What is Tetta ?

The same lke BigO notation but from top and bottom of original function

4) What is Omega?

The same like BigO, but from bottom. 

5) Different type of complexities

Worst - when resource costs are maximum
Average - average case of input data, random for example
Best - minumum of

6) Implement quick sort, write complexities

7) Implement buble sort, write complexities

8) Implement heap sort, write complexities

9) Implement merge sort, write complexities

10) Implement inject sorting

-------- Not easy level

11) Implement a fucntion which has one input parameter, which is a unsinged int. The function returns true is number is prime and false if it's not prime

# The simplest variant with eratoshene Sieve
fun isPrime(input: Int):Boolean {
	if (input < 2) return false
	if (input % 2 == 0) return false

	var eratostheneSieve = BooleanArray(input + 1, fun(x:Int) = true)
	var i = 3

	while (i * i < input) {
		if (eratostheneSieve[i])
			for(j in (i*i)..(input-1) step i)
				eratostheneSieve[j] = false
		i+= 2
	}

	return eratostheneSieve[input]
}

# The simplest variant - just checking to sqrt(n)
# We use sqrt(input) because lowest divider exactly smaller than sqrt(n)
fun isPrime(input: Int):Boolean {
    if (input < 2) return false
    if (input == 2 || input == 3) return true
    if (input % 2 == 0 || input % 3 == 0) return false

    var i = 5
    val sqrtInput = Math.sqrt(input.toDouble())
    while  (i <= sqrtInput) {
        if (input % i == 0) return false
        if (input % (i + 2) == 0)
        i+=6
    }

    return true
}

# The test Fermats says:
# If n is not prime than half numbers between 1 and n which are not divide to n have the next relationship a^(n-1) mod n != 1
# the probability that number is not prime = (1/2)^k where k - number of tests and test fetmats says true
# Also exist Carmichael numbers that with any a a^(n-1) mod n == 1 but number is not prime
fun isPrimeFermats(input: Int):Boolean {
    if (input < 2)
        return false;

    if (input == 2 || input == 3 || input == 5)
        return true

    if (input % 2 == 0 || input % 3 == 0 || input % 5 == 0)
        return false

    // Check Carmichael numbers
    if (input == 561 || input == 41041 || input == 825265 || input == 321197285)
        return false

    val checks_count = Math.min(5, input - 5)
    val inputBig = input.toBigInteger()
    for (a in 5..input step (input - 5) / checks_count)
        if (a % input != 0 && a.toBigInteger().modPow(inputBig - 1.toBigInteger(), inputBig) != 1.toBigInteger()) {
            return false
        }

    return true
}

12) Describe Diffie-Hellman protocol:
