# -*- coding: utf-8 -*-
from flectra import api, fields, models
from flectra.exceptions import ValidationError


class societyinfo(models.Model):
    _name="society.information"

    no_of_house = fields.Integer(string = "no of houses")
    house_area = fields.Integer(string="total area")
    house_type = fields.Selection([('threebhk','threebhk'),
                                 ('fourbhk','fourbhk')], string="house type",default = "threebhk")
    society_area = fields.Integer(string="total area")
    playground =fields.Boolean(string="Is available")
    start_date = fields.Date(string='data')

    floor_id = fields.Many2one("society.floor",required=True,string="societyfloor")
    name = fields.Char(string="floors")
    amenity_ids = fields.Many2many("society.ameinities", "room_amenity_rel",
                                   "society_id", "amenity_id", string="Amenities")

    @api.constrains('house_area')
    def check_house_area(self):
        if self.house_area < 200.00 or self.house_area > 500.00:
            raise ValidationError("Room Area should be between 200 to 500.")

    @api.onchange('floor_id')
    def _onchange_code(self):
        print("this is onchange",self.no_of_house)
        self.name = self.floor_id.name

class floor(models.Model):
    _name="society.floor"

    @api.depends('room_line')
    def _compute_total_room(self):
        for floor in self:
            print ("LEN----------", len(floor.room_line))
            floor.total_rooms = len(floor.room_line)

    name= fields.Char(string="floors",required=True)
    code= fields.Char(string="floor code")
    room_line = fields.One2many("society.information", "floor_id", string="Rooms")
   # total_house = fields.Integer(string = "total no of floors",readonly=True)
    total_rooms = fields.Integer(string="Total Rooms on Floor",compute ='_compute_total_room',readonly=True, store=True)


class ameinities(models.Model):
    _name="society.ameinities"

    name= fields.Char(string="name of amienity",required=True)
    code=fields.Char(string="code",required=True)

    info_ids = fields.Many2many("society.information", "room_amenity_rel",
                                 "amenity_id", "society_id", string="Amenities")

    total_rooms = fields.Integer(string="Total Rooms on Floor", readonly=True)

    @api.multi
    def count_total_rooms(self):
        print ("IN COUNT ROOMS-------", len(self))
        self.total_rooms = len(self.info_ids)