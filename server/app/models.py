from flask import current_app, request
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, end, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            }
        }
        
        return data

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UnibCombos(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 

    character = db.Column(db.String(15), index=True, nullable=False) 
    ver = db.Column(db.String(10), index=True, nullable=False) 
    damage = db.Column(db.Integer, index=True, nullable=False) 
    cs = db.Column(db.Boolean, index=True, nullable=False) 
    ch = db.Column(db.Boolean, index=True, nullable=False)
    pos = db.Column(db.String(10), index=True, nullable=False) 
    starter = db.Column(db.String(10), index=True, nullable=False) 
    meter = db.Column(db.Integer, index=True, nullable=False)
    
    yt = db.Column(db.String(300), index=True)
    tw = db.Column(db.String(300), index=True)
    bullets = db.Column(db.Integer, index=True)
    enh = db.Column(db.Integer, index=True)
    wSword = db.Column(db.Boolean, index=True)
    wShield = db.Column(db.Boolean, index=True)
    azhi = db.Column(db.Boolean, index=True)

    notation = db.Column(db.String(140))
    desc = db.Column(db.String(140))
    flag = db.Column(db.String(140))

    def to_dict(self):
        data = {
            'id': self.id,
            'character': self.character,
            'ver': self.ver,
            'damage': self.damage,
            'cs': self.cs,
            'ch': self.ch,
            'pos': self.pos,
            'starter': self.starter,
            'meter': self.meter,
            'flag': self.flag
        }

        if self.character == "Eltnum":
            data['bullets'] = self.bullets
            data['enh'] = self.enh
        elif self.character == "Wagner":
            data['wSword'] = self.wSword
            data['wShield'] = self.wShield
        elif self.character == "Chaos":
            data['azhi'] = self.azhi

        if self.yt != None:
            data['yt'] = self.yt
        elif self.tw != None:
            data['tw'] = self.tw
        
        if self.desc != None:
            data['desc'] = self.desc
        if self.notation != None:
            data['notation'] = self.notation
    
        return data
    
    def from_dict(self, data):
        fields = [
            'character', 'ver', 'damage', 'cs', 'ch',
            'starter', 'meter', 'pos', 'yt', 'tw', 'bullets',
            'enh', 'wSword', 'wShield', 'azhi', 'notation', 'desc' 
        ]

        for field in fields:
            if field in data:
                setattr(self, field, data[field])
    
    def get_query(self):
        query = self.query

        if request.args.get('char') is not None and request.args.get('char') != 'All':
            query = query.filter_by(character=request.args.get('char'))
        
        if request.args.get('str') is not None and request.args.get('str') != 'All':
            query = query.filter_by(starter=request.args.get('str'))

        if request.args.get('ver') is not None and request.args.get('ver') == 'CLR':
            query = query.filter_by(ver=request.args.get('ver'))
        else:
            query = query.filter_by(ver='ST')
        
        if request.args.get('mtr1') is not None and request.args.get('mtr2') is not None:
            query = query.filter(self.meter>=int(request.args.get('mtr1')))
            query = query.filter(self.meter<=int(request.args.get('mtr2')))
        
        if request.args.get('pos') is not None:
            query = query.filter_by(pos=request.args.get('pos'))
        else:
            query = query.filter_by(pos='Midscreen')

        if request.args.get('cs') is not None and request.args.get('cs') == 'false':
            query = query.filter_by(cs=False)

        if request.args.get('ch') is not None and request.args.get('ch') == 'true':
            query = query.filter_by(ch=True)
        else:
            query = query.filter_by(ch=False)
        
        if request.args.get('blt') is not None and request.args.get('char') == 'Eltnum':
            query = query.filter(self.bullets<=int(request.args.get('blt')))

        if request.args.get('enh') is not None and request.args.get('char') == 'Eltnum':
            query = query.filter(self.enh<=int(request.args.get('enh')))

        if request.args.get('sw') is not None and request.args.get('char') == 'Wagner' \
           and request.args.get('sw') == 'false':
            query = query.filter_by(wSword=False)

        if request.args.get('sh') is not None and request.args.get('char') == 'Wagner' \
           and request.args.get('sh') == 'false':
            query = query.filter_by(wShield=False)

        if request.args.get('az') is not None and request.args.get('char') == 'Chaos' \
           and request.args.get('az') == 'false':
            query = query.filter_by(azhi=False)

        if request.args.get('flt') == 'Damage':
            query = query.order_by(self.damage.desc())
        
        query = query.order_by(self.id.desc())

        return query
