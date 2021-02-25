import enum
from flask_sqlalchemy import SQLAlchemy
import json  
from dataclasses import asdict, dataclass
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method 

db = SQLAlchemy()

class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    email = db.Column(db.VARCHAR, unique=True, nullable=False)
    _password = db.Column("password", db.VARCHAR, nullable=False)
    place_name = db.Column(db.String, nullable=False)
    address = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    open_hour = db.Column(db.Time, nullable=False)
    close_hour = db.Column(db.Time, nullable=False) 
    menu = db.relationship('Menu', backref='business',lazy=True)

    def __repr__(self):
        return f'business: {self.place_name}'

    @hybrid_property
    def password(self):
        return self._password
    
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "place_name": self.place_name,
            "address": self.address,
            "phone_number": self.phone_number,
            "open_hour": self.open_hour.isoformat(),
            "close_hour": self.close_hour.isoformat(),
            "description": self.description,
        }

    @classmethod
    def get_by_id(cls, place_id):
        profile = cls.query.filter_by(id = place_id).first()
        return profile.to_dict()

    @classmethod
    def get_all_profile(cls):
        return cls.query.all()

    @classmethod
    def delete_profile(cls, place_id):
        profile = cls.query.filter_by(id = place_id).first()
        profile.is_active = False
        db.session.commit()

    @classmethod
    def active_profile(cls, place_id):
        profile = cls.query.filter_by(id = place_id).first()
        profile.is_active = True
        db.session.commit()

    @classmethod  
    def get_by_email(cls, email):
        user = cls.query.filter_by(email = email).first_or_404( description="Invalid username or Password" )
        return user

    @classmethod
    def add(cls, email, password, place_name, address, description, phone_number, open_hour, close_hour):
        user = cls(
            email=email,
            _password=password,
            place_name=place_name,
            address=address,
            description=description,
            phone_number=phone_number,
            open_hour=open_hour,
            close_hour=close_hour
            )
        db.session.add(user)
        db.session.commit()
        return user

    def get_password(self):
        return self._password
    
    def get_is_active(self):
        return self.is_active
    
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey("business.id"), nullable=False)
    template_id = db.Column(db.Integer, db.ForeignKey("template.id"), nullable=False)
    meal = db.relationship('Meal', backref='menu',lazy=True)

    def __repr__(self):
        return f'The menu of business: {self.business_id}'

    def to_dict(self):
        return {
            "id": self.id,
            "business_id": self.business_id,
            "template_id": self.template_id
        }
    @classmethod
    def get_by_business_id(cls, place_id):
        menus = cls.query.filter_by(business_id = place_id).all()
        return [menu.to_dict() for menu in menus]

class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.VARCHAR, nullable=False)
    description = db.Column(db.Text) # add nullable=False
    price = db.Column(db.Float) # add nullable=False
    menu = db.relationship('Menu', backref='template',lazy=True)
    menu_type_id = db.Column(db.Integer, db.ForeignKey("menu_type.id"), nullable=False) # add nullable=False

    def __repr__(self):
        return f'The template is: {self.title}'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }

class Enum_Category(enum.Enum):
    daily_menu = "daily_menu"
    cart_menu = "cart_menu"
    drinks_menu = "drinks_menu"
    dessert_menu = "dessert_menu"
    cocktail_menu = "cocktail_menu"

class Menu_Type(db.Model):
    __tablename__ = 'menu_type'
    id = db.Column(db.Integer, primary_key=True) 
    menu_type = db.Column(db.Enum(Enum_Category), nullable=False)
    template = db.relationship('Template', backref='menu_type',lazy=True)
    

    def __repr__(self):
        return f'The meal is: {self.meal_name}'

    def to_dict(self):
        return {
            "id": self.id,
            "menu_type": self.menu_type
        }

association_table = db.Table('meal_contains_meal_info', db.Model.metadata,
    db.Column('meal', db.Integer, db.ForeignKey('meal.id')),
    db.Column('meal_info', db.Integer, db.ForeignKey('meal_info.id'))
)
class Meal(db.Model):
    __tablename__ = 'meal'
    id = db.Column(db.Integer, primary_key=True) 
    meal_name = db.Column(db.VARCHAR, nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=False) #Add  nullable=False
    meal_info = db.relationship(
        "Meal_Info",
        secondary=association_table,
        back_populates="meal")

    def __repr__(self):
        return f'The meal is: {self.meal_name}'

    def to_dict(self):
        return {
            "id": self.id,
            "meal_name": self.meal_name,
            "price": self.price
        }

class Enum_Info(enum.Enum):
    gluten = "gluten"
    peanuts = "peanuts"
    tree_nuts = "tree_nuts"
    celery = "celery"
    mustard = "mustard"
    eggs = "eggs"
    milk = "milk"
    sesame = "sesame"
    fish = "fish"
    custaceans = "custaceans"
    molluscs = "molluscs"
    soya = "soya"
    sulphites = "sulphites"
    lupin  = "lupin"
    vegetarian_friendly = "vegetarian_friendly"
    vegan_friendly = "vegan_friendly"

class Meal_Info(db.Model):
    __tablename__ = 'meal_info'
    id = db.Column(db.Integer, primary_key=True) 
    info = db.Column(db.Enum(Enum_Info), nullable=False)
    meal = db.relationship(
        "Meal",
        secondary=association_table,
        back_populates="meal_info")

    def __repr__(self):
        return f'The meal info: {self.info}'
    
    def to_dict(self):
        return {
            "id": self.id,
            # do not to_dict the password, its a security breach
        }