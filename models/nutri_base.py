# -*- coding: utf-8 -*-

from odoo import models, fields, api


class nutriBase(models.Model):
    _name = 'nutribase.base'

    name = fields.Char('nome de teste')


class nutriIngredient(models.Model):
    _name = 'nutribase.ingredient'

    ingrediente_id = fields.Many2one('nutribase.ingredient.data', string='Ingrediente')
    quantidade = fields.Float('Quantidade')

    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')
    receita_id = fields.Many2one('nutribase.receita', 'Receitas')

    @api.onchange('quantidade')
    def atualiza_ingrediente(self):
        self.proteinas = (self.quantidade * self.ingrediente_id.proteinas) / 100
        self.gorduras = (self.quantidade * self.ingrediente_id.gorduras) / 100
        self.gorduras_saturadas = (self.quantidade * self.ingrediente_id.gorduras_saturadas) / 100
        self.gorduras_trans = (self.quantidade * self.ingrediente_id.gorduras_trans) / 100
        self.fibras = (self.quantidade * self.ingrediente_id.fibras) / 100
        self.sodio = (self.quantidade * self.ingrediente_id.sodio) / 100
        self.carboidratos = (self.quantidade * self.ingrediente_id.carboidratos) / 100
        self.carboidratos = (self.quantidade * self.ingrediente_id.carboidratos) / 100


class nutriIngredientData(models.Model):
    _name = 'nutribase.ingredient.data'

    name = fields.Char('Ingrediente')
    description = fields.Text('Description')
    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')


class nutriReceita(models.Model):
    _name = 'nutribase.receita'

    name = fields.Char('Nome da Receita')
    porcao = fields.Float('Porcao')
    rendimento = fields.Float('Rendimento')
    proteinas = fields.Float('Proteinas')
    gorduras = fields.Float('Gorduras Totais')
    gorduras_saturadas = fields.Float('Gorduras Saturadas')
    gorduras_trans = fields.Float('Gorduras Trans')
    fibras = fields.Float('Fibras')
    sodio = fields.Float('Sodio')
    carboidratos = fields.Float('Carboidratos')
    total_g = fields.Float('Total em Gramas')
    calorias = fields.Float('Calorias')
    ingredientes_ids = fields.One2many('nutribase.ingredient', 'receita_id', string="Ingredientes")
    customer_id = fields.Many2one('res.partner')

    @api.multi
    def atualiza_receita(self):
        self.proteinas = 0
        self.gorduras = 0
        self.gorduras_saturadas = 0
        self.gorduras_trans = 0
        self.fibras = 0
        self.sodio = 0
        self.carboidratos = 0
        self.total_g = 0
        self.calorias = 0

        for i in self.ingredientes_ids:
            self.proteinas += (i.proteinas / self.rendimento) * self.porcao
            self.gorduras += (i.gorduras / self.rendimento) * self.porcao
            self.gorduras_saturadas += (i.gorduras_saturadas / self.rendimento) * self.porcao
            self.gorduras_trans += (i.gorduras_trans / self.rendimento) * self.porcao
            self.fibras += (i.fibras / self.rendimento) * self.porcao
            self.sodio += (i.sodio / self.rendimento) * self.porcao
            self.carboidratos += (i.carboidratos / self.rendimento) * self.porcao
            self.total_g += i.quantidade
        self.calorias = (self.proteinas * 4) + (self.carboidratos * 4) + (self.gorduras * 9)

class nutriVisita(models.Model):
    _name = 'nutribase.visit'

    data_visita = fields.Date('Data da visita')
    partner_id = fields.Many2one('res.partner','Cliente')
    evaluation_ids = fields.One2many('nutribase.visit.evaluate', 'visit_id', string='Avaliações de Setores')


# Opções para avaliações
options_eval = [('s','S'),
                ('n', 'N'),
                ('na', 'NA'),
                ('no', 'NO')]

class nutriVisitaAvaliacao(models.Model):
    _name = 'nutribase.visit.evaluate'

    visit_id = fields.Many2one('nutribase.visit', 'Visita Referente')
    setor = fields.Char('Setor')

    # Adicionar todos os campos para avaliação
    inspecao = fields.Selection(options_eval,
                                string=u'Inspeção')

    inspecao_comment = fields.Text(u'Comentário')

    pre_treatment = fields.Selection(options_eval,
                                string=u'Pré Tratamento')

    pre_treatment_comment = fields.Text(u'Comentário')

    perish_products = fields.Selection(options_eval,
                                string=u'Amostras de Perecíveis')

    perish_products_comment = fields.Text(u'Comentário')

    storage = fields.Selection(options_eval,
                                string=u'Armazenamento a Temperatura Ambiente (Almoxarifado)')

    storage_comment = fields.Text(u'Comentário')

    # Temperatura ambiente
    organization = fields.Selection(options_eval,
                                string=u'Organização')

    organization_comment = fields.Text(u'Comentário')

    pvps = fields.Selection(options_eval,
                                string=u'PVPS',
                                help=u'Controle de rotatividade')

    pvps_comment = fields.Text(u'Comentário')

    perish_date = fields.Selection(options_eval,
                                string=u'Validade dos Produtos',)

    perish_date_comment = fields.Text(u'Comentário')

    chemical_products = fields.Selection(options_eval,
                                string=u'Produtos químicos',)

    chemical_products_comment = fields.Text(u'Comentário')

    cleaning = fields.Selection(options_eval,
                                string=u'Limpeza',)

    cleaning_comment = fields.Text(u'Comentário')

    identification = fields.Selection(options_eval,
                                string=u'Identificação', )

    identification_comment = fields.Text(u'Comentário')

    protection = fields.Selection(options_eval,
                                string=u'Proteção', )

    protection_comment = fields.Text(u'Comentário')

    # temperatura controlada
    contr_organization = fields.Selection(options_eval,
                                string=u'Organização')

    contr_organization_comment = fields.Text(u'Comentário')

    contr_pvps = fields.Selection(options_eval,
                                string=u'PVPS',
                                help=u'Controle de rotatividade')

    contr_pvps_comment = fields.Text(u'Comentário')

    contr_perish_date = fields.Selection(options_eval,
                                string=u'Validade dos Produtos',)

    contr_perish_date_comment = fields.Text(u'Comentário')

    chemical_products = fields.Selection(options_eval,
                                string=u'Produtos químicos',)

    chemical_products_comment = fields.Text(u'Comentário')

    contr_cleaning = fields.Selection(options_eval,
                                string=u'Limpeza',)

    contr_cleaning_comment = fields.Text(u'Comentário')

    contr_identification = fields.Selection(options_eval,
                                string=u'Identificação', )

    contr_identification_comment = fields.Text(u'Comentário')

    contr_protection = fields.Selection(options_eval,
                                string=u'Proteção', )

    contr_protection_comment = fields.Text(u'Comentário')

    contr_crossed_contamination = fields.Selection(options_eval,
                                string=u'Contaminação cruzada', )

    contr_crossed_contamination_comment = fields.Text(u'Comentário')

#         Add Temperaturas


