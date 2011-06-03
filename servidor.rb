#!/usr/bin/ruby

require 'socket'


if ARGV.empty?
	raise "Uso: ./servidor <porta>"
else
	port = ARGV[0].to_i
end

p port
begin
	# Criamos um servidor na porta fornecida sobre IPV6.
	server = TCPServer.open('::',port)
    if Socket.gethostname != 'macalan'
        nextServer = TCPSocket.open('macalan',port)

rescue Exception => e
	puts "Não pude abrir o socket. Verifique os dados fornecidos."
	raise e
end


loop {
    cliente = server.accept

    if Socket.gethostname == 'macalan'
    	buff = Time.now.ctime
    else
        nextServer.puts("")
        buff = nextServer.gets
    end

    cliente.puts(buff)
    puts buff
    cliente.close
}
