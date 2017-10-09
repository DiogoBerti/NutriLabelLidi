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
    evaluate_line_ids = fields.One2many('nutribase.visit.evaluate.lines', 'evaluation_id',
                                        string='Relatório de avaliação')

    # Adicionar um stage

class nutriVisitaAvaliacaoLines(models.Model):
    _name = 'nutribase.visit.evaluate.lines'
    evaluation_id = fields.Many2one('nutribase.visit.evaluate')
    value = fields.Selection(options_eval,
                             string=u'Conceito')
    standard_id = fields.Many2one('nutribase.visit.standard', 'Critério')
    standard_description = fields.Text('Descrição do critério', related='standard_id.description')
    standard_comment = fields.Text('Comentários:')


class nutriVisitaCriterios(models.Model):
    _name = 'nutribase.visit.standard'

    name = fields.Char('Nome do Critério')
    description = fields.Text('Descrição')
    standard_type = fields.Selection([('single','Simples'),
                                      ('composed', 'Composto')],
                                     string='Tipo de Critério')
    sub_id = fields.Many2one('nutribase.visit.standard.sub', 'Sub')

class nutriVisitaSubCriterios(models.Model):
    _name = 'nutribase.visit.standard.sub'
    name = fields.Char('Nome do Sub Critério')
    description = fields.Text('Descrição')


