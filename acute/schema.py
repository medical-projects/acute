"""
Define acute schemas.
"""
from acute import models

list_columns = [
    models.Demographics,
    models.Location,
    models.Allergies,
    models.Diagnosis,
    models.PastMedicalHistory,
    models.Antimicrobial,
    models.Investigation
]

list_schemas = {
    'default': list_columns,
}

detail_columns = list_columns