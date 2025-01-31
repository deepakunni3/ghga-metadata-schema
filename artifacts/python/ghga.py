# Auto generated from ghga.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-12-06T16:37:53
# Schema: GHGA-Metadata-Schema
#
# id: https://w3id.org/GHGA-Metadata-Schema
# description: The metadata schema for the German Human Genome-Phenome Archive (GHGA).
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CLO = CurieNamespace('CLO', 'http://purl.obolibrary.org/obo/CLO_')
COB = CurieNamespace('COB', 'http://purl.obolibrary.org/obo/COB_')
EFO = CurieNamespace('EFO', 'http://www.ebi.ac.uk/efo/EFO_')
GENEPIO = CurieNamespace('GENEPIO', 'http://purl.obolibrary.org/obo/GENEPIO_')
GHGA = CurieNamespace('GHGA', 'https://w3id.org/GHGA/')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://purl.bioontology.org/ontology/SNOMEDCT/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
DEFAULT_ = GHGA


# Types

# Class references
class NamedThingId(extended_str):
    pass


class PlannedProcessId(NamedThingId):
    pass


class InvestigationId(PlannedProcessId):
    pass


class DataTransformationId(PlannedProcessId):
    pass


class ResearchActivityId(PlannedProcessId):
    pass


class ProjectId(ResearchActivityId):
    pass


class StudyId(InvestigationId):
    pass


class ExperimentId(InvestigationId):
    pass


class ExperimentProcessId(PlannedProcessId):
    pass


class AgentId(NamedThingId):
    pass


class PersonId(NamedThingId):
    pass


class IndividualId(PersonId):
    pass


class DonorId(IndividualId):
    pass


class AnalysisId(DataTransformationId):
    pass


class AnalysisProcessId(PlannedProcessId):
    pass


class CommitteeId(NamedThingId):
    pass


class DataAccessCommitteeId(CommitteeId):
    pass


class MemberId(PersonId):
    pass


class MaterialEntityId(NamedThingId):
    pass


class BiospecimenId(MaterialEntityId):
    pass


class SampleId(MaterialEntityId):
    pass


class PopulationId(MaterialEntityId):
    pass


class FamilyId(PopulationId):
    pass


class CohortId(PopulationId):
    pass


class AnatomicalEntityId(MaterialEntityId):
    pass


class CellLineId(MaterialEntityId):
    pass


class BiologicalQualityId(NamedThingId):
    pass


class DiseaseOrPhenotypicFeatureId(BiologicalQualityId):
    pass


class DiseaseId(DiseaseOrPhenotypicFeatureId):
    pass


class PhenotypicFeatureId(DiseaseOrPhenotypicFeatureId):
    pass


class InformationContentEntityId(NamedThingId):
    pass


class ProtocolId(InformationContentEntityId):
    pass


class LibraryPreparationProtocolId(ProtocolId):
    pass


class SequencingProtocolId(ProtocolId):
    pass


class TechnologyId(InformationContentEntityId):
    pass


class WorkflowId(InformationContentEntityId):
    pass


class WorkflowStepId(InformationContentEntityId):
    pass


class FileId(InformationContentEntityId):
    pass


class DatasetId(InformationContentEntityId):
    pass


class DataAccessPolicyId(InformationContentEntityId):
    pass


class PublicationId(InformationContentEntityId):
    pass


class UserId(PersonId):
    pass


class SubmissionId(extended_str):
    pass


class OntologyClassMixinId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A databased entity, concept or class. This is a generic class that is the root of all the other classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.NamedThing
    class_class_curie: ClassVar[str] = "GHGA:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = GHGA.NamedThing

    id: Union[str, NamedThingId] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    creation_date: Optional[str] = None
    update_date: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.update_date is not None and not isinstance(self.update_date, str):
            self.update_date = str(self.update_date)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class Attribute(YAMLRoot):
    """
    A key/value pair that further characterizes an entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Attribute
    class_class_curie: ClassVar[str] = "GHGA:Attribute"
    class_name: ClassVar[str] = "attribute"
    class_model_uri: ClassVar[URIRef] = GHGA.Attribute

    key: str = None
    value: str = None
    key_type: Optional[str] = None
    value_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.key):
            self.MissingRequiredField("key")
        if not isinstance(self.key, str):
            self.key = str(self.key)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.key_type is not None and not isinstance(self.key_type, str):
            self.key_type = str(self.key_type)

        if self.value_type is not None and not isinstance(self.value_type, str):
            self.value_type = str(self.value_type)

        super().__post_init__(**kwargs)


@dataclass
class PlannedProcess(NamedThing):
    """
    A process is an entity that exists in time by occurring or happening, has temporal parts and always involves and
    depends on some entity during the time it occurs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.PlannedProcess
    class_class_curie: ClassVar[str] = "GHGA:PlannedProcess"
    class_name: ClassVar[str] = "planned process"
    class_model_uri: ClassVar[URIRef] = GHGA.PlannedProcess

    id: Union[str, PlannedProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Investigation(PlannedProcess):
    """
    Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the
    object of study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Investigation
    class_class_curie: ClassVar[str] = "GHGA:Investigation"
    class_name: ClassVar[str] = "investigation"
    class_model_uri: ClassVar[URIRef] = GHGA.Investigation

    id: Union[str, InvestigationId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvestigationId):
            self.id = InvestigationId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class DataTransformation(PlannedProcess):
    """
    A data transformation technique used to analyze and interpret data to gain a better understanding of it.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataTransformation
    class_class_curie: ClassVar[str] = "GHGA:DataTransformation"
    class_name: ClassVar[str] = "data transformation"
    class_model_uri: ClassVar[URIRef] = GHGA.DataTransformation

    id: Union[str, DataTransformationId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTransformationId):
            self.id = DataTransformationId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class ResearchActivity(PlannedProcess):
    """
    A planned process executed in the performance of scientific research wherein systematic investigations are
    performed to establish facts and reach new conclusions about phenomena in the world.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ResearchActivity
    class_class_curie: ClassVar[str] = "GHGA:ResearchActivity"
    class_name: ClassVar[str] = "research activity"
    class_model_uri: ClassVar[URIRef] = GHGA.ResearchActivity

    id: Union[str, ResearchActivityId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResearchActivityId):
            self.id = ResearchActivityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Project(ResearchActivity):
    """
    Any specifically defined piece of work that is undertaken or attempted to meet a single requirement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Project
    class_class_curie: ClassVar[str] = "GHGA:Project"
    class_name: ClassVar[str] = "project"
    class_model_uri: ClassVar[URIRef] = GHGA.Project

    id: Union[str, ProjectId] = None
    title: str = None
    description: str = None
    has_publication: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="has_publication", slot_type=Publication, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Study(Investigation):
    """
    Studies are experimental investigations of a particular phenomenon. It involves a detailed examination and
    analysis of a subject to learn more about the phenomenon being studied.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Study
    class_class_curie: ClassVar[str] = "GHGA:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = GHGA.Study

    id: Union[str, StudyId] = None
    affiliation: Union[str, List[str]] = None
    title: str = None
    description: str = None
    type: Union[str, "StudyTypeEnum"] = None
    has_experiment: Optional[Union[Dict[Union[str, ExperimentId], Union[dict, "Experiment"]], List[Union[dict, "Experiment"]]]] = empty_dict()
    has_analysis: Optional[Union[Dict[Union[str, AnalysisId], Union[dict, "Analysis"]], List[Union[dict, "Analysis"]]]] = empty_dict()
    has_project: Optional[Union[dict, Project]] = None
    has_publication: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()
    status: Optional[Union[str, "StatusEnum"]] = None
    accession: Optional[str] = None
    release_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.affiliation):
            self.MissingRequiredField("affiliation")
        if not isinstance(self.affiliation, list):
            self.affiliation = [self.affiliation] if self.affiliation is not None else []
        self.affiliation = [v if isinstance(v, str) else str(v) for v in self.affiliation]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, StudyTypeEnum):
            self.type = StudyTypeEnum(self.type)

        self._normalize_inlined_as_list(slot_name="has_experiment", slot_type=Experiment, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_analysis", slot_type=Analysis, key_name="id", keyed=True)

        if self.has_project is not None and not isinstance(self.has_project, Project):
            self.has_project = Project(**as_dict(self.has_project))

        self._normalize_inlined_as_list(slot_name="has_publication", slot_type=Publication, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        super().__post_init__(**kwargs)


@dataclass
class Experiment(Investigation):
    """
    An experiment is an investigation that consists of a coordinated set of actions and observations designed to
    generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Experiment
    class_class_curie: ClassVar[str] = "GHGA:Experiment"
    class_name: ClassVar[str] = "experiment"
    class_model_uri: ClassVar[URIRef] = GHGA.Experiment

    id: Union[str, ExperimentId] = None
    has_study: Union[dict, Study] = None
    has_sample: Union[dict, "Sample"] = None
    title: str = None
    description: str = None
    biological_replicates: Optional[str] = None
    technical_replicates: Optional[str] = None
    experimental_replicates: Optional[str] = None
    has_technology: Optional[Union[dict, "Technology"]] = None
    has_file: Optional[Union[Dict[Union[str, FileId], Union[dict, "File"]], List[Union[dict, "File"]]]] = empty_dict()
    has_experiment_process: Optional[Union[Dict[Union[str, ExperimentProcessId], Union[dict, "ExperimentProcess"]], List[Union[dict, "ExperimentProcess"]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        if self._is_empty(self.has_study):
            self.MissingRequiredField("has_study")
        if not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self._is_empty(self.has_sample):
            self.MissingRequiredField("has_sample")
        if not isinstance(self.has_sample, Sample):
            self.has_sample = Sample(**as_dict(self.has_sample))

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.biological_replicates is not None and not isinstance(self.biological_replicates, str):
            self.biological_replicates = str(self.biological_replicates)

        if self.technical_replicates is not None and not isinstance(self.technical_replicates, str):
            self.technical_replicates = str(self.technical_replicates)

        if self.experimental_replicates is not None and not isinstance(self.experimental_replicates, str):
            self.experimental_replicates = str(self.experimental_replicates)

        if self.has_technology is not None and not isinstance(self.has_technology, Technology):
            self.has_technology = Technology(**as_dict(self.has_technology))

        self._normalize_inlined_as_list(slot_name="has_file", slot_type=File, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_experiment_process", slot_type=ExperimentProcess, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class ExperimentProcess(PlannedProcess):
    """
    An Experiment Process is a process that describes how a Sample is transformed to a File via an assay. The
    Experiment Process also keeps track of the Protocol used and the Agent that is running the experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ExperimentProcess
    class_class_curie: ClassVar[str] = "GHGA:ExperimentProcess"
    class_name: ClassVar[str] = "experiment process"
    class_model_uri: ClassVar[URIRef] = GHGA.ExperimentProcess

    id: Union[str, ExperimentProcessId] = None
    title: Optional[str] = None
    has_input: Optional[Union[dict, "Sample"]] = None
    has_protocol: Optional[Union[dict, "Protocol"]] = None
    has_agent: Optional[Union[dict, "Agent"]] = None
    has_output: Optional[Union[dict, "File"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentProcessId):
            self.id = ExperimentProcessId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.has_input is not None and not isinstance(self.has_input, Sample):
            self.has_input = Sample(**as_dict(self.has_input))

        if self.has_protocol is not None and not isinstance(self.has_protocol, Protocol):
            self.has_protocol = Protocol(**as_dict(self.has_protocol))

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        if self.has_output is not None and not isinstance(self.has_output, File):
            self.has_output = File(**as_dict(self.has_output))

        super().__post_init__(**kwargs)


@dataclass
class Agent(NamedThing):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an
    entity, or for another agent's activity. Agents include a Person, Organization, or Software that performs an
    activity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Agent
    class_class_curie: ClassVar[str] = "GHGA:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = GHGA.Agent

    id: Union[str, AgentId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgentId):
            self.id = AgentId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowParameter(YAMLRoot):
    """
    A key/value pair that represents a parameter used in a Workflow Step.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.WorkflowParameter
    class_class_curie: ClassVar[str] = "GHGA:WorkflowParameter"
    class_name: ClassVar[str] = "workflow parameter"
    class_model_uri: ClassVar[URIRef] = GHGA.WorkflowParameter

    key: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A member of the species Homo sapiens.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Person
    class_class_curie: ClassVar[str] = "GHGA:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = GHGA.Person

    id: Union[str, PersonId] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    additional_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.given_name is not None and not isinstance(self.given_name, str):
            self.given_name = str(self.given_name)

        if self.family_name is not None and not isinstance(self.family_name, str):
            self.family_name = str(self.family_name)

        if self.additional_name is not None and not isinstance(self.additional_name, str):
            self.additional_name = str(self.additional_name)

        super().__post_init__(**kwargs)


@dataclass
class Individual(Person):
    """
    An Individual is a Person who is participating in a Study.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Individual
    class_class_curie: ClassVar[str] = "GHGA:Individual"
    class_name: ClassVar[str] = "individual"
    class_model_uri: ClassVar[URIRef] = GHGA.Individual

    id: Union[str, IndividualId] = None
    sex: Union[str, "BiologicalSexEnum"] = None
    age: int = None
    vital_status: Union[str, "VitalStatusEnum"] = None
    gender: Optional[str] = None
    year_of_birth: Optional[str] = None
    geographical_region: Optional[str] = None
    ethnicity: Optional[str] = None
    ancestry: Optional[str] = None
    has_parent: Optional[Union[Dict[Union[str, IndividualId], Union[dict, "Individual"]], List[Union[dict, "Individual"]]]] = empty_dict()
    has_children: Optional[Union[Dict[Union[str, IndividualId], Union[dict, "Individual"]], List[Union[dict, "Individual"]]]] = empty_dict()
    has_disease: Optional[Union[Dict[Union[str, DiseaseId], Union[dict, "Disease"]], List[Union[dict, "Disease"]]]] = empty_dict()
    has_phenotypic_feature: Optional[Union[Dict[Union[str, PhenotypicFeatureId], Union[dict, "PhenotypicFeature"]], List[Union[dict, "PhenotypicFeature"]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndividualId):
            self.id = IndividualId(self.id)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, BiologicalSexEnum):
            self.sex = BiologicalSexEnum(self.sex)

        if self._is_empty(self.age):
            self.MissingRequiredField("age")
        if not isinstance(self.age, int):
            self.age = int(self.age)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, VitalStatusEnum):
            self.vital_status = VitalStatusEnum(self.vital_status)

        if self.gender is not None and not isinstance(self.gender, str):
            self.gender = str(self.gender)

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, str):
            self.year_of_birth = str(self.year_of_birth)

        if self.geographical_region is not None and not isinstance(self.geographical_region, str):
            self.geographical_region = str(self.geographical_region)

        if self.ethnicity is not None and not isinstance(self.ethnicity, str):
            self.ethnicity = str(self.ethnicity)

        if self.ancestry is not None and not isinstance(self.ancestry, str):
            self.ancestry = str(self.ancestry)

        self._normalize_inlined_as_list(slot_name="has_parent", slot_type=Individual, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_children", slot_type=Individual, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_disease", slot_type=Disease, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_phenotypic_feature", slot_type=PhenotypicFeature, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Donor(Individual):
    """
    A Donor is an Individual that participates in a research Study by donating a Biospecimen. The use of the
    Biospecimen is restricted to the consent provided by the Donor.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Donor
    class_class_curie: ClassVar[str] = "GHGA:Donor"
    class_name: ClassVar[str] = "donor"
    class_model_uri: ClassVar[URIRef] = GHGA.Donor

    id: Union[str, DonorId] = None
    sex: Union[str, "BiologicalSexEnum"] = None
    age: int = None
    vital_status: Union[str, "VitalStatusEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DonorId):
            self.id = DonorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Analysis(DataTransformation):
    """
    An Analysis is a data transformation that transforms input data to output data. The workflow used to achieve this
    transformation and the individual steps are also captured.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Analysis
    class_class_curie: ClassVar[str] = "GHGA:Analysis"
    class_name: ClassVar[str] = "analysis"
    class_model_uri: ClassVar[URIRef] = GHGA.Analysis

    id: Union[str, AnalysisId] = None
    has_input: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    has_study: Optional[Union[dict, Study]] = None
    has_workflow: Optional[Union[dict, Workflow]] = None
    has_analysis_process: Optional[Union[Dict[Union[str, AnalysisProcessId], Union[dict, "AnalysisProcess"]], List[Union[dict, "AnalysisProcess"]]]] = empty_dict()
    has_output: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisId):
            self.id = AnalysisId(self.id)

        self._normalize_inlined_as_list(slot_name="has_input", slot_type=File, key_name="id", keyed=True)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.has_workflow is not None and not isinstance(self.has_workflow, Workflow):
            self.has_workflow = Workflow(**as_dict(self.has_workflow))

        self._normalize_inlined_as_list(slot_name="has_analysis_process", slot_type=AnalysisProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_output", slot_type=File, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class AnalysisProcess(PlannedProcess):
    """
    An analysis process is a process that describes how one or more Files, from a Study, are transformed to another
    set of Files via a Workflow. The analysis process also keeps track of the workflow metadata and the Agent that is
    running the Analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AnalysisProcess
    class_class_curie: ClassVar[str] = "GHGA:AnalysisProcess"
    class_name: ClassVar[str] = "analysis process"
    class_model_uri: ClassVar[URIRef] = GHGA.AnalysisProcess

    id: Union[str, AnalysisProcessId] = None
    title: Optional[str] = None
    has_input: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    has_workflow_step: Optional[Union[dict, WorkflowStep]] = None
    has_agent: Optional[Union[dict, Agent]] = None
    has_output: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisProcessId):
            self.id = AnalysisProcessId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="has_input", slot_type=File, key_name="id", keyed=True)

        if self.has_workflow_step is not None and not isinstance(self.has_workflow_step, WorkflowStep):
            self.has_workflow_step = WorkflowStep(**as_dict(self.has_workflow_step))

        if self.has_agent is not None and not isinstance(self.has_agent, Agent):
            self.has_agent = Agent(**as_dict(self.has_agent))

        self._normalize_inlined_as_list(slot_name="has_output", slot_type=File, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DataUseCondition(YAMLRoot):
    """
    Data Use Condition represents the use conditions associated with a Dataset. A permission field can have one or
    more terms that collectively defines the data use condition. The modifier determines the interpretation of the use
    permission(s).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataUseCondition
    class_class_curie: ClassVar[str] = "GHGA:DataUseCondition"
    class_name: ClassVar[str] = "data use condition"
    class_model_uri: ClassVar[URIRef] = GHGA.DataUseCondition

    permission: Optional[str] = None
    modifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.permission is not None and not isinstance(self.permission, str):
            self.permission = str(self.permission)

        if self.modifier is not None and not isinstance(self.modifier, str):
            self.modifier = str(self.modifier)

        super().__post_init__(**kwargs)


@dataclass
class Committee(NamedThing):
    """
    A group of people organized for a specific purpose.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Committee
    class_class_curie: ClassVar[str] = "GHGA:Committee"
    class_name: ClassVar[str] = "committee"
    class_model_uri: ClassVar[URIRef] = GHGA.Committee

    id: Union[str, CommitteeId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommitteeId):
            self.id = CommitteeId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessCommittee(Committee):
    """
    A group of members that are delegated to grant access to one or more datasets after ensuring the minimum criteria
    for data sharing has been met, and request for data use does not raise ethical and/or legal concerns.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataAccessCommittee
    class_class_curie: ClassVar[str] = "GHGA:DataAccessCommittee"
    class_name: ClassVar[str] = "data access committee"
    class_model_uri: ClassVar[URIRef] = GHGA.DataAccessCommittee

    id: Union[str, DataAccessCommitteeId] = None
    name: str = None
    description: Optional[str] = None
    main_contact: Optional[Union[str, MemberId]] = None
    has_member: Optional[Union[Dict[Union[str, MemberId], Union[dict, "Member"]], List[Union[dict, "Member"]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAccessCommitteeId):
            self.id = DataAccessCommitteeId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.main_contact is not None and not isinstance(self.main_contact, MemberId):
            self.main_contact = MemberId(self.main_contact)

        self._normalize_inlined_as_list(slot_name="has_member", slot_type=Member, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Member(Person):
    """
    Member of an Organization or a Committee.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Member
    class_class_curie: ClassVar[str] = "GHGA:Member"
    class_name: ClassVar[str] = "member"
    class_model_uri: ClassVar[URIRef] = GHGA.Member

    id: Union[str, MemberId] = None
    email: str = None
    telephone: str = None
    organization: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemberId):
            self.id = MemberId(self.id)

        if self._is_empty(self.email):
            self.MissingRequiredField("email")
        if not isinstance(self.email, str):
            self.email = str(self.email)

        if self._is_empty(self.telephone):
            self.MissingRequiredField("telephone")
        if not isinstance(self.telephone, str):
            self.telephone = str(self.telephone)

        if self._is_empty(self.organization):
            self.MissingRequiredField("organization")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    A material entity is a physical entity that is spatially extended, exists as a whole at any point in time and has
    mass.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.MaterialEntity
    class_class_curie: ClassVar[str] = "GHGA:MaterialEntity"
    class_name: ClassVar[str] = "material entity"
    class_model_uri: ClassVar[URIRef] = GHGA.MaterialEntity

    id: Union[str, MaterialEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Biospecimen(MaterialEntity):
    """
    A Biospecimen is any natural material taken from a biological entity (usually a human) for testing, diagnostics,
    treatment, or research purposes. The Biospecimen is linked to the Individual from which the Biospecimen is
    derived.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Biospecimen
    class_class_curie: ClassVar[str] = "GHGA:Biospecimen"
    class_name: ClassVar[str] = "biospecimen"
    class_model_uri: ClassVar[URIRef] = GHGA.Biospecimen

    id: Union[str, BiospecimenId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    has_individual: Optional[Union[dict, "Individual"]] = None
    has_anatomical_entity: Optional[Union[dict, "AnatomicalEntity"]] = None
    has_disease: Optional[Union[Dict[Union[str, DiseaseId], Union[dict, "Disease"]], List[Union[dict, "Disease"]]]] = empty_dict()
    has_phenotypic_feature: Optional[Union[Dict[Union[str, PhenotypicFeatureId], Union[dict, "PhenotypicFeature"]], List[Union[dict, "PhenotypicFeature"]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiospecimenId):
            self.id = BiospecimenId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.has_individual is not None and not isinstance(self.has_individual, Individual):
            self.has_individual = Individual(**as_dict(self.has_individual))

        if self.has_anatomical_entity is not None and not isinstance(self.has_anatomical_entity, AnatomicalEntity):
            self.has_anatomical_entity = AnatomicalEntity(**as_dict(self.has_anatomical_entity))

        self._normalize_inlined_as_list(slot_name="has_disease", slot_type=Disease, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_phenotypic_feature", slot_type=PhenotypicFeature, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Sample(MaterialEntity):
    """
    A sample is a limited quantity of something to be used for testing, analysis, inspection, investigation,
    demonstration, or trial use. A sample is prepared from a Biospecimen (isolate or tissue).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Sample
    class_class_curie: ClassVar[str] = "GHGA:Sample"
    class_name: ClassVar[str] = "sample"
    class_model_uri: ClassVar[URIRef] = GHGA.Sample

    id: Union[str, SampleId] = None
    name: str = None
    description: str = None
    tissue: str = None
    has_individual: Union[dict, "Individual"] = None
    vital_status_at_sampling: Optional[str] = None
    isolation: Optional[str] = None
    storage: Optional[str] = None
    has_biospecimen: Optional[Union[dict, Biospecimen]] = None
    type: Optional[Union[str, "CaseControlEnum"]] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.tissue):
            self.MissingRequiredField("tissue")
        if not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

        if self._is_empty(self.has_individual):
            self.MissingRequiredField("has_individual")
        if not isinstance(self.has_individual, Individual):
            self.has_individual = Individual(**as_dict(self.has_individual))

        if self.vital_status_at_sampling is not None and not isinstance(self.vital_status_at_sampling, str):
            self.vital_status_at_sampling = str(self.vital_status_at_sampling)

        if self.isolation is not None and not isinstance(self.isolation, str):
            self.isolation = str(self.isolation)

        if self.storage is not None and not isinstance(self.storage, str):
            self.storage = str(self.storage)

        if self.has_biospecimen is not None and not isinstance(self.has_biospecimen, Biospecimen):
            self.has_biospecimen = Biospecimen(**as_dict(self.has_biospecimen))

        if self.type is not None and not isinstance(self.type, CaseControlEnum):
            self.type = CaseControlEnum(self.type)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Population(MaterialEntity):
    """
    A population is a collection of individuals from the same taxonomic class living, counted or sampled at a
    particular site or in a particular area.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Population
    class_class_curie: ClassVar[str] = "GHGA:Population"
    class_name: ClassVar[str] = "population"
    class_model_uri: ClassVar[URIRef] = GHGA.Population

    id: Union[str, PopulationId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PopulationId):
            self.id = PopulationId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Family(Population):
    """
    A domestic group, or a number of domestic groups linked through descent (demonstrated or stipulated) from a common
    ancestor, marriage, or adoption.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Family
    class_class_curie: ClassVar[str] = "GHGA:Family"
    class_name: ClassVar[str] = "family"
    class_model_uri: ClassVar[URIRef] = GHGA.Family

    id: Union[str, FamilyId] = None
    has_member: Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]] = empty_dict()
    has_proband: Optional[Union[dict, Individual]] = None
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyId):
            self.id = FamilyId(self.id)

        self._normalize_inlined_as_list(slot_name="has_member", slot_type=Individual, key_name="id", keyed=True)

        if self.has_proband is not None and not isinstance(self.has_proband, Individual):
            self.has_proband = Individual(**as_dict(self.has_proband))

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Cohort(Population):
    """
    A cohort is a collection of individuals that share a common characteristic/observation and have been grouped
    together for a research study/investigation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Cohort
    class_class_curie: ClassVar[str] = "GHGA:Cohort"
    class_name: ClassVar[str] = "cohort"
    class_model_uri: ClassVar[URIRef] = GHGA.Cohort

    id: Union[str, CohortId] = None
    has_member: Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]] = empty_dict()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CohortId):
            self.id = CohortId(self.id)

        self._normalize_inlined_as_list(slot_name="has_member", slot_type=Individual, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(MaterialEntity):
    """
    Biological entity that is either an individual member of a biological species or constitutes the structural
    organization of an individual member of a biological species.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AnatomicalEntity
    class_class_curie: ClassVar[str] = "GHGA:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = GHGA.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class CellLine(MaterialEntity):
    """
    A cultured cell population that represents a genetically stable and homogenous population of cultured cells that
    shares a common propagation history.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.CellLine
    class_class_curie: ClassVar[str] = "GHGA:CellLine"
    class_name: ClassVar[str] = "cell line"
    class_model_uri: ClassVar[URIRef] = GHGA.CellLine

    id: Union[str, CellLineId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellLineId):
            self.id = CellLineId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalQuality(NamedThing):
    """
    A biological quality is a quality held by a biological entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.BiologicalQuality
    class_class_curie: ClassVar[str] = "GHGA:BiologicalQuality"
    class_name: ClassVar[str] = "biological quality"
    class_model_uri: ClassVar[URIRef] = GHGA.BiologicalQuality

    id: Union[str, BiologicalQualityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalQualityId):
            self.id = BiologicalQualityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseOrPhenotypicFeature(BiologicalQuality):
    """
    Disease or Phenotypic Feature that the entity is associated with. This entity is a union of Disease and Phenotypic
    Feature and exists to accommodate situations where Disease concepts are used interchangeably with Phenotype
    concepts or vice-versa.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DiseaseOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "GHGA:DiseaseOrPhenotypicFeature"
    class_name: ClassVar[str] = "disease or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = GHGA.DiseaseOrPhenotypicFeature

    id: Union[str, DiseaseOrPhenotypicFeatureId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseOrPhenotypicFeatureId):
            self.id = DiseaseOrPhenotypicFeatureId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Disease(DiseaseOrPhenotypicFeature):
    """
    A disease is a disposition to undergo pathological processes that exists in an organism because of one or more
    disorders in that organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Disease
    class_class_curie: ClassVar[str] = "GHGA:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = GHGA.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PhenotypicFeature(DiseaseOrPhenotypicFeature):
    """
    The observable form taken by some character (or group of characters) in an individual or an organism, excluding
    pathology and disease. The detectable outward manifestations of a specific genotype.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.PhenotypicFeature
    class_class_curie: ClassVar[str] = "GHGA:PhenotypicFeature"
    class_name: ClassVar[str] = "phenotypic feature"
    class_model_uri: ClassVar[URIRef] = GHGA.PhenotypicFeature

    id: Union[str, PhenotypicFeatureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypicFeatureId):
            self.id = PhenotypicFeatureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationContentEntity(NamedThing):
    """
    A generically dependent continuant that is about some thing.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.InformationContentEntity
    class_class_curie: ClassVar[str] = "GHGA:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = GHGA.InformationContentEntity

    id: Union[str, InformationContentEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationContentEntityId):
            self.id = InformationContentEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Protocol(InformationContentEntity):
    """
    A plan specification which has sufficient level of detail and quantitative information to communicate it between
    investigation agents, so that different investigation agents will reliably be able to independently reproduce the
    process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Protocol
    class_class_curie: ClassVar[str] = "GHGA:Protocol"
    class_name: ClassVar[str] = "protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.Protocol

    id: Union[str, ProtocolId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    type: Optional[str] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtocolId):
            self.id = ProtocolId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class LibraryPreparationProtocol(Protocol):
    """
    Information about the library preparation of an Experiment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.LibraryPreparationProtocol
    class_class_curie: ClassVar[str] = "GHGA:LibraryPreparationProtocol"
    class_name: ClassVar[str] = "library preparation protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.LibraryPreparationProtocol

    id: Union[str, LibraryPreparationProtocolId] = None
    library_name: str = None
    library_layout: str = None
    library_type: str = None
    library_selection: str = None
    library_construction: str = None
    library_preparation: str = None
    library_construction_kit_retail_name: str = None
    library_construction_kit_manufacturer: str = None
    name: str = None
    description: str = None
    library_level: Optional[str] = None
    primer: Optional[str] = None
    end_bias: Optional[str] = None
    target_regions: Optional[str] = None
    rnaseq_strandedness: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LibraryPreparationProtocolId):
            self.id = LibraryPreparationProtocolId(self.id)

        if self._is_empty(self.library_name):
            self.MissingRequiredField("library_name")
        if not isinstance(self.library_name, str):
            self.library_name = str(self.library_name)

        if self._is_empty(self.library_layout):
            self.MissingRequiredField("library_layout")
        if not isinstance(self.library_layout, str):
            self.library_layout = str(self.library_layout)

        if self._is_empty(self.library_type):
            self.MissingRequiredField("library_type")
        if not isinstance(self.library_type, str):
            self.library_type = str(self.library_type)

        if self._is_empty(self.library_selection):
            self.MissingRequiredField("library_selection")
        if not isinstance(self.library_selection, str):
            self.library_selection = str(self.library_selection)

        if self._is_empty(self.library_construction):
            self.MissingRequiredField("library_construction")
        if not isinstance(self.library_construction, str):
            self.library_construction = str(self.library_construction)

        if self._is_empty(self.library_preparation):
            self.MissingRequiredField("library_preparation")
        if not isinstance(self.library_preparation, str):
            self.library_preparation = str(self.library_preparation)

        if self._is_empty(self.library_construction_kit_retail_name):
            self.MissingRequiredField("library_construction_kit_retail_name")
        if not isinstance(self.library_construction_kit_retail_name, str):
            self.library_construction_kit_retail_name = str(self.library_construction_kit_retail_name)

        if self._is_empty(self.library_construction_kit_manufacturer):
            self.MissingRequiredField("library_construction_kit_manufacturer")
        if not isinstance(self.library_construction_kit_manufacturer, str):
            self.library_construction_kit_manufacturer = str(self.library_construction_kit_manufacturer)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.library_level is not None and not isinstance(self.library_level, str):
            self.library_level = str(self.library_level)

        if self.primer is not None and not isinstance(self.primer, str):
            self.primer = str(self.primer)

        if self.end_bias is not None and not isinstance(self.end_bias, str):
            self.end_bias = str(self.end_bias)

        if self.target_regions is not None and not isinstance(self.target_regions, str):
            self.target_regions = str(self.target_regions)

        if self.rnaseq_strandedness is not None and not isinstance(self.rnaseq_strandedness, str):
            self.rnaseq_strandedness = str(self.rnaseq_strandedness)

        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class SequencingProtocol(Protocol):
    """
    Information about the sequencing of a sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.SequencingProtocol
    class_class_curie: ClassVar[str] = "GHGA:SequencingProtocol"
    class_name: ClassVar[str] = "sequencing protocol"
    class_model_uri: ClassVar[URIRef] = GHGA.SequencingProtocol

    id: Union[str, SequencingProtocolId] = None
    sequencing_center: str = None
    instrument_model: str = None
    read_length: Optional[str] = None
    read_pair_number: Optional[str] = None
    sequencing_length: Optional[str] = None
    target_coverage: Optional[str] = None
    reference_annotation: Optional[str] = None
    lane_number: Optional[str] = None
    flow_cell_id: Optional[str] = None
    flow_cell_type: Optional[str] = None
    umi_barcode_read: Optional[str] = None
    umi_barcode_size: Optional[str] = None
    umi_barcode_offset: Optional[str] = None
    cell_barcode_read: Optional[str] = None
    cell_barcode_offset: Optional[str] = None
    cell_barcode_size: Optional[str] = None
    sample_barcode_read: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequencingProtocolId):
            self.id = SequencingProtocolId(self.id)

        if self._is_empty(self.sequencing_center):
            self.MissingRequiredField("sequencing_center")
        if not isinstance(self.sequencing_center, str):
            self.sequencing_center = str(self.sequencing_center)

        if self._is_empty(self.instrument_model):
            self.MissingRequiredField("instrument_model")
        if not isinstance(self.instrument_model, str):
            self.instrument_model = str(self.instrument_model)

        if self.read_length is not None and not isinstance(self.read_length, str):
            self.read_length = str(self.read_length)

        if self.read_pair_number is not None and not isinstance(self.read_pair_number, str):
            self.read_pair_number = str(self.read_pair_number)

        if self.sequencing_length is not None and not isinstance(self.sequencing_length, str):
            self.sequencing_length = str(self.sequencing_length)

        if self.target_coverage is not None and not isinstance(self.target_coverage, str):
            self.target_coverage = str(self.target_coverage)

        if self.reference_annotation is not None and not isinstance(self.reference_annotation, str):
            self.reference_annotation = str(self.reference_annotation)

        if self.lane_number is not None and not isinstance(self.lane_number, str):
            self.lane_number = str(self.lane_number)

        if self.flow_cell_id is not None and not isinstance(self.flow_cell_id, str):
            self.flow_cell_id = str(self.flow_cell_id)

        if self.flow_cell_type is not None and not isinstance(self.flow_cell_type, str):
            self.flow_cell_type = str(self.flow_cell_type)

        if self.umi_barcode_read is not None and not isinstance(self.umi_barcode_read, str):
            self.umi_barcode_read = str(self.umi_barcode_read)

        if self.umi_barcode_size is not None and not isinstance(self.umi_barcode_size, str):
            self.umi_barcode_size = str(self.umi_barcode_size)

        if self.umi_barcode_offset is not None and not isinstance(self.umi_barcode_offset, str):
            self.umi_barcode_offset = str(self.umi_barcode_offset)

        if self.cell_barcode_read is not None and not isinstance(self.cell_barcode_read, str):
            self.cell_barcode_read = str(self.cell_barcode_read)

        if self.cell_barcode_offset is not None and not isinstance(self.cell_barcode_offset, str):
            self.cell_barcode_offset = str(self.cell_barcode_offset)

        if self.cell_barcode_size is not None and not isinstance(self.cell_barcode_size, str):
            self.cell_barcode_size = str(self.cell_barcode_size)

        if self.sample_barcode_read is not None and not isinstance(self.sample_barcode_read, str):
            self.sample_barcode_read = str(self.sample_barcode_read)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Technology(InformationContentEntity):
    """
    A Technology is an abstraction that represents the instrument used for an assay. The Technology entity captures
    instrument-specific attributes that are relevant for an Experiment entity. The Technology entity may be further
    characterized by its children where each child has fields that are relevant to that particular technology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Technology
    class_class_curie: ClassVar[str] = "GHGA:Technology"
    class_name: ClassVar[str] = "technology"
    class_model_uri: ClassVar[URIRef] = GHGA.Technology

    id: Union[str, TechnologyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnologyId):
            self.id = TechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Workflow(InformationContentEntity):
    """
    A Workflow is an abstraction that represents the workflow used to perform an analysis. The Workflow entity
    captures workflow-specific attributes that are relevant for an Analysis entity. The Workflow entity may be further
    characterized by its children where each child has fields that are relevant to that particular workflow.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Workflow
    class_class_curie: ClassVar[str] = "GHGA:Workflow"
    class_name: ClassVar[str] = "workflow"
    class_model_uri: ClassVar[URIRef] = GHGA.Workflow

    id: Union[str, WorkflowId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowId):
            self.id = WorkflowId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class WorkflowStep(InformationContentEntity):
    """
    A Workflow Step represents each individual step performed in a Workflow. If the Workflow is a single-step workflow
    then the Workflow has just one Workflow Step entity. If the Workflow is a multi-step workflow then the Workflow
    has a Workflow Step entity for each step. All Workflow step specific attributes like parameters, and metadata
    about execution environment are captured by the Workflow Step entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.WorkflowStep
    class_class_curie: ClassVar[str] = "GHGA:WorkflowStep"
    class_name: ClassVar[str] = "workflow step"
    class_model_uri: ClassVar[URIRef] = GHGA.WorkflowStep

    id: Union[str, WorkflowStepId] = None
    has_parameter: Optional[Union[Union[dict, "WorkflowParameter"], List[Union[dict, "WorkflowParameter"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowStepId):
            self.id = WorkflowStepId(self.id)

        if not isinstance(self.has_parameter, list):
            self.has_parameter = [self.has_parameter] if self.has_parameter is not None else []
        self.has_parameter = [v if isinstance(v, WorkflowParameter) else WorkflowParameter(**as_dict(v)) for v in self.has_parameter]

        super().__post_init__(**kwargs)


@dataclass
class File(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.File
    class_class_curie: ClassVar[str] = "GHGA:File"
    class_name: ClassVar[str] = "file"
    class_model_uri: ClassVar[URIRef] = GHGA.File

    id: Union[str, FileId] = None
    name: str = None
    format: Optional[str] = None
    size: Optional[str] = None
    checksum: Optional[str] = None
    file_index: Optional[str] = None
    category: Optional[str] = None
    type: Optional[Union[str, "FileTypeEnum"]] = None
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self.file_index is not None and not isinstance(self.file_index, str):
            self.file_index = str(self.file_index)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.type is not None and not isinstance(self.type, FileTypeEnum):
            self.type = FileTypeEnum(self.type)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(InformationContentEntity):
    """
    A Dataset is a collection of Files that is prepared for distribution and is tied to a Data Access Policy.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Dataset
    class_class_curie: ClassVar[str] = "GHGA:Dataset"
    class_name: ClassVar[str] = "dataset"
    class_model_uri: ClassVar[URIRef] = GHGA.Dataset

    id: Union[str, DatasetId] = None
    title: str = None
    description: str = None
    has_study: Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]] = empty_dict()
    has_experiment: Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]] = empty_dict()
    has_sample: Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]] = empty_dict()
    has_analysis: Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]] = empty_dict()
    has_file: Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]] = empty_dict()
    has_data_access_policy: Union[Dict[Union[str, DataAccessPolicyId], Union[dict, "DataAccessPolicy"]], List[Union[dict, "DataAccessPolicy"]]] = empty_dict()
    type: str = None
    has_publication: Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]] = empty_dict()
    accession: Optional[str] = None
    status: Optional[Union[str, "StatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.has_study):
            self.MissingRequiredField("has_study")
        self._normalize_inlined_as_list(slot_name="has_study", slot_type=Study, key_name="id", keyed=True)

        if self._is_empty(self.has_experiment):
            self.MissingRequiredField("has_experiment")
        self._normalize_inlined_as_list(slot_name="has_experiment", slot_type=Analysis, key_name="id", keyed=True)

        if self._is_empty(self.has_sample):
            self.MissingRequiredField("has_sample")
        self._normalize_inlined_as_list(slot_name="has_sample", slot_type=Study, key_name="id", keyed=True)

        if self._is_empty(self.has_analysis):
            self.MissingRequiredField("has_analysis")
        self._normalize_inlined_as_list(slot_name="has_analysis", slot_type=Study, key_name="id", keyed=True)

        if self._is_empty(self.has_file):
            self.MissingRequiredField("has_file")
        self._normalize_inlined_as_list(slot_name="has_file", slot_type=File, key_name="id", keyed=True)

        if self._is_empty(self.has_data_access_policy):
            self.MissingRequiredField("has_data_access_policy")
        self._normalize_inlined_as_list(slot_name="has_data_access_policy", slot_type=DataAccessPolicy, key_name="id", keyed=True)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        self._normalize_inlined_as_list(slot_name="has_publication", slot_type=Publication, key_name="id", keyed=True)

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        super().__post_init__(**kwargs)


@dataclass
class DataAccessPolicy(InformationContentEntity):
    """
    A Data Access Policy specifies under which circumstances, legal or otherwise, a user can have access to one or
    more Datasets belonging to one or more Studies.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DataAccessPolicy
    class_class_curie: ClassVar[str] = "GHGA:DataAccessPolicy"
    class_name: ClassVar[str] = "data access policy"
    class_model_uri: ClassVar[URIRef] = GHGA.DataAccessPolicy

    id: Union[str, DataAccessPolicyId] = None
    description: str = None
    policy_text: str = None
    has_data_access_committee: Union[dict, "DataAccessCommittee"] = None
    name: Optional[str] = None
    policy_url: Optional[str] = None
    has_data_use_condition: Optional[Union[Union[dict, DataUseCondition], List[Union[dict, DataUseCondition]]]] = empty_list()
    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAccessPolicyId):
            self.id = DataAccessPolicyId(self.id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.policy_text):
            self.MissingRequiredField("policy_text")
        if not isinstance(self.policy_text, str):
            self.policy_text = str(self.policy_text)

        if self._is_empty(self.has_data_access_committee):
            self.MissingRequiredField("has_data_access_committee")
        if not isinstance(self.has_data_access_committee, DataAccessCommittee):
            self.has_data_access_committee = DataAccessCommittee(**as_dict(self.has_data_access_committee))

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.policy_url is not None and not isinstance(self.policy_url, str):
            self.policy_url = str(self.policy_url)

        if not isinstance(self.has_data_use_condition, list):
            self.has_data_use_condition = [self.has_data_use_condition] if self.has_data_use_condition is not None else []
        self.has_data_use_condition = [v if isinstance(v, DataUseCondition) else DataUseCondition(**as_dict(v)) for v in self.has_data_use_condition]

        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class Publication(InformationContentEntity):
    """
    The Publication entity represents a publication. While a publication can be any article that is published, the
    minimum expectation is that the publication has a valid DOI.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Publication
    class_class_curie: ClassVar[str] = "GHGA:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = GHGA.Publication

    id: Union[str, PublicationId] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    xref: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        super().__post_init__(**kwargs)


@dataclass
class User(Person):
    """
    A user in GHGA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.User
    class_class_curie: ClassVar[str] = "GHGA:User"
    class_name: ClassVar[str] = "user"
    class_model_uri: ClassVar[URIRef] = GHGA.User

    id: Union[str, UserId] = None
    email: Optional[str] = None
    role: Optional[Union[str, "UserRoleEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserId):
            self.id = UserId(self.id)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.role is not None and not isinstance(self.role, UserRoleEnum):
            self.role = UserRoleEnum(self.role)

        super().__post_init__(**kwargs)


@dataclass
class Submission(YAMLRoot):
    """
    A grouping entity that represents information about one or more entities. A submission can be considered as a set
    of inter-related (and inter-connected) entities that represent a data submission to GHGA.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.Submission
    class_class_curie: ClassVar[str] = "GHGA:Submission"
    class_name: ClassVar[str] = "submission"
    class_model_uri: ClassVar[URIRef] = GHGA.Submission

    id: Union[str, SubmissionId] = None
    has_study: Optional[Union[dict, Study]] = None
    has_project: Optional[Union[dict, Project]] = None
    has_sample: Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]] = empty_dict()
    has_biospecimen: Optional[Union[Dict[Union[str, BiospecimenId], Union[dict, Biospecimen]], List[Union[dict, Biospecimen]]]] = empty_dict()
    has_individual: Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]] = empty_dict()
    has_experiment: Optional[Union[Dict[Union[str, ExperimentId], Union[dict, Experiment]], List[Union[dict, Experiment]]]] = empty_dict()
    has_analysis: Optional[Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]]] = empty_dict()
    has_file: Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]] = empty_dict()
    has_data_access_policy: Optional[Union[dict, DataAccessPolicy]] = None
    submission_date: Optional[str] = None
    creation_date: Optional[str] = None
    update_date: Optional[str] = None
    status: Optional[Union[str, "StatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubmissionId):
            self.id = SubmissionId(self.id)

        if self.has_study is not None and not isinstance(self.has_study, Study):
            self.has_study = Study(**as_dict(self.has_study))

        if self.has_project is not None and not isinstance(self.has_project, Project):
            self.has_project = Project(**as_dict(self.has_project))

        self._normalize_inlined_as_list(slot_name="has_sample", slot_type=Sample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_biospecimen", slot_type=Biospecimen, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_individual", slot_type=Individual, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_experiment", slot_type=Experiment, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_analysis", slot_type=Analysis, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_file", slot_type=File, key_name="id", keyed=True)

        if self.has_data_access_policy is not None and not isinstance(self.has_data_access_policy, DataAccessPolicy):
            self.has_data_access_policy = DataAccessPolicy(**as_dict(self.has_data_access_policy))

        if self.submission_date is not None and not isinstance(self.submission_date, str):
            self.submission_date = str(self.submission_date)

        if self.creation_date is not None and not isinstance(self.creation_date, str):
            self.creation_date = str(self.creation_date)

        if self.update_date is not None and not isinstance(self.update_date, str):
            self.update_date = str(self.update_date)

        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClassMixin(YAMLRoot):
    """
    Mixin for entities that represent an class/term/concept from an ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.OntologyClassMixin
    class_class_curie: ClassVar[str] = "GHGA:OntologyClassMixin"
    class_name: ClassVar[str] = "ontology class mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.OntologyClassMixin

    id: Union[str, OntologyClassMixinId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassMixinId):
            self.id = OntologyClassMixinId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class AccessionMixin(YAMLRoot):
    """
    Mixin for entities that can be assigned a GHGA accession.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AccessionMixin
    class_class_curie: ClassVar[str] = "GHGA:AccessionMixin"
    class_name: ClassVar[str] = "accession mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.AccessionMixin

    accession: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.accession is not None and not isinstance(self.accession, str):
            self.accession = str(self.accession)

        super().__post_init__(**kwargs)


@dataclass
class AttributeMixin(YAMLRoot):
    """
    Mixin for entities that can have one or more attributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.AttributeMixin
    class_class_curie: ClassVar[str] = "GHGA:AttributeMixin"
    class_name: ClassVar[str] = "attribute mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.AttributeMixin

    has_attribute: Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="has_attribute", slot_type=Attribute, key_name="key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class PublicationMixin(YAMLRoot):
    """
    Mixin for entities that can have one or more publications.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.PublicationMixin
    class_class_curie: ClassVar[str] = "GHGA:PublicationMixin"
    class_name: ClassVar[str] = "publication mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.PublicationMixin

    has_publication: Optional[Union[str, PublicationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_publication is not None and not isinstance(self.has_publication, PublicationId):
            self.has_publication = PublicationId(self.has_publication)

        super().__post_init__(**kwargs)


@dataclass
class DeprecatedMixin(YAMLRoot):
    """
    Mixin for entities that can be deprecated.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.DeprecatedMixin
    class_class_curie: ClassVar[str] = "GHGA:DeprecatedMixin"
    class_name: ClassVar[str] = "deprecated mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.DeprecatedMixin

    replaced_by: Optional[Union[str, NamedThingId]] = None
    deprecation_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.replaced_by is not None and not isinstance(self.replaced_by, NamedThingId):
            self.replaced_by = NamedThingId(self.replaced_by)

        if self.deprecation_date is not None and not isinstance(self.deprecation_date, str):
            self.deprecation_date = str(self.deprecation_date)

        super().__post_init__(**kwargs)


@dataclass
class StatusMixin(YAMLRoot):
    """
    Mixin for entities that can have a status.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.StatusMixin
    class_class_curie: ClassVar[str] = "GHGA:StatusMixin"
    class_name: ClassVar[str] = "status mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.StatusMixin

    status: Optional[Union[str, "StatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.status is not None and not isinstance(self.status, StatusEnum):
            self.status = StatusEnum(self.status)

        super().__post_init__(**kwargs)


@dataclass
class ReleaseMixin(YAMLRoot):
    """
    Mixin for entities that can be released at a later point in time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GHGA.ReleaseMixin
    class_class_curie: ClassVar[str] = "GHGA:ReleaseMixin"
    class_name: ClassVar[str] = "release mixin"
    class_model_uri: ClassVar[URIRef] = GHGA.ReleaseMixin

    release_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.release_date is not None and not isinstance(self.release_date, str):
            self.release_date = str(self.release_date)

        super().__post_init__(**kwargs)


# Enumerations
class CaseControlEnum(EnumDefinitionImpl):
    """
    Enum to capture whether a Sample is to be considered as Case or Control.
    """
    control = PermissibleValue(text="control",
                                     description="The Sample is to be treated as Control")
    case = PermissibleValue(text="case",
                               description="The Sample is to be treated as Case")

    _defn = EnumDefinition(
        name="CaseControlEnum",
        description="Enum to capture whether a Sample is to be considered as Case or Control.",
    )

class BiologicalSexEnum(EnumDefinitionImpl):
    """
    The biological sex of an Individual as determined by their chromosomes.
    """
    XX = PermissibleValue(text="XX",
                           description="Female")
    XY = PermissibleValue(text="XY",
                           description="Male")
    none = PermissibleValue(text="none",
                               description="unspecified")

    _defn = EnumDefinition(
        name="BiologicalSexEnum",
        description="The biological sex of an Individual as determined by their chromosomes.",
    )

class UserRoleEnum(EnumDefinitionImpl):
    """
    Enum to capture the different roles a GHGA User can have.
    """
    _defn = EnumDefinition(
        name="UserRoleEnum",
        description="Enum to capture the different roles a GHGA User can have.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "data requester",
                PermissibleValue(text="data requester",
                                 description="Role of a Data Requester where the user requests access to one or more Datasets.") )
        setattr(cls, "data steward",
                PermissibleValue(text="data steward",
                                 description="Role of a Data Steward where the user is responsible for approving request from a user for one or more Datasets.") )

class VitalStatusEnum(EnumDefinitionImpl):
    """
    Enum to capture the vital status of an individual.
    """
    alive = PermissibleValue(text="alive",
                                 description="Showing characteristics of life; displaying signs of life.")
    deceased = PermissibleValue(text="deceased",
                                       description="The cessation of life.")
    unknown = PermissibleValue(text="unknown",
                                     description="Vital status is unknown.")

    _defn = EnumDefinition(
        name="VitalStatusEnum",
        description="Enum to capture the vital status of an individual.",
    )

class StudyTypeEnum(EnumDefinitionImpl):
    """
    Enum to capture the type of a study.
    """
    whole_genome_sequencing = PermissibleValue(text="whole_genome_sequencing",
                                                                     description="Whole Genome Sequencing")
    metagenomics = PermissibleValue(text="metagenomics",
                                               description="Metagenomics")
    transcriptome_analysis = PermissibleValue(text="transcriptome_analysis",
                                                                   description="Transcriptome Analysis")
    resequencing = PermissibleValue(text="resequencing",
                                               description="Resequencing")
    epigenetics = PermissibleValue(text="epigenetics",
                                             description="Epigenetics")
    synthetic_genomics = PermissibleValue(text="synthetic_genomics",
                                                           description="Sythetic Genomics")
    forensic_paleo_genomics = PermissibleValue(text="forensic_paleo_genomics",
                                                                     description="Forensic or Paleo-genomics")
    gene_regulation = PermissibleValue(text="gene_regulation",
                                                     description="Gene Regulation Study")
    cancer_genomics = PermissibleValue(text="cancer_genomics",
                                                     description="Cancer Genomics")
    population_genomics = PermissibleValue(text="population_genomics",
                                                             description="Population Genomics")
    rna_seq = PermissibleValue(text="rna_seq",
                                     description="RNAseq")
    exome_sequencing = PermissibleValue(text="exome_sequencing",
                                                       description="Exome Sequencing")
    pooled_clone_sequencing = PermissibleValue(text="pooled_clone_sequencing",
                                                                     description="Pooled Clone Sequencing")
    other = PermissibleValue(text="other",
                                 description="Other study")

    _defn = EnumDefinition(
        name="StudyTypeEnum",
        description="Enum to capture the type of a study.",
    )

class FileTypeEnum(EnumDefinitionImpl):
    """
    Enum to capture file types.
    """
    bam = PermissibleValue(text="bam",
                             description="BAM File")
    complete_genomics = PermissibleValue(text="complete_genomics",
                                                         description="Complete Genomics File")
    cram = PermissibleValue(text="cram",
                               description="CRAM File")
    fasta = PermissibleValue(text="fasta",
                                 description="Fasta File")
    fastq = PermissibleValue(text="fastq",
                                 description="FastQ File")
    pacbio_hdf5 = PermissibleValue(text="pacbio_hdf5",
                                             description="PacBio HDF5 File")
    sff = PermissibleValue(text="sff",
                             description="Standard flowgram format used to encode results  of pyrosequencing from the 454 Life Sciences platform.")
    srf = PermissibleValue(text="srf",
                             description="SRF is a generic format for DNA sequence data.")
    vcf = PermissibleValue(text="vcf",
                             description="vcf File for storing gene sequence variations.")

    _defn = EnumDefinition(
        name="FileTypeEnum",
        description="Enum to capture file types.",
    )

class StatusEnum(EnumDefinitionImpl):
    """
    Enum to capture the status of an entity.
    """
    submitted = PermissibleValue(text="submitted",
                                         description="Signifies that the entity has been successfully submitted.")
    unreleased = PermissibleValue(text="unreleased",
                                           description="Signifies that the entity is submitted but unreleased for public consumption.")
    released = PermissibleValue(text="released",
                                       description="Signifies that the entity is submitted and released for public consumption.")
    deprecated = PermissibleValue(text="deprecated",
                                           description="Signifies that the entity is deprecated and may be replaced by another entity.")

    _defn = EnumDefinition(
        name="StatusEnum",
        description="Enum to capture the status of an entity.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "in progress",
                PermissibleValue(text="in progress",
                                 description="Signifies that the entity is in the process of being submitted.") )

# Slots
class slots:
    pass

slots.id = Slot(uri=GHGA.id, name="id", curie=GHGA.curie('id'),
                   model_uri=GHGA.id, domain=None, range=URIRef)

slots.accession = Slot(uri=GHGA.accession, name="accession", curie=GHGA.curie('accession'),
                   model_uri=GHGA.accession, domain=None, range=Optional[str])

slots.given_name = Slot(uri=GHGA.given_name, name="given name", curie=GHGA.curie('given_name'),
                   model_uri=GHGA.given_name, domain=None, range=Optional[str])

slots.family_name = Slot(uri=GHGA.family_name, name="family name", curie=GHGA.curie('family_name'),
                   model_uri=GHGA.family_name, domain=None, range=Optional[str])

slots.additional_name = Slot(uri=GHGA.additional_name, name="additional name", curie=GHGA.curie('additional_name'),
                   model_uri=GHGA.additional_name, domain=None, range=Optional[str])

slots.name = Slot(uri=GHGA.name, name="name", curie=GHGA.curie('name'),
                   model_uri=GHGA.name, domain=None, range=Optional[str])

slots.type = Slot(uri=GHGA.type, name="type", curie=GHGA.curie('type'),
                   model_uri=GHGA.type, domain=None, range=Optional[str])

slots.title = Slot(uri=GHGA.title, name="title", curie=GHGA.curie('title'),
                   model_uri=GHGA.title, domain=None, range=Optional[str])

slots.abstract = Slot(uri=GHGA.abstract, name="abstract", curie=GHGA.curie('abstract'),
                   model_uri=GHGA.abstract, domain=None, range=Optional[str])

slots.technical_replicates = Slot(uri=GHGA.technical_replicates, name="technical replicates", curie=GHGA.curie('technical_replicates'),
                   model_uri=GHGA.technical_replicates, domain=None, range=Optional[str])

slots.biological_replicates = Slot(uri=GHGA.biological_replicates, name="biological replicates", curie=GHGA.curie('biological_replicates'),
                   model_uri=GHGA.biological_replicates, domain=None, range=Optional[str])

slots.experimental_replicates = Slot(uri=GHGA.experimental_replicates, name="experimental replicates", curie=GHGA.curie('experimental_replicates'),
                   model_uri=GHGA.experimental_replicates, domain=None, range=Optional[str])

slots.xref = Slot(uri=GHGA.xref, name="xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.xref, domain=None, range=Optional[Union[str, List[str]]])

slots.creation_date = Slot(uri=GHGA.creation_date, name="creation date", curie=GHGA.curie('creation_date'),
                   model_uri=GHGA.creation_date, domain=None, range=Optional[str])

slots.update_date = Slot(uri=GHGA.update_date, name="update date", curie=GHGA.curie('update_date'),
                   model_uri=GHGA.update_date, domain=None, range=Optional[str])

slots.url = Slot(uri=GHGA.url, name="url", curie=GHGA.curie('url'),
                   model_uri=GHGA.url, domain=None, range=Optional[str])

slots.has_attribute = Slot(uri=GHGA.has_attribute, name="has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.has_attribute, domain=None, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.description = Slot(uri=GHGA.description, name="description", curie=GHGA.curie('description'),
                   model_uri=GHGA.description, domain=None, range=Optional[str])

slots.has_study = Slot(uri=GHGA.has_study, name="has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.has_study, domain=None, range=Optional[Union[str, StudyId]])

slots.has_project = Slot(uri=GHGA.has_project, name="has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.has_project, domain=None, range=Optional[Union[str, ProjectId]])

slots.has_publication = Slot(uri=GHGA.has_publication, name="has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.has_publication, domain=None, range=Optional[Union[str, PublicationId]])

slots.has_sample = Slot(uri=GHGA.has_sample, name="has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.has_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.has_protocol = Slot(uri=GHGA.has_protocol, name="has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.has_protocol, domain=None, range=Optional[Union[str, ProtocolId]])

slots.has_experiment = Slot(uri=GHGA.has_experiment, name="has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.has_experiment, domain=None, range=Optional[Union[str, ExperimentId]])

slots.has_analysis = Slot(uri=GHGA.has_analysis, name="has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.has_analysis, domain=None, range=Optional[str])

slots.has_sequencing_protocol = Slot(uri=GHGA.has_sequencing_protocol, name="has sequencing protocol", curie=GHGA.curie('has_sequencing_protocol'),
                   model_uri=GHGA.has_sequencing_protocol, domain=None, range=Optional[str])

slots.has_library_preparation_protocol = Slot(uri=GHGA.has_library_preparation_protocol, name="has library preparation protocol", curie=GHGA.curie('has_library_preparation_protocol'),
                   model_uri=GHGA.has_library_preparation_protocol, domain=None, range=Optional[str])

slots.has_technology = Slot(uri=GHGA.has_technology, name="has technology", curie=GHGA.curie('has_technology'),
                   model_uri=GHGA.has_technology, domain=None, range=Optional[Union[str, TechnologyId]])

slots.has_experiment_process = Slot(uri=GHGA.has_experiment_process, name="has experiment process", curie=GHGA.curie('has_experiment_process'),
                   model_uri=GHGA.has_experiment_process, domain=None, range=Optional[Union[str, ExperimentProcessId]])

slots.has_analysis_process = Slot(uri=GHGA.has_analysis_process, name="has analysis process", curie=GHGA.curie('has_analysis_process'),
                   model_uri=GHGA.has_analysis_process, domain=None, range=Optional[Union[str, AnalysisProcessId]])

slots.has_file = Slot(uri=GHGA.has_file, name="has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.has_file, domain=None, range=Optional[Union[str, FileId]])

slots.has_input = Slot(uri=GHGA.has_input, name="has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.has_input, domain=None, range=Optional[Union[str, FileId]])

slots.has_output = Slot(uri=GHGA.has_output, name="has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.has_output, domain=None, range=Optional[Union[str, FileId]])

slots.has_agent = Slot(uri=GHGA.has_agent, name="has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.has_agent, domain=None, range=Optional[Union[str, AgentId]])

slots.has_workflow = Slot(uri=GHGA.has_workflow, name="has workflow", curie=GHGA.curie('has_workflow'),
                   model_uri=GHGA.has_workflow, domain=None, range=Optional[Union[str, WorkflowId]])

slots.has_workflow_step = Slot(uri=GHGA.has_workflow_step, name="has workflow step", curie=GHGA.curie('has_workflow_step'),
                   model_uri=GHGA.has_workflow_step, domain=None, range=Optional[Union[str, WorkflowStepId]])

slots.has_parameter = Slot(uri=GHGA.has_parameter, name="has parameter", curie=GHGA.curie('has_parameter'),
                   model_uri=GHGA.has_parameter, domain=None, range=Optional[Union[dict, WorkflowParameter]])

slots.has_dataset = Slot(uri=GHGA.has_dataset, name="has dataset", curie=GHGA.curie('has_dataset'),
                   model_uri=GHGA.has_dataset, domain=None, range=Optional[Union[str, DatasetId]])

slots.has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.has_biospecimen, domain=None, range=Optional[Union[str, BiospecimenId]])

slots.has_individual = Slot(uri=GHGA.has_individual, name="has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.has_individual, domain=None, range=Optional[Union[str, IndividualId]])

slots.has_anatomical_entity = Slot(uri=GHGA.has_anatomical_entity, name="has anatomical entity", curie=GHGA.curie('has_anatomical_entity'),
                   model_uri=GHGA.has_anatomical_entity, domain=None, range=Optional[Union[str, AnatomicalEntityId]])

slots.geographical_region = Slot(uri=GHGA.geographical_region, name="geographical region", curie=GHGA.curie('geographical_region'),
                   model_uri=GHGA.geographical_region, domain=None, range=Optional[str])

slots.has_disease = Slot(uri=GHGA.has_disease, name="has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.has_disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.has_phenotypic_feature, domain=None, range=Optional[Union[str, PhenotypicFeatureId]])

slots.has_parent = Slot(uri=GHGA.has_parent, name="has parent", curie=GHGA.curie('has_parent'),
                   model_uri=GHGA.has_parent, domain=None, range=Optional[str])

slots.has_children = Slot(uri=GHGA.has_children, name="has children", curie=GHGA.curie('has_children'),
                   model_uri=GHGA.has_children, domain=None, range=Optional[str])

slots.has_data_use_condition = Slot(uri=GHGA.has_data_use_condition, name="has data use condition", curie=GHGA.curie('has_data_use_condition'),
                   model_uri=GHGA.has_data_use_condition, domain=None, range=Optional[str])

slots.role = Slot(uri=GHGA.role, name="role", curie=GHGA.curie('role'),
                   model_uri=GHGA.role, domain=None, range=Optional[Union[str, "UserRoleEnum"]])

slots.has_proband = Slot(uri=GHGA.has_proband, name="has proband", curie=GHGA.curie('has_proband'),
                   model_uri=GHGA.has_proband, domain=None, range=Optional[Union[str, IndividualId]])

slots.permission = Slot(uri=GHGA.permission, name="permission", curie=GHGA.curie('permission'),
                   model_uri=GHGA.permission, domain=None, range=Optional[str])

slots.modifier = Slot(uri=GHGA.modifier, name="modifier", curie=GHGA.curie('modifier'),
                   model_uri=GHGA.modifier, domain=None, range=Optional[str])

slots.gender = Slot(uri=GHGA.gender, name="gender", curie=GHGA.curie('gender'),
                   model_uri=GHGA.gender, domain=None, range=Optional[str])

slots.sex = Slot(uri=GHGA.sex, name="sex", curie=GHGA.curie('sex'),
                   model_uri=GHGA.sex, domain=None, range=Optional[Union[str, "BiologicalSexEnum"]])

slots.age = Slot(uri=GHGA.age, name="age", curie=GHGA.curie('age'),
                   model_uri=GHGA.age, domain=None, range=Optional[int])

slots.tissue = Slot(uri=GHGA.tissue, name="tissue", curie=GHGA.curie('tissue'),
                   model_uri=GHGA.tissue, domain=None, range=Optional[str])

slots.isolation = Slot(uri=GHGA.isolation, name="isolation", curie=GHGA.curie('isolation'),
                   model_uri=GHGA.isolation, domain=None, range=Optional[str])

slots.storage = Slot(uri=GHGA.storage, name="storage", curie=GHGA.curie('storage'),
                   model_uri=GHGA.storage, domain=None, range=Optional[str])

slots.year_of_birth = Slot(uri=GHGA.year_of_birth, name="year of birth", curie=GHGA.curie('year_of_birth'),
                   model_uri=GHGA.year_of_birth, domain=None, range=Optional[str])

slots.vital_status = Slot(uri=GHGA.vital_status, name="vital status", curie=GHGA.curie('vital_status'),
                   model_uri=GHGA.vital_status, domain=None, range=Optional[Union[str, "VitalStatusEnum"]])

slots.ethnicity = Slot(uri=GHGA.ethnicity, name="ethnicity", curie=GHGA.curie('ethnicity'),
                   model_uri=GHGA.ethnicity, domain=None, range=Optional[str])

slots.ancestry = Slot(uri=GHGA.ancestry, name="ancestry", curie=GHGA.curie('ancestry'),
                   model_uri=GHGA.ancestry, domain=None, range=Optional[str])

slots.format = Slot(uri=GHGA.format, name="format", curie=GHGA.curie('format'),
                   model_uri=GHGA.format, domain=None, range=Optional[str])

slots.size = Slot(uri=GHGA.size, name="size", curie=GHGA.curie('size'),
                   model_uri=GHGA.size, domain=None, range=Optional[str])

slots.checksum = Slot(uri=GHGA.checksum, name="checksum", curie=GHGA.curie('checksum'),
                   model_uri=GHGA.checksum, domain=None, range=Optional[str])

slots.file_index = Slot(uri=GHGA.file_index, name="file index", curie=GHGA.curie('file_index'),
                   model_uri=GHGA.file_index, domain=None, range=Optional[str])

slots.category = Slot(uri=GHGA.category, name="category", curie=GHGA.curie('category'),
                   model_uri=GHGA.category, domain=None, range=Optional[str])

slots.has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.has_data_access_policy, domain=None, range=Optional[Union[str, DataAccessPolicyId]])

slots.policy_text = Slot(uri=GHGA.policy_text, name="policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.policy_text, domain=None, range=Optional[str])

slots.policy_url = Slot(uri=GHGA.policy_url, name="policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.policy_url, domain=None, range=Optional[str])

slots.has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.has_data_access_committee, domain=None, range=Optional[Union[str, DataAccessCommitteeId]])

slots.main_contact = Slot(uri=GHGA.main_contact, name="main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.main_contact, domain=None, range=Optional[Union[str, MemberId]])

slots.has_member = Slot(uri=GHGA.has_member, name="has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.has_member, domain=None, range=Optional[str])

slots.telephone = Slot(uri=GHGA.telephone, name="telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.telephone, domain=None, range=Optional[str])

slots.organization = Slot(uri=GHGA.organization, name="organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.organization, domain=None, range=Optional[str])

slots.email = Slot(uri=GHGA.email, name="email", curie=GHGA.curie('email'),
                   model_uri=GHGA.email, domain=None, range=Optional[str])

slots.key = Slot(uri=GHGA.key, name="key", curie=GHGA.curie('key'),
                   model_uri=GHGA.key, domain=None, range=Optional[str])

slots.key_type = Slot(uri=GHGA.key_type, name="key type", curie=GHGA.curie('key_type'),
                   model_uri=GHGA.key_type, domain=None, range=Optional[str])

slots.value = Slot(uri=GHGA.value, name="value", curie=GHGA.curie('value'),
                   model_uri=GHGA.value, domain=None, range=Optional[str])

slots.value_type = Slot(uri=GHGA.value_type, name="value type", curie=GHGA.curie('value_type'),
                   model_uri=GHGA.value_type, domain=None, range=Optional[str])

slots.affiliation = Slot(uri=GHGA.affiliation, name="affiliation", curie=GHGA.curie('affiliation'),
                   model_uri=GHGA.affiliation, domain=None, range=Optional[str])

slots.library_name = Slot(uri=GHGA.library_name, name="library name", curie=GHGA.curie('library_name'),
                   model_uri=GHGA.library_name, domain=None, range=Optional[str])

slots.library_layout = Slot(uri=GHGA.library_layout, name="library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.library_layout, domain=None, range=Optional[str])

slots.library_type = Slot(uri=GHGA.library_type, name="library type", curie=GHGA.curie('library_type'),
                   model_uri=GHGA.library_type, domain=None, range=Optional[str])

slots.library_selection = Slot(uri=GHGA.library_selection, name="library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.library_selection, domain=None, range=Optional[str])

slots.library_construction = Slot(uri=GHGA.library_construction, name="library construction", curie=GHGA.curie('library_construction'),
                   model_uri=GHGA.library_construction, domain=None, range=Optional[str])

slots.library_preparation = Slot(uri=GHGA.library_preparation, name="library preparation", curie=GHGA.curie('library_preparation'),
                   model_uri=GHGA.library_preparation, domain=None, range=Optional[str])

slots.library_level = Slot(uri=GHGA.library_level, name="library level", curie=GHGA.curie('library_level'),
                   model_uri=GHGA.library_level, domain=None, range=Optional[str])

slots.library_construction_kit_retail_name = Slot(uri=GHGA.library_construction_kit_retail_name, name="library construction kit retail name", curie=GHGA.curie('library_construction_kit_retail_name'),
                   model_uri=GHGA.library_construction_kit_retail_name, domain=None, range=Optional[str])

slots.library_construction_kit_manufacturer = Slot(uri=GHGA.library_construction_kit_manufacturer, name="library construction kit manufacturer", curie=GHGA.curie('library_construction_kit_manufacturer'),
                   model_uri=GHGA.library_construction_kit_manufacturer, domain=None, range=Optional[str])

slots.primer = Slot(uri=GHGA.primer, name="primer", curie=GHGA.curie('primer'),
                   model_uri=GHGA.primer, domain=None, range=Optional[str])

slots.end_bias = Slot(uri=GHGA.end_bias, name="end bias", curie=GHGA.curie('end_bias'),
                   model_uri=GHGA.end_bias, domain=None, range=Optional[str])

slots.target_regions = Slot(uri=GHGA.target_regions, name="target regions", curie=GHGA.curie('target_regions'),
                   model_uri=GHGA.target_regions, domain=None, range=Optional[str])

slots.rnaseq_strandedness = Slot(uri=GHGA.rnaseq_strandedness, name="rnaseq strandedness", curie=GHGA.curie('rnaseq_strandedness'),
                   model_uri=GHGA.rnaseq_strandedness, domain=None, range=Optional[str])

slots.sequencing_center = Slot(uri=GHGA.sequencing_center, name="sequencing center", curie=GHGA.curie('sequencing_center'),
                   model_uri=GHGA.sequencing_center, domain=None, range=Optional[str])

slots.instrument_model = Slot(uri=GHGA.instrument_model, name="instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.instrument_model, domain=None, range=Optional[str])

slots.read_length = Slot(uri=GHGA.read_length, name="read length", curie=GHGA.curie('read_length'),
                   model_uri=GHGA.read_length, domain=None, range=Optional[str])

slots.sequencing_length = Slot(uri=GHGA.sequencing_length, name="sequencing length", curie=GHGA.curie('sequencing_length'),
                   model_uri=GHGA.sequencing_length, domain=None, range=Optional[str])

slots.read_pair_number = Slot(uri=GHGA.read_pair_number, name="read pair number", curie=GHGA.curie('read_pair_number'),
                   model_uri=GHGA.read_pair_number, domain=None, range=Optional[str])

slots.reference_annotation = Slot(uri=GHGA.reference_annotation, name="reference annotation", curie=GHGA.curie('reference_annotation'),
                   model_uri=GHGA.reference_annotation, domain=None, range=Optional[str])

slots.lane_number = Slot(uri=GHGA.lane_number, name="lane number", curie=GHGA.curie('lane_number'),
                   model_uri=GHGA.lane_number, domain=None, range=Optional[str])

slots.target_coverage = Slot(uri=GHGA.target_coverage, name="target coverage", curie=GHGA.curie('target_coverage'),
                   model_uri=GHGA.target_coverage, domain=None, range=Optional[str])

slots.flow_cell_id = Slot(uri=GHGA.flow_cell_id, name="flow cell id", curie=GHGA.curie('flow_cell_id'),
                   model_uri=GHGA.flow_cell_id, domain=None, range=Optional[str])

slots.flow_cell_type = Slot(uri=GHGA.flow_cell_type, name="flow cell type", curie=GHGA.curie('flow_cell_type'),
                   model_uri=GHGA.flow_cell_type, domain=None, range=Optional[str])

slots.umi_barcode_read = Slot(uri=GHGA.umi_barcode_read, name="umi barcode read", curie=GHGA.curie('umi_barcode_read'),
                   model_uri=GHGA.umi_barcode_read, domain=None, range=Optional[str])

slots.umi_barcode_offset = Slot(uri=GHGA.umi_barcode_offset, name="umi barcode offset", curie=GHGA.curie('umi_barcode_offset'),
                   model_uri=GHGA.umi_barcode_offset, domain=None, range=Optional[str])

slots.umi_barcode_size = Slot(uri=GHGA.umi_barcode_size, name="umi barcode size", curie=GHGA.curie('umi_barcode_size'),
                   model_uri=GHGA.umi_barcode_size, domain=None, range=Optional[str])

slots.cell_barcode_read = Slot(uri=GHGA.cell_barcode_read, name="cell barcode read", curie=GHGA.curie('cell_barcode_read'),
                   model_uri=GHGA.cell_barcode_read, domain=None, range=Optional[str])

slots.cell_barcode_offset = Slot(uri=GHGA.cell_barcode_offset, name="cell barcode offset", curie=GHGA.curie('cell_barcode_offset'),
                   model_uri=GHGA.cell_barcode_offset, domain=None, range=Optional[str])

slots.cell_barcode_size = Slot(uri=GHGA.cell_barcode_size, name="cell barcode size", curie=GHGA.curie('cell_barcode_size'),
                   model_uri=GHGA.cell_barcode_size, domain=None, range=Optional[str])

slots.sample_barcode_read = Slot(uri=GHGA.sample_barcode_read, name="sample barcode read", curie=GHGA.curie('sample_barcode_read'),
                   model_uri=GHGA.sample_barcode_read, domain=None, range=Optional[str])

slots.vital_status_at_sampling = Slot(uri=GHGA.vital_status_at_sampling, name="vital status at sampling", curie=GHGA.curie('vital_status_at_sampling'),
                   model_uri=GHGA.vital_status_at_sampling, domain=None, range=Optional[str])

slots.submission_date = Slot(uri=GHGA.submission_date, name="submission date", curie=GHGA.curie('submission_date'),
                   model_uri=GHGA.submission_date, domain=None, range=Optional[str])

slots.release_date = Slot(uri=GHGA.release_date, name="release date", curie=GHGA.curie('release_date'),
                   model_uri=GHGA.release_date, domain=None, range=Optional[str])

slots.deprecation_date = Slot(uri=GHGA.deprecation_date, name="deprecation date", curie=GHGA.curie('deprecation_date'),
                   model_uri=GHGA.deprecation_date, domain=None, range=Optional[str])

slots.replaced_by = Slot(uri=GHGA.replaced_by, name="replaced by", curie=GHGA.curie('replaced_by'),
                   model_uri=GHGA.replaced_by, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.replaces = Slot(uri=GHGA.replaces, name="replaces", curie=GHGA.curie('replaces'),
                   model_uri=GHGA.replaces, domain=NamedThing, range=Optional[Union[str, NamedThingId]])

slots.status = Slot(uri=GHGA.status, name="status", curie=GHGA.curie('status'),
                   model_uri=GHGA.status, domain=None, range=Optional[Union[str, "StatusEnum"]])

slots.named_thing_id = Slot(uri=GHGA.id, name="named thing_id", curie=GHGA.curie('id'),
                   model_uri=GHGA.named_thing_id, domain=NamedThing, range=Union[str, NamedThingId])

slots.named_thing_xref = Slot(uri=GHGA.xref, name="named thing_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.named_thing_xref, domain=NamedThing, range=Optional[Union[str, List[str]]])

slots.named_thing_type = Slot(uri=GHGA.type, name="named thing_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.named_thing_type, domain=NamedThing, range=Optional[str])

slots.named_thing_creation_date = Slot(uri=GHGA.creation_date, name="named thing_creation date", curie=GHGA.curie('creation_date'),
                   model_uri=GHGA.named_thing_creation_date, domain=NamedThing, range=Optional[str])

slots.named_thing_update_date = Slot(uri=GHGA.update_date, name="named thing_update date", curie=GHGA.curie('update_date'),
                   model_uri=GHGA.named_thing_update_date, domain=NamedThing, range=Optional[str])

slots.attribute_key = Slot(uri=GHGA.key, name="attribute_key", curie=GHGA.curie('key'),
                   model_uri=GHGA.attribute_key, domain=Attribute, range=str)

slots.attribute_key_type = Slot(uri=GHGA.key_type, name="attribute_key type", curie=GHGA.curie('key_type'),
                   model_uri=GHGA.attribute_key_type, domain=Attribute, range=Optional[str])

slots.attribute_value = Slot(uri=GHGA.value, name="attribute_value", curie=GHGA.curie('value'),
                   model_uri=GHGA.attribute_value, domain=Attribute, range=str)

slots.attribute_value_type = Slot(uri=GHGA.value_type, name="attribute_value type", curie=GHGA.curie('value_type'),
                   model_uri=GHGA.attribute_value_type, domain=Attribute, range=Optional[str])

slots.project_title = Slot(uri=GHGA.title, name="project_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.project_title, domain=Project, range=str)

slots.project_description = Slot(uri=GHGA.description, name="project_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.project_description, domain=Project, range=str)

slots.project_has_publication = Slot(uri=GHGA.has_publication, name="project_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.project_has_publication, domain=Project, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.project_has_attribute = Slot(uri=GHGA.has_attribute, name="project_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.project_has_attribute, domain=Project, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.study_title = Slot(uri=GHGA.title, name="study_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.study_title, domain=Study, range=str)

slots.study_description = Slot(uri=GHGA.description, name="study_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.study_description, domain=Study, range=str)

slots.study_type = Slot(uri=GHGA.type, name="study_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.study_type, domain=Study, range=Union[str, "StudyTypeEnum"])

slots.study_affiliation = Slot(uri=GHGA.affiliation, name="study_affiliation", curie=GHGA.curie('affiliation'),
                   model_uri=GHGA.study_affiliation, domain=Study, range=Union[str, List[str]])

slots.study_has_publication = Slot(uri=GHGA.has_publication, name="study_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.study_has_publication, domain=Study, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.study_has_experiment = Slot(uri=GHGA.has_experiment, name="study_has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.study_has_experiment, domain=Study, range=Optional[Union[Dict[Union[str, ExperimentId], Union[dict, "Experiment"]], List[Union[dict, "Experiment"]]]])

slots.study_has_analysis = Slot(uri=GHGA.has_analysis, name="study_has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.study_has_analysis, domain=Study, range=Optional[Union[Dict[Union[str, AnalysisId], Union[dict, "Analysis"]], List[Union[dict, "Analysis"]]]])

slots.study_has_project = Slot(uri=GHGA.has_project, name="study_has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.study_has_project, domain=Study, range=Optional[Union[dict, Project]])

slots.study_has_attribute = Slot(uri=GHGA.has_attribute, name="study_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.study_has_attribute, domain=Study, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.study_status = Slot(uri=GHGA.status, name="study_status", curie=GHGA.curie('status'),
                   model_uri=GHGA.study_status, domain=Study, range=Optional[Union[str, "StatusEnum"]])

slots.experiment_title = Slot(uri=GHGA.title, name="experiment_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.experiment_title, domain=Experiment, range=str)

slots.experiment_description = Slot(uri=GHGA.description, name="experiment_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.experiment_description, domain=Experiment, range=str)

slots.experiment_biological_replicates = Slot(uri=GHGA.biological_replicates, name="experiment_biological replicates", curie=GHGA.curie('biological_replicates'),
                   model_uri=GHGA.experiment_biological_replicates, domain=Experiment, range=Optional[str])

slots.experiment_technical_replicates = Slot(uri=GHGA.technical_replicates, name="experiment_technical replicates", curie=GHGA.curie('technical_replicates'),
                   model_uri=GHGA.experiment_technical_replicates, domain=Experiment, range=Optional[str])

slots.experiment_experimental_replicates = Slot(uri=GHGA.experimental_replicates, name="experiment_experimental replicates", curie=GHGA.curie('experimental_replicates'),
                   model_uri=GHGA.experiment_experimental_replicates, domain=Experiment, range=Optional[str])

slots.experiment_has_study = Slot(uri=GHGA.has_study, name="experiment_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.experiment_has_study, domain=Experiment, range=Union[dict, Study])

slots.experiment_has_sample = Slot(uri=GHGA.has_sample, name="experiment_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.experiment_has_sample, domain=Experiment, range=Union[dict, "Sample"])

slots.experiment_has_technology = Slot(uri=GHGA.has_technology, name="experiment_has technology", curie=GHGA.curie('has_technology'),
                   model_uri=GHGA.experiment_has_technology, domain=Experiment, range=Optional[Union[dict, "Technology"]])

slots.experiment_has_file = Slot(uri=GHGA.has_file, name="experiment_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.experiment_has_file, domain=Experiment, range=Optional[Union[Dict[Union[str, FileId], Union[dict, "File"]], List[Union[dict, "File"]]]])

slots.experiment_has_experiment_process = Slot(uri=GHGA.has_experiment_process, name="experiment_has experiment process", curie=GHGA.curie('has_experiment_process'),
                   model_uri=GHGA.experiment_has_experiment_process, domain=Experiment, range=Optional[Union[Dict[Union[str, ExperimentProcessId], Union[dict, "ExperimentProcess"]], List[Union[dict, "ExperimentProcess"]]]])

slots.experiment_process_title = Slot(uri=GHGA.title, name="experiment process_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.experiment_process_title, domain=ExperimentProcess, range=Optional[str])

slots.experiment_process_has_input = Slot(uri=GHGA.has_input, name="experiment process_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.experiment_process_has_input, domain=ExperimentProcess, range=Optional[Union[dict, "Sample"]])

slots.experiment_process_has_protocol = Slot(uri=GHGA.has_protocol, name="experiment process_has protocol", curie=GHGA.curie('has_protocol'),
                   model_uri=GHGA.experiment_process_has_protocol, domain=ExperimentProcess, range=Optional[Union[dict, "Protocol"]])

slots.experiment_process_has_agent = Slot(uri=GHGA.has_agent, name="experiment process_has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.experiment_process_has_agent, domain=ExperimentProcess, range=Optional[Union[dict, "Agent"]])

slots.experiment_process_has_output = Slot(uri=GHGA.has_output, name="experiment process_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.experiment_process_has_output, domain=ExperimentProcess, range=Optional[Union[dict, "File"]])

slots.protocol_name = Slot(uri=GHGA.name, name="protocol_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.protocol_name, domain=Protocol, range=Optional[str])

slots.protocol_type = Slot(uri=GHGA.type, name="protocol_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.protocol_type, domain=Protocol, range=Optional[str])

slots.protocol_description = Slot(uri=GHGA.description, name="protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.protocol_description, domain=Protocol, range=Optional[str])

slots.protocol_url = Slot(uri=GHGA.url, name="protocol_url", curie=GHGA.curie('url'),
                   model_uri=GHGA.protocol_url, domain=Protocol, range=Optional[str])

slots.protocol_xref = Slot(uri=GHGA.xref, name="protocol_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.protocol_xref, domain=Protocol, range=Optional[Union[str, List[str]]])

slots.protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.protocol_has_attribute, domain=Protocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.library_preparation_protocol_name = Slot(uri=GHGA.name, name="library preparation protocol_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.library_preparation_protocol_name, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_description = Slot(uri=GHGA.description, name="library preparation protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.library_preparation_protocol_description, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_name = Slot(uri=GHGA.library_name, name="library preparation protocol_library name", curie=GHGA.curie('library_name'),
                   model_uri=GHGA.library_preparation_protocol_library_name, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_layout = Slot(uri=GHGA.library_layout, name="library preparation protocol_library layout", curie=GHGA.curie('library_layout'),
                   model_uri=GHGA.library_preparation_protocol_library_layout, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_type = Slot(uri=GHGA.library_type, name="library preparation protocol_library type", curie=GHGA.curie('library_type'),
                   model_uri=GHGA.library_preparation_protocol_library_type, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_selection = Slot(uri=GHGA.library_selection, name="library preparation protocol_library selection", curie=GHGA.curie('library_selection'),
                   model_uri=GHGA.library_preparation_protocol_library_selection, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_construction = Slot(uri=GHGA.library_construction, name="library preparation protocol_library construction", curie=GHGA.curie('library_construction'),
                   model_uri=GHGA.library_preparation_protocol_library_construction, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_preparation = Slot(uri=GHGA.library_preparation, name="library preparation protocol_library preparation", curie=GHGA.curie('library_preparation'),
                   model_uri=GHGA.library_preparation_protocol_library_preparation, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_construction_kit_retail_name = Slot(uri=GHGA.library_construction_kit_retail_name, name="library preparation protocol_library construction kit retail name", curie=GHGA.curie('library_construction_kit_retail_name'),
                   model_uri=GHGA.library_preparation_protocol_library_construction_kit_retail_name, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_library_construction_kit_manufacturer = Slot(uri=GHGA.library_construction_kit_manufacturer, name="library preparation protocol_library construction kit manufacturer", curie=GHGA.curie('library_construction_kit_manufacturer'),
                   model_uri=GHGA.library_preparation_protocol_library_construction_kit_manufacturer, domain=LibraryPreparationProtocol, range=str)

slots.library_preparation_protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="library preparation protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.library_preparation_protocol_has_attribute, domain=LibraryPreparationProtocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.sequencing_protocol_sequencing_center = Slot(uri=GHGA.sequencing_center, name="sequencing protocol_sequencing center", curie=GHGA.curie('sequencing_center'),
                   model_uri=GHGA.sequencing_protocol_sequencing_center, domain=SequencingProtocol, range=str)

slots.sequencing_protocol_instrument_model = Slot(uri=GHGA.instrument_model, name="sequencing protocol_instrument model", curie=GHGA.curie('instrument_model'),
                   model_uri=GHGA.sequencing_protocol_instrument_model, domain=SequencingProtocol, range=str)

slots.sequencing_protocol_name = Slot(uri=GHGA.name, name="sequencing protocol_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.sequencing_protocol_name, domain=SequencingProtocol, range=Optional[str])

slots.sequencing_protocol_description = Slot(uri=GHGA.description, name="sequencing protocol_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.sequencing_protocol_description, domain=SequencingProtocol, range=Optional[str])

slots.sequencing_protocol_has_attribute = Slot(uri=GHGA.has_attribute, name="sequencing protocol_has attribute", curie=GHGA.curie('has_attribute'),
                   model_uri=GHGA.sequencing_protocol_has_attribute, domain=SequencingProtocol, range=Optional[Union[Union[dict, Attribute], List[Union[dict, Attribute]]]])

slots.workflow_step_has_parameter = Slot(uri=GHGA.has_parameter, name="workflow step_has parameter", curie=GHGA.curie('has_parameter'),
                   model_uri=GHGA.workflow_step_has_parameter, domain=WorkflowStep, range=Optional[Union[Union[dict, "WorkflowParameter"], List[Union[dict, "WorkflowParameter"]]]])

slots.workflow_parameter_key = Slot(uri=GHGA.key, name="workflow parameter_key", curie=GHGA.curie('key'),
                   model_uri=GHGA.workflow_parameter_key, domain=WorkflowParameter, range=Optional[str])

slots.workflow_parameter_value = Slot(uri=GHGA.value, name="workflow parameter_value", curie=GHGA.curie('value'),
                   model_uri=GHGA.workflow_parameter_value, domain=WorkflowParameter, range=Optional[str])

slots.biospecimen_has_individual = Slot(uri=GHGA.has_individual, name="biospecimen_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.biospecimen_has_individual, domain=Biospecimen, range=Optional[Union[dict, "Individual"]])

slots.biospecimen_has_anatomical_entity = Slot(uri=GHGA.has_anatomical_entity, name="biospecimen_has anatomical entity", curie=GHGA.curie('has_anatomical_entity'),
                   model_uri=GHGA.biospecimen_has_anatomical_entity, domain=Biospecimen, range=Optional[Union[dict, "AnatomicalEntity"]])

slots.biospecimen_has_disease = Slot(uri=GHGA.has_disease, name="biospecimen_has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.biospecimen_has_disease, domain=Biospecimen, range=Optional[Union[Dict[Union[str, DiseaseId], Union[dict, "Disease"]], List[Union[dict, "Disease"]]]])

slots.biospecimen_has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="biospecimen_has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.biospecimen_has_phenotypic_feature, domain=Biospecimen, range=Optional[Union[Dict[Union[str, PhenotypicFeatureId], Union[dict, "PhenotypicFeature"]], List[Union[dict, "PhenotypicFeature"]]]])

slots.sample_name = Slot(uri=GHGA.name, name="sample_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.sample_name, domain=Sample, range=str)

slots.sample_type = Slot(uri=GHGA.type, name="sample_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.sample_type, domain=Sample, range=Optional[Union[str, "CaseControlEnum"]])

slots.sample_description = Slot(uri=GHGA.description, name="sample_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.sample_description, domain=Sample, range=str)

slots.sample_tissue = Slot(uri=GHGA.tissue, name="sample_tissue", curie=GHGA.curie('tissue'),
                   model_uri=GHGA.sample_tissue, domain=Sample, range=str)

slots.sample_has_individual = Slot(uri=GHGA.has_individual, name="sample_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.sample_has_individual, domain=Sample, range=Union[dict, "Individual"])

slots.sample_xref = Slot(uri=GHGA.xref, name="sample_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.sample_xref, domain=Sample, range=Optional[Union[str, List[str]]])

slots.sample_has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="sample_has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.sample_has_biospecimen, domain=Sample, range=Optional[Union[dict, Biospecimen]])

slots.individual_sex = Slot(uri=GHGA.sex, name="individual_sex", curie=GHGA.curie('sex'),
                   model_uri=GHGA.individual_sex, domain=Individual, range=Union[str, "BiologicalSexEnum"])

slots.individual_age = Slot(uri=GHGA.age, name="individual_age", curie=GHGA.curie('age'),
                   model_uri=GHGA.individual_age, domain=Individual, range=int)

slots.individual_vital_status = Slot(uri=GHGA.vital_status, name="individual_vital status", curie=GHGA.curie('vital_status'),
                   model_uri=GHGA.individual_vital_status, domain=Individual, range=Union[str, "VitalStatusEnum"])

slots.individual_has_parent = Slot(uri=GHGA.has_parent, name="individual_has parent", curie=GHGA.curie('has_parent'),
                   model_uri=GHGA.individual_has_parent, domain=Individual, range=Optional[Union[Dict[Union[str, IndividualId], Union[dict, "Individual"]], List[Union[dict, "Individual"]]]])

slots.individual_has_children = Slot(uri=GHGA.has_children, name="individual_has children", curie=GHGA.curie('has_children'),
                   model_uri=GHGA.individual_has_children, domain=Individual, range=Optional[Union[Dict[Union[str, IndividualId], Union[dict, "Individual"]], List[Union[dict, "Individual"]]]])

slots.individual_has_disease = Slot(uri=GHGA.has_disease, name="individual_has disease", curie=GHGA.curie('has_disease'),
                   model_uri=GHGA.individual_has_disease, domain=Individual, range=Optional[Union[Dict[Union[str, DiseaseId], Union[dict, "Disease"]], List[Union[dict, "Disease"]]]])

slots.individual_has_phenotypic_feature = Slot(uri=GHGA.has_phenotypic_feature, name="individual_has phenotypic feature", curie=GHGA.curie('has_phenotypic_feature'),
                   model_uri=GHGA.individual_has_phenotypic_feature, domain=Individual, range=Optional[Union[Dict[Union[str, PhenotypicFeatureId], Union[dict, "PhenotypicFeature"]], List[Union[dict, "PhenotypicFeature"]]]])

slots.family_has_member = Slot(uri=GHGA.has_member, name="family_has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.family_has_member, domain=Family, range=Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]])

slots.family_has_proband = Slot(uri=GHGA.has_proband, name="family_has proband", curie=GHGA.curie('has_proband'),
                   model_uri=GHGA.family_has_proband, domain=Family, range=Optional[Union[dict, Individual]])

slots.cohort_has_member = Slot(uri=GHGA.has_member, name="cohort_has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.cohort_has_member, domain=Cohort, range=Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]])

slots.file_name = Slot(uri=GHGA.name, name="file_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.file_name, domain=File, range=str)

slots.file_type = Slot(uri=GHGA.type, name="file_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.file_type, domain=File, range=Optional[Union[str, "FileTypeEnum"]])

slots.analysis_has_input = Slot(uri=GHGA.has_input, name="analysis_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.analysis_has_input, domain=Analysis, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.analysis_has_study = Slot(uri=GHGA.has_study, name="analysis_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.analysis_has_study, domain=Analysis, range=Optional[Union[dict, Study]])

slots.analysis_has_workflow = Slot(uri=GHGA.has_workflow, name="analysis_has workflow", curie=GHGA.curie('has_workflow'),
                   model_uri=GHGA.analysis_has_workflow, domain=Analysis, range=Optional[Union[dict, Workflow]])

slots.analysis_has_analysis_process = Slot(uri=GHGA.has_analysis_process, name="analysis_has analysis process", curie=GHGA.curie('has_analysis_process'),
                   model_uri=GHGA.analysis_has_analysis_process, domain=Analysis, range=Optional[Union[Dict[Union[str, AnalysisProcessId], Union[dict, "AnalysisProcess"]], List[Union[dict, "AnalysisProcess"]]]])

slots.analysis_has_output = Slot(uri=GHGA.has_output, name="analysis_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.analysis_has_output, domain=Analysis, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.analysis_process_has_input = Slot(uri=GHGA.has_input, name="analysis process_has input", curie=GHGA.curie('has_input'),
                   model_uri=GHGA.analysis_process_has_input, domain=AnalysisProcess, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.analysis_process_has_workflow_step = Slot(uri=GHGA.has_workflow_step, name="analysis process_has workflow step", curie=GHGA.curie('has_workflow_step'),
                   model_uri=GHGA.analysis_process_has_workflow_step, domain=AnalysisProcess, range=Optional[Union[dict, WorkflowStep]])

slots.analysis_process_has_agent = Slot(uri=GHGA.has_agent, name="analysis process_has agent", curie=GHGA.curie('has_agent'),
                   model_uri=GHGA.analysis_process_has_agent, domain=AnalysisProcess, range=Optional[Union[dict, Agent]])

slots.analysis_process_has_output = Slot(uri=GHGA.has_output, name="analysis process_has output", curie=GHGA.curie('has_output'),
                   model_uri=GHGA.analysis_process_has_output, domain=AnalysisProcess, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.dataset_title = Slot(uri=GHGA.title, name="dataset_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.dataset_title, domain=Dataset, range=str)

slots.dataset_description = Slot(uri=GHGA.description, name="dataset_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.dataset_description, domain=Dataset, range=str)

slots.dataset_type = Slot(uri=GHGA.type, name="dataset_type", curie=GHGA.curie('type'),
                   model_uri=GHGA.dataset_type, domain=Dataset, range=str)

slots.dataset_has_study = Slot(uri=GHGA.has_study, name="dataset_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.dataset_has_study, domain=Dataset, range=Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]])

slots.dataset_has_experiment = Slot(uri=GHGA.has_experiment, name="dataset_has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.dataset_has_experiment, domain=Dataset, range=Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]])

slots.dataset_has_sample = Slot(uri=GHGA.has_sample, name="dataset_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.dataset_has_sample, domain=Dataset, range=Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]])

slots.dataset_has_analysis = Slot(uri=GHGA.has_analysis, name="dataset_has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.dataset_has_analysis, domain=Dataset, range=Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]])

slots.dataset_has_file = Slot(uri=GHGA.has_file, name="dataset_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.dataset_has_file, domain=Dataset, range=Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]])

slots.dataset_has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="dataset_has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.dataset_has_data_access_policy, domain=Dataset, range=Union[Dict[Union[str, DataAccessPolicyId], Union[dict, "DataAccessPolicy"]], List[Union[dict, "DataAccessPolicy"]]])

slots.dataset_has_publication = Slot(uri=GHGA.has_publication, name="dataset_has publication", curie=GHGA.curie('has_publication'),
                   model_uri=GHGA.dataset_has_publication, domain=Dataset, range=Optional[Union[Dict[Union[str, PublicationId], Union[dict, "Publication"]], List[Union[dict, "Publication"]]]])

slots.data_use_condition_permission = Slot(uri=GHGA.permission, name="data use condition_permission", curie=GHGA.curie('permission'),
                   model_uri=GHGA.data_use_condition_permission, domain=DataUseCondition, range=Optional[str])

slots.data_use_condition_modifier = Slot(uri=GHGA.modifier, name="data use condition_modifier", curie=GHGA.curie('modifier'),
                   model_uri=GHGA.data_use_condition_modifier, domain=DataUseCondition, range=Optional[str])

slots.data_access_policy_description = Slot(uri=GHGA.description, name="data access policy_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.data_access_policy_description, domain=DataAccessPolicy, range=str)

slots.data_access_policy_policy_text = Slot(uri=GHGA.policy_text, name="data access policy_policy text", curie=GHGA.curie('policy_text'),
                   model_uri=GHGA.data_access_policy_policy_text, domain=DataAccessPolicy, range=str)

slots.data_access_policy_policy_url = Slot(uri=GHGA.policy_url, name="data access policy_policy url", curie=GHGA.curie('policy_url'),
                   model_uri=GHGA.data_access_policy_policy_url, domain=DataAccessPolicy, range=Optional[str])

slots.data_access_policy_has_data_access_committee = Slot(uri=GHGA.has_data_access_committee, name="data access policy_has data access committee", curie=GHGA.curie('has_data_access_committee'),
                   model_uri=GHGA.data_access_policy_has_data_access_committee, domain=DataAccessPolicy, range=Union[dict, "DataAccessCommittee"])

slots.data_access_policy_has_data_use_condition = Slot(uri=GHGA.has_data_use_condition, name="data access policy_has data use condition", curie=GHGA.curie('has_data_use_condition'),
                   model_uri=GHGA.data_access_policy_has_data_use_condition, domain=DataAccessPolicy, range=Optional[Union[Union[dict, DataUseCondition], List[Union[dict, DataUseCondition]]]])

slots.data_access_committee_name = Slot(uri=GHGA.name, name="data access committee_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.data_access_committee_name, domain=DataAccessCommittee, range=str)

slots.data_access_committee_main_contact = Slot(uri=GHGA.main_contact, name="data access committee_main contact", curie=GHGA.curie('main_contact'),
                   model_uri=GHGA.data_access_committee_main_contact, domain=DataAccessCommittee, range=Optional[Union[str, MemberId]])

slots.data_access_committee_has_member = Slot(uri=GHGA.has_member, name="data access committee_has member", curie=GHGA.curie('has_member'),
                   model_uri=GHGA.data_access_committee_has_member, domain=DataAccessCommittee, range=Optional[Union[Dict[Union[str, MemberId], Union[dict, "Member"]], List[Union[dict, "Member"]]]])

slots.member_email = Slot(uri=GHGA.email, name="member_email", curie=GHGA.curie('email'),
                   model_uri=GHGA.member_email, domain=Member, range=str)

slots.member_telephone = Slot(uri=GHGA.telephone, name="member_telephone", curie=GHGA.curie('telephone'),
                   model_uri=GHGA.member_telephone, domain=Member, range=str)

slots.member_organization = Slot(uri=GHGA.organization, name="member_organization", curie=GHGA.curie('organization'),
                   model_uri=GHGA.member_organization, domain=Member, range=str)

slots.publication_id = Slot(uri=GHGA.id, name="publication_id", curie=GHGA.curie('id'),
                   model_uri=GHGA.publication_id, domain=Publication, range=Union[str, PublicationId])

slots.publication_title = Slot(uri=GHGA.title, name="publication_title", curie=GHGA.curie('title'),
                   model_uri=GHGA.publication_title, domain=Publication, range=Optional[str])

slots.publication_xref = Slot(uri=GHGA.xref, name="publication_xref", curie=GHGA.curie('xref'),
                   model_uri=GHGA.publication_xref, domain=Publication, range=Optional[Union[str, List[str]]])

slots.user_role = Slot(uri=GHGA.role, name="user_role", curie=GHGA.curie('role'),
                   model_uri=GHGA.user_role, domain=User, range=Optional[Union[str, "UserRoleEnum"]])

slots.submission_id = Slot(uri=GHGA.id, name="submission_id", curie=GHGA.curie('id'),
                   model_uri=GHGA.submission_id, domain=Submission, range=Union[str, SubmissionId])

slots.submission_has_study = Slot(uri=GHGA.has_study, name="submission_has study", curie=GHGA.curie('has_study'),
                   model_uri=GHGA.submission_has_study, domain=Submission, range=Optional[Union[dict, Study]])

slots.submission_has_project = Slot(uri=GHGA.has_project, name="submission_has project", curie=GHGA.curie('has_project'),
                   model_uri=GHGA.submission_has_project, domain=Submission, range=Optional[Union[dict, Project]])

slots.submission_has_sample = Slot(uri=GHGA.has_sample, name="submission_has sample", curie=GHGA.curie('has_sample'),
                   model_uri=GHGA.submission_has_sample, domain=Submission, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.submission_has_biospecimen = Slot(uri=GHGA.has_biospecimen, name="submission_has biospecimen", curie=GHGA.curie('has_biospecimen'),
                   model_uri=GHGA.submission_has_biospecimen, domain=Submission, range=Optional[Union[Dict[Union[str, BiospecimenId], Union[dict, Biospecimen]], List[Union[dict, Biospecimen]]]])

slots.submission_has_individual = Slot(uri=GHGA.has_individual, name="submission_has individual", curie=GHGA.curie('has_individual'),
                   model_uri=GHGA.submission_has_individual, domain=Submission, range=Optional[Union[Dict[Union[str, IndividualId], Union[dict, Individual]], List[Union[dict, Individual]]]])

slots.submission_has_experiment = Slot(uri=GHGA.has_experiment, name="submission_has experiment", curie=GHGA.curie('has_experiment'),
                   model_uri=GHGA.submission_has_experiment, domain=Submission, range=Optional[Union[Dict[Union[str, ExperimentId], Union[dict, Experiment]], List[Union[dict, Experiment]]]])

slots.submission_has_analysis = Slot(uri=GHGA.has_analysis, name="submission_has analysis", curie=GHGA.curie('has_analysis'),
                   model_uri=GHGA.submission_has_analysis, domain=Submission, range=Optional[Union[Dict[Union[str, AnalysisId], Union[dict, Analysis]], List[Union[dict, Analysis]]]])

slots.submission_has_file = Slot(uri=GHGA.has_file, name="submission_has file", curie=GHGA.curie('has_file'),
                   model_uri=GHGA.submission_has_file, domain=Submission, range=Optional[Union[Dict[Union[str, FileId], Union[dict, File]], List[Union[dict, File]]]])

slots.submission_has_data_access_policy = Slot(uri=GHGA.has_data_access_policy, name="submission_has data access policy", curie=GHGA.curie('has_data_access_policy'),
                   model_uri=GHGA.submission_has_data_access_policy, domain=Submission, range=Optional[Union[dict, DataAccessPolicy]])

slots.submission_creation_date = Slot(uri=GHGA.creation_date, name="submission_creation date", curie=GHGA.curie('creation_date'),
                   model_uri=GHGA.submission_creation_date, domain=Submission, range=Optional[str])

slots.submission_update_date = Slot(uri=GHGA.update_date, name="submission_update date", curie=GHGA.curie('update_date'),
                   model_uri=GHGA.submission_update_date, domain=Submission, range=Optional[str])

slots.submission_status = Slot(uri=GHGA.status, name="submission_status", curie=GHGA.curie('status'),
                   model_uri=GHGA.submission_status, domain=Submission, range=Optional[Union[str, "StatusEnum"]])

slots.ontology_class_mixin_id = Slot(uri=GHGA.id, name="ontology class mixin_id", curie=GHGA.curie('id'),
                   model_uri=GHGA.ontology_class_mixin_id, domain=OntologyClassMixin, range=Union[str, OntologyClassMixinId])

slots.ontology_class_mixin_name = Slot(uri=GHGA.name, name="ontology class mixin_name", curie=GHGA.curie('name'),
                   model_uri=GHGA.ontology_class_mixin_name, domain=OntologyClassMixin, range=Optional[str])

slots.ontology_class_mixin_description = Slot(uri=GHGA.description, name="ontology class mixin_description", curie=GHGA.curie('description'),
                   model_uri=GHGA.ontology_class_mixin_description, domain=OntologyClassMixin, range=Optional[str])
