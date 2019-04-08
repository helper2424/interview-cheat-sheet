class Test
	p self
	def self.test
		p self

	end

	class << self

	p self

	def test2
		p self
		1.times do 
			p  "#{self}!!!"
		end

	end

	end
end

p self
Test.test
Test.test2