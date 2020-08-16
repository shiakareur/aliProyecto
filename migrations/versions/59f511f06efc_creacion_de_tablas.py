"""creacion de tablas

Revision ID: 59f511f06efc
Revises: 
Create Date: 2020-08-15 19:51:32.766965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59f511f06efc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modalidad',
    sa.Column('id_modalidad', sa.Integer(), nullable=False),
    sa.Column('nombre_modalidad', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_modalidad')
    )
    op.create_index(op.f('ix_modalidad_nombre_modalidad'), 'modalidad', ['nombre_modalidad'], unique=False)
    op.create_table('persona',
    sa.Column('codigo', sa.Integer(), nullable=False),
    sa.Column('nombres', sa.String(length=120), nullable=False),
    sa.Column('apellido_paterno', sa.String(length=80), nullable=False),
    sa.Column('apellido_materno', sa.String(length=80), nullable=False),
    sa.Column('dni', sa.String(length=8), nullable=False),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=False),
    sa.Column('genero', sa.String(length=1), nullable=False),
    sa.Column('correo', sa.String(length=100), nullable=False),
    sa.Column('telefono', sa.String(length=40), nullable=False),
    sa.Column('direccion', sa.String(length=200), nullable=False),
    sa.Column('hijos', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('codigo')
    )
    op.create_index(op.f('ix_persona_apellido_materno'), 'persona', ['apellido_materno'], unique=False)
    op.create_index(op.f('ix_persona_apellido_paterno'), 'persona', ['apellido_paterno'], unique=False)
    op.create_index(op.f('ix_persona_dni'), 'persona', ['dni'], unique=False)
    op.create_index(op.f('ix_persona_genero'), 'persona', ['genero'], unique=False)
    op.create_table('promocion',
    sa.Column('id_promocion', sa.Integer(), nullable=False),
    sa.Column('nombre_promocion', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_promocion')
    )
    op.create_index(op.f('ix_promocion_nombre_promocion'), 'promocion', ['nombre_promocion'], unique=False)
    op.create_table('usuario',
    sa.Column('nombre_usuario', sa.String(length=45), nullable=False),
    sa.Column('clave', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('nombre_usuario')
    )
    op.create_table('informacion',
    sa.Column('estado', sa.String(length=45), nullable=False),
    sa.Column('planta', sa.String(length=45), nullable=False),
    sa.Column('motivo_cese', sa.String(length=200), nullable=True),
    sa.Column('observaciones', sa.String(length=300), nullable=True),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=False),
    sa.Column('fecha_fin', sa.DateTime(), nullable=True),
    sa.Column('fecha_renovacion', sa.DateTime(), nullable=False),
    sa.Column('fecha_cese', sa.DateTime(), nullable=False),
    sa.Column('codigo_persona', sa.Integer(), nullable=False),
    sa.Column('id_promocion', sa.Integer(), nullable=True),
    sa.Column('id_modalidad', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['codigo_persona'], ['persona.codigo'], ),
    sa.ForeignKeyConstraint(['id_modalidad'], ['modalidad.id_modalidad'], ),
    sa.ForeignKeyConstraint(['id_promocion'], ['promocion.id_promocion'], ),
    sa.PrimaryKeyConstraint('codigo_persona')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('informacion')
    op.drop_table('usuario')
    op.drop_index(op.f('ix_promocion_nombre_promocion'), table_name='promocion')
    op.drop_table('promocion')
    op.drop_index(op.f('ix_persona_genero'), table_name='persona')
    op.drop_index(op.f('ix_persona_dni'), table_name='persona')
    op.drop_index(op.f('ix_persona_apellido_paterno'), table_name='persona')
    op.drop_index(op.f('ix_persona_apellido_materno'), table_name='persona')
    op.drop_table('persona')
    op.drop_index(op.f('ix_modalidad_nombre_modalidad'), table_name='modalidad')
    op.drop_table('modalidad')
    # ### end Alembic commands ###
