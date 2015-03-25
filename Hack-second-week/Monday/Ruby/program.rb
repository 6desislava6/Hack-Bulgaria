require "base64"

class Proc
  def self.compose(f, g)
    lambda { |*args| f[g[*args]] }
  end
  def *(g)
    Proc.compose(self, g)
  end
end


class RubyRubyRuby
   def initialize(what_to_decode)
      @what_to_decode = what_to_decode
   end
   def answer
      puts "You got that right!"
      puts "You should check out the answer and you might like Ruby!"
      once = lambda { |x| Base64.decode64(x) }
      twice = lambda { |x| Base64.decode64(x) }
      result = once * twice
      puts "Your answer is:"
      puts result[@what_to_decode]
   end
end

hello = RubyRubyRuby.new("YUhSMGNITTZMeTkzZDNjdWNuVmllUzFzWVc1bkxtOXlaeTlpWnk4PQo=\n")
hello.answer
