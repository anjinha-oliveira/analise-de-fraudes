SELECT 
	distinct cliente_id, 
    clientes.nome, 
    clientes.email, 
    clientes.data_cadastro, 
    clientes.telefone
FROM transacoes AS t1
inner join clientes
on t1.cliente_id = clientes.ID
	WHERE t1.id in
		(SELECT
			t1.ID
		FROM
			transacoes t2
		where
			t1.cliente_id = t2.cliente_id and
			t1.ID != t2.ID and 
			DATEDIFF(MINUTE, t1.data, t2.data) < 2 and t2.data < t1.data
		)
