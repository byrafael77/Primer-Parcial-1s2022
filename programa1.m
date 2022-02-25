try
  
 d1=randi(6)
 d2=randi(6)
 disp("dado 1: ")
 disp(dado1)
 disp("dado 2: ")
 disp(dado2)
 suma = dado1+dado2;
 disp("La suma es: ")
 disp(suma)
 if suma == 7
   disp("Perdedor")
   resultado = ('Perdedor'); 
   pq_exec_params(conn, 'insert into p1 values ($1,$2,$3);',{dado1,dado2,resultado});
 elseif  suma == 8
   disp("Ganador")
   resultado = ('Ganador');
   pq_exec_params(conn, 'insert into p1 values ($1,$2,$3);',{dado1,dado2,resultado});
 else
   disp("Juega de nuevo")
   resultado = ('Juega de nuevo');
   pq_exec_params(conn, 'insert into p1 values ($1,$2,$3);',{dado1,dado2,resultado});
 endif
catch
 disp("Algo salió mal")
end_try_catch
pkg load database
conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "3062887960313"))
N=pq_exec_params(conn, 'select * from p1;')