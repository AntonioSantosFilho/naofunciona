from django.core.management.base import BaseCommand
from faker import Faker
from apps.seu_app.models import Usuario, Vendedor, Produto, Pedido, Avaliacao, Chat, Notificacao, Pagamento
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Criar usuários
        usuarios = []
        for _ in range(200):  # Ajuste para 200 usuários
            usuario = Usuario.objects.create(
                nome=fake.name(),
                email=fake.unique.email(),
                telefone=fake.phone_number(),
                is_vendedor=fake.boolean()
            )
            usuarios.append(usuario)
        
        # Criar vendedores
        vendedores = []
        for usuario in usuarios:
            if usuario.is_vendedor:
                vendedor = Vendedor.objects.create(
                    usuario=usuario,
                    localizacao=fake.address(),
                    telefone=fake.phone_number(),
                    status=fake.boolean()
                )
                vendedores.append(vendedor)
        
        # Criar produtos para cada vendedor
        produtos = []
        for vendedor in vendedores:
            for _ in range(10):  # Ajuste para 10 produtos por vendedor
                produto = Produto.objects.create(
                    vendedor=vendedor,
                    nome=fake.word().capitalize(),
                    descricao=fake.text(),
                    preco=round(random.uniform(10.0, 100.0), 2),
                    disponibilidade=fake.boolean()
                )
                produtos.append(produto)

        # Criar pedidos entre compradores e vendedores
        pedidos = []
        for _ in range(500):  # Ajuste para 500 pedidos
            comprador = random.choice([u for u in usuarios if not u.is_vendedor])
            vendedor = random.choice(vendedores)
            produto = random.choice(produtos)
            pedido = Pedido.objects.create(
                comprador=comprador,
                vendedor=vendedor,
                produto=produto,
                preco_total=produto.preco,
                status=random.choice(['pendente', 'concluido'])
            )
            pedidos.append(pedido)
        
        # Criar avaliações para produtos
        for _ in range(1000):  # Ajuste para 1000 avaliações
            avaliador = random.choice([u for u in usuarios if not u.is_vendedor])
            produto = random.choice(produtos)
            Avaliacao.objects.create(
                produto=produto,
                avaliador=avaliador,
                nota=random.randint(1, 5),
                comentario=fake.text()
            )

        # Criar chats entre compradores e vendedores
        for _ in range(2000):  # Ajuste para 2000 mensagens de chat
            vendedor = random.choice(vendedores)
            comprador = random.choice([u for u in usuarios if not u.is_vendedor])
            Chat.objects.create(
                vendedor=vendedor,
                comprador=comprador,
                mensagem=fake.sentence(),
                data_horario=fake.date_time_this_year()
            )

        # Criar notificações para usuários
        for usuario in usuarios:
            for _ in range(10):  # Ajuste para 10 notificações por usuário
                Notificacao.objects.create(
                    usuario=usuario,
                    mensagem=fake.sentence(),
                    enviado_em=fake.date_time_this_year()
                )

        # Criar pagamentos para produtos
        for produto in produtos:
            for _ in range(2):  # Ajuste para 2 pagamentos por produto
                Pagamento.objects.create(
                    produto=produto,
                    tipo_pagamento=random.choice(['cartao', 'boleto']),
                    pago_em=fake.date_time_this_year()
                )

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com centenas de registros!'))
