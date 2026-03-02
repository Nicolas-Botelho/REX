from typing import List

from ai_gen.models.test_case import TestCase as TC_pydantic
from ai_gen.response_model.test_case_response import TCOutput

from rex.models.testcase import TestCase as TC_django

class TC_converter():
  def save_tc(tc_list: TCOutput):
    for tc in tc_list.tc_list:
      try:
        TC_django.objects.update(
          iD = tc.iD,
          description = tc.description
        )
  
      except(Exception):
        TC_django.objects.create(
          description = tc.description
        )

  def load_tc(tc_list : List[TC_django]) -> TCOutput:
    out = TCOutput([])

    for tc in tc_list:
      tc_pyd = TC_pydantic()
      tc_pyd.iD = tc.iD
      tc_pyd.description = tc.description

      out.tc_list.append(tc_pyd)

    return out