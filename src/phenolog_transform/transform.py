import uuid # For generating UUIDs for associations

from biolink_model.datamodel.pydanticmodel_v2 import KnowledgeLevelEnum, Association, AgentTypeEnum # Replace * with any necessary data classes from the Biolink Model
from koza.cli_utils import get_koza_app

koza_app = get_koza_app("monarch_phenolog")

while (row := koza_app.get_row()) is not None:
    # Code to transform each row of data
    # For more information, see https://koza.monarchinitiative.org/Ingests/transform
    entity = Association(
        id=str(uuid.uuid1()),
        subject=row["Species A Phenotype ID"],
        predicate="biolink:related_to", # Controlled vocabulary from biolink
        object=row["Species B Phenotype ID"],
        knowledge_level=KnowledgeLevelEnum.statistical_association,
        agent_type=AgentTypeEnum.computational_model, # https://biolink.github.io/biolink-model/AgentTypeEnum/,
##        p_value=row["p-value"]
    )
    koza_app.write(entity)