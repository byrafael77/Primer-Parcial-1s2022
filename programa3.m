try

 precio=input("Ingrese el precio: ");
 siniva = (precio/1.12) ;
 iva = precio - siniva;
 disp("el precio si iva es: ")
 disp(siniva)
 disp("el precio del iva es: ")
 disp(iva)
catch
 disp("Ha ocurrido un error")
end_try_catch

pkg load database
conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "3062887960313"))
pq_exec_params(conn, 'insert into p3 values ($1,$2,$3);',{precio,siniva,iva});
N=pq_exec_params(conn, 'select * from p3;') %ver datos en la tabla
