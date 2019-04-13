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

a = b if a == false

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

----
Multipurpose Internet Mail Extension. It's way to identify content type. Has type and subtype: image/png, text/html

13) Describe the key advantages of HTTP/2 as compared with HTTP 1.1.

- binary
- header compression
- request multiplexing
- push

Http2 is a binaty protocol. It has term frames and work with sendings frmaes between client and server. We have less data, headers compressed. Push availability. Load page parallel.

14) What is an ETag and how does it work?

Like hash calculated from file. When internal file changed. After first client save etag and send to server (If-None-Match: "686897696a7c876b7e"). If tag not changed server will response 304.

Is an tag added to resources on web server. If tag changed then server says 304 Not modified and client can use cache.

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

19) What is Rack?

Rack is an api for work with web application server. Bridge API between web server and ruby frameworks

To use Rack, provide an "app": an object that responds to the call method, taking the environment hash as a parameter, and returning an Array with three elements:

The HTTP response code
A Hash of headers
The response body, which must respond to each

20)Explain the Rack application interface

It should have method call which receive env hash and return array with three elements: HTTP code,headers, response body ,which must response to each

21) Write a simple Rack application

run Proc.new { |env| ['200', {'Content-Type' => 'text/html'}, ['get rack\'d']] }

22) How does Rack middleware works?

23)
  What is RubyGems? How does it work?
How can you build your own Ruby gem?
Explain the structure of a Ruby gem.
Can you give me some examples of your favorite gems besides Ruby on Rails?

RubyGems - is a software which allow easily manage ruby packages. You can install new packages by command gem install. And packages will be copied to special dir. .rvm/gems/gem_set/ with hash. THis directory added to $LOAD_PATH. So after this you can include package to your code by require method.

To build your game you should create file soething.gemspec and build it with command `gem build`

Favorite gems:
  pry
  rubocop
  vcr
  celluloid

  optimized json
  devise 
  connection_pool
  redis
  rspec
  webmock
  database_cleaner 
  timecop

24) What is ActiveJob. 

This is framework for running backgrund tasks. You can use it to handle some large tasks, tasks which might be delayed, tasks should run periodically. I don't use Activejib, worked just with sidekiq.

25) What is Asset Pipeline?

This is framework for preprocess assets for rails applicaiton. For example to minimize css and js. Or translate it from other languages, like coffescript, sass etc.

26) What is a Rails engine?

This is framework which allow separate rails functionality to separate bundles. Engine fully copy rails app structure

27) Provide an example of RESTful routing and controller.

resource :some

class TestController < ApplicationController
  def index end
  def update end
  def create end
  def destroy end
  def show end

  def edit end
  def new end
end

28) Describe CRUD verbs and actions.

Create
Read 
Update
Delete

This is abbreviation. All applicaitons in essence make this 4 thisng with data.

29) How test routes?

Like any other intergration tests, use to_route

30) How should you use filters in controllers?

Filters in Ror is methods which you can call like chain before and after action calls. 
example

class TestController < ApllicationController::Base
  before_filter :test

ALso it have after, around filters. If you wanna stop chain in before filter - call render or redirect

31) What are Strong Parameters?

This is technique when you mark input params aa require or permitted and pass to mass update, or create methods.

32) What do we need to test in controllers?

Rspec and methods get, post, put, etc. and see what returned in response.

33) How should you use content_for and yield?
content_for is a method for attaching markup block to label and use it after.

content_for :test do
  <div/>
  end

yield :test

34) How should you use nested layouts?

You can redeclare some content_for labels and render one layout inside other.

<%= render template :test %>

35) Explain the Active Record pattern.


Active record (AR) — шаблон проектирования приложений, описанный Мартином Фаулером в книге Patterns of Enterprise Application Architecture («Шаблоны архитектуры корпоративных приложений»). AR является популярным способом доступа к данным реляционных баз данных в объектно-ориентированном программировании.

Схема Active Record — это подход к доступу к данным в базе данных. Таблица базы данных или представление обёрнуты в классы. Таким образом, объектный экземпляр привязан к единственной строке в таблице. После создания объекта новая строка будет добавляться к таблице на сохранение. Любой загруженный объект получает свою информацию от базы данных. Когда объект обновлён, соответствующая строка в таблице также будет обновлена. Класс обёртки реализует методы средства доступа или свойства для каждого столбца в таблице или представлении.

Этот образец обычно используется объектными инструментами персистентности и в объектно-реляционном отображении (ORM). Как правило, отношения внешнего ключа будут представлены как объектный экземпляр надлежащего типа через свойство.

Реализации данного шаблона часто нарушают принцип единственной ответственности (SRP), совмещая в одном объекте как представление и внутреннюю логику самого объекта, так и механизмы CRUD, поэтому Active Record может считаться антипаттерном[1]. В других случаях это утверждение спорно, так как сам по себе объект, реализующий ActiveRecord, не содержащий никакой бизнес-логики, а предоставляющий таблицу из базы данных, имеет лишь одну причину для изменения (изменение таблицы), что не противоречит определением принципа SRP[2].

36) Describe Active Record names conventions

Tables called like plural forms of modek names. 
primary keys by default - id
foreight_key - attribute _ id

created_at
updated_at - update_all не рабоате
lock_version
type
association_type

37) Explain the Migrations mechanism.

38) Explain the difference between optimistic and pessimistic locking.

39) ASsociations and them examples
