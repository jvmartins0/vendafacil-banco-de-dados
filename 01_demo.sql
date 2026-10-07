INSERT INTO produtos(nome,preco,estoque) VALUES('Caderno universitário',18.90,30),('Caneta azul',3.50,100),('Mochila básica',89.90,12) ON CONFLICT(nome) DO NOTHING;
