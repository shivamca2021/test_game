# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Minesweeper(models.Model):
    _name = 'minesweeper'
    _rec_name = "player_name"
    _description = 'Classic Game'

    player_name = fields.Char(string="Player Name")
    no_of_wins = fields.Integer(string="Number of Wins")
    no_of_losses = fields.Integer(string="Number of Losses")
    avg_game_duration = fields.Float(string="Average Game Duration")
    field_size = fields.Char(string="Field Size")
    no_games = fields.Integer(string="Number of Games")
    country_id = fields.Many2one(comodel_name="res.country",string="Residence Country")

