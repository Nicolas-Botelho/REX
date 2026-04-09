import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer

from utils.crud_alias import get

def attrgen(cls_dict: dict):
  enums_str, linked_enums = write_enum_attr(cls_dict)
  string = write_prim_attr(cls_dict) + "\n\n"+ enums_str

  return string, linked_enums

def write_prim_attr(cls_dict: dict):
  string = ""
  try:
    caps = cls_dict['class_primitive_attrs']

    if type(caps) == list:
      for cap in caps:
        string += f"{cap["name"]} : {cap["attr_type"]}\n\n"
    # elif type(caps) == dict:
    #   string += f"{caps["name"]} : {caps["attr_type"]}\n\n"
  except:
    pass

  return string

def write_enum_attr(cls_dict: dict):
  string = ""
  linked_enums = []

  try:
    caes = cls_dict["class_enum_attrs"]

    if type(caes) == list:
      for cae in caes:
        string += f"{cae["name"]} : {cae["enum"]["name"]}\n\n"
        linked_enums.append((cae["enum"]["id"], cae["enum"]["name"]))
    # elif type(caes) == dict:
    #   string += f"{caes["name"]} : {caes["enum"]["name"]}\n\n"
    #   linked_enums.append((caes["enum"]["id"], caes["enum"]["name"]))
  except:
    pass
  return string, linked_enums

def relgen(cls_dict: dict):
  string = ""
  linked_clss = []

  try:
    rels = cls_dict["class_relations"]

    if type(rels) == list:
      for rel in rels:
        rel_str, linked_cls = write_relation(rel, cls_dict["name"])
        linked_clss.append(linked_cls)
        string += rel_str
  except:
    pass

  return string, linked_clss

def write_relation(rel: dict, cls_name: str):

  rcr_as_srcs = rel["rcr_as_srcs"]
  rcr_as_tgts = rel["rcr_as_tgts"]
  string = ""

  if len(rcr_as_srcs) > 0:
    tgt_rel = get("classes", "relation_class_reference", rcr_as_srcs[0]["tgt"])
    tgt_cls = get("classes", "class", tgt_rel["ref_class"])
    linked_cls = (tgt_cls["id"], tgt_cls["name"])

    string += f"{cls_name} \"{rel["minim"] if rel["minim"]!= None else 'N'}..{rel["maxim"] if rel["maxim"]!= None else 'N'}\" --> \"{tgt_rel["minim"] if tgt_rel["minim"]!= None else 'N'}..{tgt_rel["maxim"] if tgt_rel["maxim"]!= None else 'N'}\" {tgt_cls["name"]}\n\n"

  if len(rcr_as_tgts) > 0:
    src_rel = get("classes", "relation_class_reference", rcr_as_tgts[0]["src"])
    src_cls = get("classes", "class", src_rel["ref_class"])
    linked_cls = (src_cls["id"], src_cls["name"])

    string += f"{src_cls["name"]} \"{src_rel["minim"] if src_rel["minim"]!= None else 'N'}..{src_rel["maxim"] if src_rel["maxim"] != None else 'N'}\" --> \"{rel["minim"] if rel["minim"] != None else 'N'}..{rel["maxim"] if rel["maxim"] != None else 'N'}\" {cls_name}\n\n"

  return string, linked_cls

page_config()

header()

sidebar()

desc_cls = get("classes", "class", int(st.query_params.id))

attrs_str, linked_enums = attrgen(desc_cls)
rel_str, linked_clss = relgen(desc_cls)

st.markdown(
f"""
## {desc_cls.get("name")}

### Attributes
{attrs_str}

### Relations
{rel_str}
""")

if linked_clss:
  st.markdown("""
  ### Linked Classes
  """)
  for linked_cls_id, linked_cls_name in linked_clss:
    st.page_link(page="./pages/class_desc_page.py", label=f"{linked_cls_name}", query_params={"id" : linked_cls_id})

if linked_enums:
  st.markdown("""
  ### Linked Enums
  """)
  for linked_enum_id, linked_enum_name in linked_enums:
    st.page_link(page="./app.py", label=f"{linked_enum_name}", query_params={"id" : linked_enum_id})

footer()