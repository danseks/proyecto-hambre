"""empty message

Revision ID: 833a90b93728
Revises: 
Create Date: 2021-03-18 11:32:19.201625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '833a90b93728'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.Column('place_name', sa.String(), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('open_hour', sa.Time(), nullable=False),
    sa.Column('close_hour', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('meal_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('info', sa.Enum('gluten', 'peanuts', 'tree_nuts', 'celery', 'mustard', 'eggs', 'milk', 'sesame', 'fish', 'crustaceans', 'molluscs', 'soya', 'sulphites', 'lupin', 'vegetarian_friendly', 'vegan_friendly', name='enum_info'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('menu_type', sa.Enum('daily_menu', 'cart_menu', 'drinks_menu', 'dessert_menu', 'cocktail_menu', name='enum_category'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('menu_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_type_id'], ['menu_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meal_contains_meal_info',
    sa.Column('meal', sa.Integer(), nullable=True),
    sa.Column('meal_info', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meal'], ['meal.id'], ),
    sa.ForeignKeyConstraint(['meal_info'], ['meal_info.id'], )
    )
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.ForeignKeyConstraint(['template_id'], ['template.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('section',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], ),
    sa.ForeignKeyConstraint(['template_id'], ['template.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'meal_id', 'template_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('section')
    op.drop_table('menu')
    op.drop_table('meal_contains_meal_info')
    op.drop_table('template')
    op.drop_table('meal')
    op.drop_table('menu_type')
    op.drop_table('meal_info')
    op.drop_table('business')
    # ### end Alembic commands ###
