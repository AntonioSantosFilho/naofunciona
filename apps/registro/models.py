from django.db import models
from django.contrib.auth.models import User  

# Modelo para gerenciar informações básicas dos usuários e sua função como vendedor
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True)
    is_vendedor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

# Modelo que contém informações adicionais sobre vendedores, como localização e status
class Vendedor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE) #cascata para deletar o usuário
    localizacao = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='vendedores/', blank=True, null=True)
    status = models.BooleanField(default=True)  # True para ativo, False para inativo
    
    def __str__(self):
        return self.usuario.nome

# Modelo para descrever os produtos oferecidos pelos vendedores
class Produto(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidade = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    
    def __str__(self):
        return self.nome

# Modelo que registra os pedidos feitos pelos compradores
class Pedido(models.Model):
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pendente', 'Pendente'), ('concluido', 'Concluído')])
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Pedido {self.id} - {self.comprador.nome} para {self.vendedor.usuario.nome}"

# Modelo para armazenar avaliações feitas pelos compradores sobre produtos
class Avaliacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()  # Exemplo de 1 a 5 estrelas
    comentario = models.TextField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Avaliação por {self.avaliador.nome} para o produto {self. produto.nome} do vendedor {self.produto.vendedor.usuario}"

# Modelo para gerenciar as mensagens trocadas entre vendedores e compradores
class Chat(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data_horario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat entre {self.comprador.nome} e {self.vendedor.usuario.nome}"

# Modelo que envia notificações aos usuários sobre eventos importantes
class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    enviado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notificação para {self.usuario.nome}"

# Modelo para registrar detalhes dos pagamentos feitos
class Pagamento(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo_pagamento = models.CharField(max_length=50, choices=[('cartao', 'Cartão de Crédito'), ('boleto', 'Boleto Bancário')])
    pago_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pagamento de {self.produto.nome} em {self.pago_em}"