try

n=input('Introduzca un número: ');
L=1:n;
total = 0;
if nnz(rem(n,L)==0)==2
    disp('Número primo');
    total = ('Numero primo');
else
    disp('Número compuesto');
    total = ('Numero Compuesto')
end

catch
 disp('algo salio mal');
 total = ('algo salio mal');
end_try_catch

pkg load database
conn = pq_connect (setdbopts ("dbname", "postgres", "host", "localhost", "port", "5432", "user", "postgres", "password", "3062887960313"))
N=pq_exec_params(conn, "insert into p4 values ($1,$2);",{'Programa 1',total});
N=pq_exec_params(conn, 'select * from p4;') %ver datos en la tabla
