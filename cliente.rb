#!/usr/bin/ruby

require 'socket'


hostname = 'macalan'
port = 9090

begin
	sock = TCPSocket.open(hostname, port)
rescue Exception => e
	puts "Não pude me conectar ao host. Verifique os dados fornecidos."
	raise
end



while line = sock.gets
	puts line
end
sock.close
