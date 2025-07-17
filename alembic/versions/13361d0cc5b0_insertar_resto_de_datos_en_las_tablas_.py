"""Insertar resto de  datos en las tablas de la ruta 2

Revision ID: 13361d0cc5b0
Revises: 413c59219208
Create Date: 2024-10-16 20:21:47.261616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13361d0cc5b0'
down_revision: Union[str, None] = '413c59219208'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
# Insertar datos en la tabla disponibilidad_atajos
    disponibilidad_atajos_table = sa.table('disponibilidad_atajos',
                                           sa.column('atajo_id', sa.Integer),
                                           sa.column('senderismo', sa.Boolean),
                                           sa.column('bici_tour', sa.Boolean),
                                           sa.column('moto', sa.Boolean),
                                           sa.column('automovil', sa.Boolean))
    
    op.bulk_insert(disponibilidad_atajos_table,
                   [
                       {'atajo_id': 1, 'senderismo': True, 'bici_tour': True, 'moto': True, 'automovil': False},
                       {'atajo_id': 2, 'senderismo': False, 'bici_tour': False, 'moto': False, 'automovil': False},
                       {'atajo_id': 3, 'senderismo': False, 'bici_tour': False, 'moto': False, 'automovil': False},
                   ])

    # Insertar datos en la tabla coordenadas_atajos
    coordenadas_atajos_table = sa.table('coordenadas_atajos',
                                        sa.column('atajo_id', sa.Integer),
                                        sa.column('cordenadas', sa.JSON))
    
    op.bulk_insert(coordenadas_atajos_table,
                    [
                       {'atajo_id': 1, 'cordenadas': [
                           {"lat": 5.113956, "lng": -73.803188},
                           {"lat": 5.114023, "lng": -73.803203},
                           {"lat": 5.114040, "lng": -73.803288},
                           {"lat": 5.113997, "lng": -73.803351},
                           {"lat": 5.114024, "lng": -73.803391},
                           {"lat": 5.114017, "lng": -73.803445},
                           {"lat": 5.114035, "lng": -73.803567},
                           {"lat": 5.114011, "lng": -73.803707},
                           {"lat": 5.114008, "lng": -73.803915},
                           {"lat": 5.114151, "lng": -73.804193},
                           {"lat": 5.114109, "lng": -73.804299},
                           {"lat": 5.114192, "lng": -73.804551},
                           {"lat": 5.114188, "lng": -73.804772},
                           {"lat": 5.114244, "lng": -73.804941},
                           {"lat": 5.114262, "lng": -73.805090},
                           {"lat": 5.114405, "lng": -73.805207}
                       ]},
                       {'atajo_id': 2, 'cordenadas': [
                           {"lat": 5.115032, "lng": -73.805580},
                           {"lat": 5.115071, "lng": -73.805543},
                           {"lat": 5.115105, "lng": -73.805554},
                           {"lat": 5.115130, "lng": -73.805602},
                           {"lat": 5.115170, "lng": -73.805632},
                           {"lat": 5.115217, "lng": -73.805646},
                           {"lat": 5.115218, "lng": -73.805686},
                           {"lat": 5.115472, "lng": -73.805741},
                           {"lat": 5.115579, "lng": -73.805758},
                           {"lat": 5.115766, "lng": -73.805804},
                           {"lat": 5.115881, "lng": -73.805812},
                           {"lat": 5.115945, "lng": -73.805821},
                           {"lat": 5.115978, "lng": -73.805906},
                           {"lat": 5.116012, "lng": -73.805920},
                           {"lat": 5.116037, "lng": -73.805953},
                           {"lat": 5.116123, "lng": -73.806000},
                           {"lat": 5.116160, "lng": -73.806061},
                           {"lat": 5.116215, "lng": -73.806061},
                           {"lat": 5.116244, "lng": -73.806091},
                           {"lat": 5.116318, "lng": -73.806143},
                           {"lat": 5.116354, "lng": -73.806186},
                           {"lat": 5.116378, "lng": -73.806276},
                           {"lat": 5.116459, "lng": -73.806291},
                           {"lat": 5.116509, "lng": -73.806351},
                           {"lat": 5.116577, "lng": -73.806366},
                           {"lat": 5.116700, "lng": -73.806347},
                           {"lat": 5.116740, "lng": -73.806350}
                       ]},
                       {'atajo_id': 3, 'cordenadas': [
                           {"lat": 5.113500, "lng": -73.805889},
                           {"lat": 5.113567, "lng": -73.805999},
                           {"lat": 5.113634, "lng": -73.806077},
                           {"lat": 5.113722, "lng": -73.806256},
                           {"lat": 5.113714, "lng": -73.806334},
                           {"lat": 5.113773, "lng": -73.806554},
                           {"lat": 5.113794, "lng": -73.806664},
                           {"lat": 5.113963, "lng": -73.807064},
                           {"lat": 5.114045, "lng": -73.807166},
                           {"lat": 5.114367, "lng": -73.807575},
                           {"lat": 5.114530, "lng": -73.807706},
                           {"lat": 5.114629, "lng": -73.807749},
                           {"lat": 5.114704, "lng": -73.807907},
                           {"lat": 5.114731, "lng": -73.808087},
                           {"lat": 5.114763, "lng": -73.808226},
                           {"lat": 5.114773, "lng": -73.808430},
                           {"lat": 5.114768, "lng": -73.808532},
                           {"lat": 5.114787, "lng": -73.808558}
                       ]}
                   ])

    # Insertar datos en la tabla coordenadas_principales
    coordenadas_principales_table = sa.table('coordenadas_principales',
                                             sa.column('ruta_id', sa.Integer),
                                             sa.column('cordenadas', sa.JSON))
    
    op.bulk_insert(coordenadas_principales_table,
                   [
                        {'ruta_id': 1, 'cordenadas': [
                            {"lat": 5.103028, "lng": -73.798856},
                            {"lat": 5.103041, "lng": -73.798649},
                            {"lat": 5.103607, "lng": -73.798773},
                            {"lat": 5.103816, "lng": -73.798703},
                            {"lat": 5.104358, "lng": -73.798719},
                            {"lat": 5.104703, "lng": -73.798759},
                            {"lat": 5.105114, "lng": -73.798826},
                            {"lat": 5.105595, "lng": -73.798923},
                            {"lat": 5.106856, "lng": -73.799403},
                            {"lat": 5.107398, "lng": -73.799553},
                            {"lat": 5.107738, "lng": -73.799674},
                            {"lat": 5.108021, "lng": -73.799915},
                            {"lat": 5.108224, "lng": -73.800006},
                            {"lat": 5.108507, "lng": -73.799843},
                            {"lat": 5.108865, "lng": -73.800001},
                            {"lat": 5.109405, "lng": -73.800529},
                            {"lat": 5.109784, "lng": -73.800757},
                            {"lat": 5.109947, "lng": -73.800983},
                            {"lat": 5.110911, "lng": -73.801390},
                            {"lat": 5.111026, "lng": -73.801530},
                            {"lat": 5.110989, "lng": -73.801804},
                            {"lat": 5.111045, "lng": -73.801889},
                            {"lat": 5.111240, "lng": -73.802005},
                            {"lat": 5.111365, "lng": -73.802182},
                            {"lat": 5.111515, "lng": -73.802257},
                            {"lat": 5.111822, "lng": -73.802218},
                            {"lat": 5.112122, "lng": -73.802325},
                            {"lat": 5.112485, "lng": -73.802599},
                            {"lat": 5.113581, "lng": -73.802883},
                            {"lat": 5.113973, "lng": -73.803055},
                            {"lat": 5.113834, "lng": -73.803669},
                            {"lat": 5.113866, "lng": -73.804160},
                            {"lat": 5.113784, "lng": -73.804364},
                            {"lat": 5.113575, "lng": -73.804584},
                            {"lat": 5.113487, "lng": -73.804694},
                            {"lat": 5.113447, "lng": -73.804881},
                            {"lat": 5.113573, "lng": -73.805273},
                            {"lat": 5.113500, "lng": -73.805804},
                            {"lat": 5.113540, "lng": -73.805868},
                            {"lat": 5.113637, "lng": -73.805858},
                            {"lat": 5.114067, "lng": -73.805421},
                            {"lat": 5.114419, "lng": -73.805195},
                            {"lat": 5.114516, "lng": -73.805168},
                            {"lat": 5.114593, "lng": -73.805260},
                            {"lat": 5.114302, "lng": -73.805654},
                            {"lat": 5.114208, "lng": -73.805895},
                            {"lat": 5.114003, "lng": -73.806338},
                            {"lat": 5.114045, "lng": -73.806410},
                            {"lat": 5.114136, "lng": -73.806362},
                            {"lat": 5.114224, "lng": -73.806236},
                            {"lat": 5.114526, "lng": -73.805919},
                            {"lat": 5.114924, "lng": -73.805632},
                            {"lat": 5.115042, "lng": -73.805614},
                            {"lat": 5.115045, "lng": -73.805721},
                            {"lat": 5.114740, "lng": -73.806158},
                            {"lat": 5.114681, "lng": -73.806579},
                            {"lat": 5.114596, "lng": -73.806979},
                            {"lat": 5.114577, "lng": -73.807365},
                            {"lat": 5.114815, "lng": -73.808049},
                            {"lat": 5.114833, "lng": -73.808231},
                            {"lat": 5.114801, "lng": -73.808706},
                            {"lat": 5.114836, "lng": -73.808969},
                            {"lat": 5.114728, "lng": -73.809247},
                            {"lat": 5.114744, "lng": -73.809397},
                            {"lat": 5.115030, "lng": -73.809116},
                            {"lat": 5.115145, "lng": -73.808773},
                            {"lat": 5.115342, "lng": -73.807973},
                            {"lat": 5.115533, "lng": -73.807511},
                            {"lat": 5.115660, "lng": -73.807268},
                            {"lat": 5.115917, "lng": -73.806914},
                            {"lat": 5.116275, "lng": -73.806667},
                            {"lat": 5.116579, "lng": -73.806528},
                            {"lat": 5.116750, "lng": -73.806383}
                        ]}
                    ])


def downgrade() -> None:
    pass
