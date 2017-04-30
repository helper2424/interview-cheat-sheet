# Ror cheat sheet.

1) What is the difference between Ruby’s Hash and ActiveSupport’s HashWithIndifferentAccess?
HashWithIndifferentAccess[:kye] == HashWithIndifferentAccess['key']

2)What’s the problem with the following controller code? What would be the consequence of leaving this code in a production app? How would you fix it?

class MyController < ApplicationController
  def options
    options = {}
    available_option_keys = [:first_option, :second_option, :third_option]
    all_keys = params.keys.map(&:to_sym)
    set_option_keys = all_keys & available_option_keys
    set_option_keys.each do |key|
      options[key] = params[key]
    end
    options
  end
end

1. Avoid to call methods and local variables with the same name. It's will work, but might happen missundershood
2. params.keys.map(&:to_sym) - params can be very large, avoid this

	Hash[[:first_option, :second_option, :third_option].map do |i|
		value = params[i]
		value.present? ? [i, value] : nil
	end.compact]

	Symbols not garbage collected!

3) What is class?
Class in OOP paradigm is an reference, or blue print of objects. It might hold data and provide API to work with this data. 

4) What is object?
Objects is an instances of classes.

5) Can you tell me the three levels of method access control for classes and modules? What do they imply about the method?

It works differently in langs. For ruby exists 3 type: public, protected, private.
public - without restrictions
protected - can call self and instances of the same class
private - just through self

6) There are three ways to invoke a method in ruby. Can you give me at least two?
o = Object.new
o.object_id
o.send :object_id
o.method(:object_id).call

7) Explain this ruby idiom: a ||= b

a = b if b == false

8) What does self mean?

Reference to the current object (classes objects too, so self can refer to the class)

9) What is a Proc?

Proc is a class, which instances wrap methods. You can pass this objects like params, and call wrapped method in any time. Proc, lambdas and blocks are all Proccess.

10) What is CORS? How does it work?

crossorigin request sharing
Mechanism to control cross origin requests. Example: by default browser restring requests to another domain or port, so you will need enable this.

11) Explain the purpose of each of the HTTP request types when used with a RESTful web service.

GET - retrive some data
POST - create some data
PUT - modify some data
PATCH - too modify
DELETE - remove some data
HEAD - same like get, but return only headers
TRACE - return the data which send
OPTIONS - request permissons 
CONNECT - for estabilish tcp conenction ( for proxy)

12) What is a “MIME type”, what does it consist of, and what is it used for? Provide an example.

Multi-purpose Internet Mail Extension. System map documents and documents types. Consist of type and subtype with slash. text/html, image/png

13) Describe the key advantages of HTTP/2 as compared with HTTP 1.1.

Http2 is a binaty protocol. It has term frames and work with sendings frmaes between client and server. We have less data, headers compressed. Push availability. Load page parallel.

14) What is an ETag and how does it work?

Is an tag added to resources om web server. If tag changed then server says 304 Not modified and client can use cache.

15) Explain the basic structure of a MIME multipart message when used to transfer different content type parts. Provide a simple example.

A simple example of a MIME multipart message is as follows:

MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=frontier

This is a message with multiple parts in MIME format.
--frontier
Content-Type: text/plain

This is the body of the message.
--frontier
Content-Type: application/octet-stream
Content-Transfer-Encoding: base64

PGh0bWw+CiAgPGhlYWQ+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPHA+VGhpcyBpcyB0aGUg
Ym9keSBvZiB0aGUgbWVzc2FnZS48L3A+CiAgPC9ib2R5Pgo8L2h0bWw+Cg==
--frontier--
Each MIME message starts with a message header. This header contains information about the message content and boundary. In this case Content-Type: multipart/mixed; boundary=frontier means that message contains multiple parts where each part is of different content type and they are separated by --frontier as their boundary.

Each part consists of its own content header (zero or more Content- header fields) and a body. Multipart content can be nested. The content-transfer-encoding of a multipart type must always be 7bit, 8bit, or binary to avoid the complications that would be posed by multiple levels of decoding. The multipart block as a whole does not have a charset; non-ASCII characters in the part headers are handled by the Encoded-Word system, and the part bodies can have charsets specified if appropriate for their content-type.

16) What is long pooling?

This is technique, when client send non stop requests to server (queed requests) and server don't accept them and waitining for events. When events ready it send response and close connection.  It's way how to emulate push technology.

17) What does it mean to normalize a database? How does one go about doing it? Describe a potential consequence of database normalization.

?

18) Describe a Hash index and a BTree Index. What are some of their relative advantages and disadvantages?
 ? https://www.toptal.com/web#hiring-guide