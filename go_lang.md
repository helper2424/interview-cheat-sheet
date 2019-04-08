1) Do you need both GOPATH and GOROOT variables, and why?

GOROOT - root of golang, if you wanna change golang version you should change this variable
GOPATH - root of directory with dependencies and projects code

2) What is the difference, if any, in the following two slice declarations, and which one is more preferable?
```
var a []int
```
and

```
a := []int{}
```

The first declaration does not allocate memory if the slice is not used, so this declaration method is preferred.

3)What would you do if you need a hash displayed in a fixed order?

You would need to sort that hash’s keys.

fruits := map[string]int{
	"oranges": 100,
	"apples":  200,
	"bananas": 300,
}

// Put the keys in a slice and sort it.
var keys []string
for key := range fruits {
	keys = append(keys, key)
}
sort.Strings(keys)

// Display keys according to the sorted slice.
for _, key := range keys {
	fmt.Printf("%s:%v\n", key, fruits[key])
}
// Output:
// apples:200
// bananas:300
// oranges:100

4) What might be wrong with the following small program?

func main() {
	scanner := bufio.NewScanner(strings.NewReader(`one
two
three
four
`))
	var (
		text string
		n    int
	)
	for scanner.Scan() {
		n++
		text += fmt.Sprintf("%d. %s\n", n, scanner.Text())
	}
	fmt.Print(text)

	// Output:
	// 1. One
	// 2. Two
	// 3. Three
	// 4. Four
}
The program numbers the lines in a buffer and uses the text/scanner to read the input line-by-line. What might be wrong with it?


---

First, it is not necessary to collect the input in the string before putting it out to standard output. This example is slightly contrived.

Second, the string text is not modified with the += operator, it is created anew for every line. This is a significant difference between strings and []byte slices — strings in Go are non-modifiable. If you need to modify a string, use a []byte slice.

Here’s a provided small program, written in a better way:

func main() {
	scanner := bufio.NewScanner(strings.NewReader(`one
two
three
four
`))
	var (
		text []byte
		n    int
	)
	for scanner.Scan() {
		n++
		text = append(text, fmt.Sprintf("%d. %s\n", n, scanner.Text())...)
	}
	os.Stdout.Write(text)
	// 1. One
	// 2. Two
	// 3. Three
	// 4. Four
}
That is the point of the existence of both bytes and strings packages.

4) How would you implement a stack and a queue in Go? Explain and provide code examples.

You use slices to implement a stack or queue by yourself:

type Stack []int
func (s Stack) Empty() bool { return len(s) == 0 }
func (s *Stack) Push(v int) { (*s) = append((*s), v) }
func (s *Stack) Pop() int {
	v := (*s)[len(*s)-1]
	(*s) = (*s)[:len(*s)-1]
	return v
}

type Queue []int
func (q Queue) Empty() bool    { return len(q) == 0 }
func (q *Queue) Enqueue(v int) { (*q) = append((*q), v) }
func (q *Queue) Dequeue() int {
	v := (*q)[0]
	(*q) = (*q)[1:len(*q)]
	return v
}

func main() {
	s := Stack{}
	s.Push(1)
	s.Push(2)
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
	fmt.Println(s.Empty())
	// Output:
	// 2
	// 1
	// true

	q := Queue{}
	q.Enqueue(1)
	q.Enqueue(2)
	fmt.Println(q.Dequeue())
	fmt.Println(q.Dequeue())
	fmt.Println(q.Empty())
	// Output:
	// 1
	// 2
	// true
}
The queue implementation above is correct, but it is suboptimal. There are better but lengthier implementations, like this one.

Occasionally, you would prefer the Go standard library’s container/list to implement them for their conciseness, genericity, and extra list data structure related operations:

stack := list.New()
stack.PushBack(1)
stack.PushBack(2)
fmt.Println(stack.Remove(stack.Back()))
fmt.Println(stack.Remove(stack.Back()))
fmt.Println(stack.Len() == 0)
// Output:
// 2
// 1
// true

queue := list.New()
queue.PushBack(1)
queue.PushBack(2)
fmt.Println(queue.Remove(queue.Front()))
fmt.Println(queue.Remove(queue.Front()))
fmt.Println(queue.Len() == 0)
// Output:
// 1
// 2
// true
Although, their usage is generally discouraged for their slower performance, compared to slices iteration pattern. Let’s compare the two following examples:

// Iterate through a list and print its contents.
for e := queue.Front(); e != nil; e = e.Next() {
    fmt.Println(e.Value)
}
for _, e := range queue {
    fmt.Println(e)
}
“Always use a slice.”, Dave Cheney
Another possibility to implement a queue is to use buffered channels, but this is never a good idea, because:

The buffer size is determined at the channel creation and cannot be increased.
It is impossible to peek at the next queue element without retrieving it from the queue.
There is a risk of deadlock: “Novices are sometimes tempted to use buffered channels within a single goroutine as a queue, lured by their pleasingly simple syntax, but this is a mistake. Channels are deeply connected to goroutine scheduling, and without another goroutine receiving from the channel, a sender—and perhaps the whole program—risks becoming blocked forever. If all you need is a simple queue, make one using a slice.”, Brian Kernighan.

5) What is wrong with the following code snippet?

```
type Orange struct {
	Quantity int
}

func (o *Orange) Increase(n int) {
	o.Quantity += n
}

func (o *Orange) Decrease(n int) {
	o.Quantity -= n
}

func (o *Orange) String() string {
	return fmt.Sprintf("%v", o.Quantity)
}

func main() {
	var orange Orange
	orange.Increase(10)
	orange.Decrease(5)
	fmt.Println(orange)
}
```
Provide the proper code solution.

----

func (o *Orange) String() string {
	return fmt.Sprintf("%v", o.Quantity)
}

-> 

func (o Orange) String() string {
	return fmt.Sprintf("%v", o.Quantity)
}

6) How do you swap two values? Provide a few examples.

a , b = b, a

7) How do you copy a slice, a map, and an interface?

slice - copy
map - traverse key
interface - doesn't exist method

8) Why would you prefer to use an empty struct{}? Provide some examples of the good use of the empty struct{}.

You would use an empty struct when you would want to save some memory. Empty structs do not take any memory for its value.

a := struct{}{}
println(unsafe.Sizeof(a))
// Output: 0
This saving is usually insignificant and is dependent on the size of the slice or a map. Although, more important use of an empty struct is to show a reader you do not need a value at all. Its purpose in most cases is mainly informational. Here are a few examples where it can be useful:

When implementing a data set:
set := make(map[string]struct{})
for _, value := range []string{"apple", "orange", "apple"} {
   set[value] = struct{}{}
}
fmt.Println(set)
// Output: map[orange:{} apple:{}]
With the seen hash, like when traversing a graph:
seen := make(map[string]struct{})
for _, ok := seen[v]; ok {
    // First time visiting a vertex.
    seen[v] = struct{}{}
}
When building an object, and only being interested in a grouping of methods and no intermediary data, or when you do not plan to retain the object state. In the example below it does not make a difference whether the method is called on the same (case #1) or on two different objects (case #2):
type Lamp struct{}

func (l Lamp) On() {
        println("On")

}
func (l Lamp) Off() {
        println("Off")
}

func main() {
       	// Case #1.
       	var lamp Lamp
       	lamp.On()
       	lamp.Off()
       	// Output:
       	// on
       	// off
	
       	// Case #2.
       	Lamp{}.On()
       	Lamp{}.Off()
       	// Output: 
       	// on
       	// off
}
When you need a channel to signal an event, but do not really need to send any data. This event is also not the last one in the sequence, in which case you would use the close(ch) built-in function.
func worker(ch chan struct{}) {
	// Receive a message from the main program.
	<-ch
	println("roger")
	
	// Send a message to the main program.
	close(ch)
}

func main() {
	ch := make(chan struct{})
	go worker(ch)
	
	// Send a message to a worker.
	ch <- struct{}{}
	
	// Receive a message from the worker.
	<-ch
	println(“roger")
	// Output:
	// roger
	// roger
}

9) == - simple types
	reflect.DeepEqual- others
bytes.Equal(), bytes.Compare(), and bytes.EqualFold() - optimized versions