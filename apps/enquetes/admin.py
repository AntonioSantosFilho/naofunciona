from django.contrib import admin
from .models import Usuario, Vendedor, Produto, Pedido, Avaliacao, Chat, Notificacao, Pagamento

# Personalização do Admin para o modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'is_vendedor')  # Campos exibidos na lista
    search_fields = ('nome', 'email')  # Campos para pesquisa
    list_filter = ('is_vendedor',)  # Filtros laterais
    readonly_fields = ('foto',)  # Tornar a foto apenas de leitura se necessário

# Personalização do Admin para o modelo Vendedor
@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'localizacao', 'telefone', 'status')
    search_fields = ('usuario__nome', 'localizacao')
    list_filter = ('status',)

# Inline para produtos associados a vendedores
class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 1  # Quantidade de produtos extras que podem ser adicionados

# Personalização do Admin para o modelo Produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vendedor', 'preco', 'disponibilidade')
    search_fields = ('nome', 'descricao')
    list_filter = ('disponibilidade', 'vendedor')
    readonly_fields = ('imagem',)  # A imagem pode ser apenas visualizada

# Personalização do Admin para o modelo Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('comprador', 'vendedor', 'produto', 'preco_total', 'status', 'atualizado_em')
    search_fields = ('comprador__nome', 'vendedor__usuario__nome', 'produto__nome')
    list_filter = ('status',)
    readonly_fields = ('preco_total', 'atualizado_em')  # Campos não editáveis

# Personalização do Admin para o modelo Avaliacao
@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'avaliador', 'nota', 'data_avaliacao')
    search_fields = ('produto__nome', 'avaliador__nome')
    list_filter = ('nota', 'produto')

# Personalização do Admin para o modelo Chat
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('comprador', 'vendedor', 'data_horario')
    search_fields = ('comprador__nome', 'vendedor__usuario__nome')
    list_filter = ('data_horario',)

# Personalização do Admin para o modelo Notificacao
@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'mensagem', 'enviado_em')
    search_fields = ('usuario__nome', 'mensagem')
    list_filter = ('enviado_em',)

# Personalização do Admin para o modelo Pagamento
@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo_pagamento', 'pago_em')
    search_fields = ('produto__nome', 'tipo_pagamento')
    list_filter = ('tipo_pagamento', 'pago_em')