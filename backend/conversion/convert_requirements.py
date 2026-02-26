from typing import List

from ai_gen.models.requirements import FunctionalRequirement as FR_pydantic, NonFunctionalRequirement as NFR_pydantic, BusinessRules as BR_pydantic
from ai_gen.response_model.requirement_response import FROutput, NFROutput, BROutput

from rex.models.requirements import FunctionalRequirement as FR_django, NonFunctionalRequirement as NFR_django, BusinessRules as BR_django

class FR_converter():
  def save_fr(fr_list: FROutput):
    for fr in fr_list.fr_list:
      FR_django.objects.create(
        description = fr.description,
        testCase = fr.testCase,
        epics = fr.epics
      )

  def load_fr(fr_list: List[FR_django]) -> FROutput:
    out = FROutput([])
    
    for fr in fr_list:
      fr_pyd = FR_pydantic()
      fr_pyd.iD = fr.iD
      fr_pyd.description = fr.description
      fr_pyd.testCase = fr.testCase
      fr_pyd.epics = fr.epics

      out.fr_list.append(fr_pyd)
    
    return out
  
class NFR_converter():
  def save_nfr(nfr_list: NFROutput):
    for nfr in nfr_list.nfr_list:
      NFR_django.objects.create(
        description = nfr.description,
        frs = nfr.frs
      )

  def load_nfr(nfr_list: List[NFR_django]) -> NFROutput:
    out = NFROutput([])
    
    for nfr in nfr_list:
      nfr_pyd = NFR_pydantic()
      nfr_pyd.iD = nfr.iD
      nfr_pyd.description = nfr.description
      nfr_pyd.frs = nfr.frs

      out.fr_list.append(nfr_pyd)
    
    return out
  
class BR_converter():
  def save_br(br_list: BROutput):
    for br in br_list.br_list:
      BR_django.objects.create(
        description = br.description,
        frs = br.frs
      )

  def load_br(br_list: List[BR_django]) -> BROutput:
    out = BROutput([])
    
    for br in br_list:
      br_pyd = BR_pydantic()
      br_pyd.iD = br.iD
      br_pyd.description = br.description
      br_pyd.frs = br.frs

      out.br_list.append(br_pyd)
    
    return out