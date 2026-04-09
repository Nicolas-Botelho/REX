import streamlit as st

from components.page_config import page_config
from components.header import header
from components.sidebar import sidebar
from components.footer import footer
from utils.crud_alias import create

page_config()

header()

sidebar()

st.title("New Class")

# Class
name = st.text_input("Class Name")

# Primitive Attributes
prim_attrs = st.session_state.get("prim_attrs")
# print(st.session_state)

for _ in prim_attrs:
  st.markdown(f"{_.get("name")}: {_.get("attr_type")}\n")

prim_attr_name = st.text_input("Primitive Attribute Name")
prim_attr_type = st.selectbox("Primitive Attribute Type", ['string', 'integer', 'boolean', 'float'])

add_prim_type_attr_button = st.button("Add Primitive Type Attribute", )
if add_prim_type_attr_button:
  st.session_state.get("prim_attrs").append({"name": prim_attr_name, "attr_type": prim_attr_type})
  add_prim_type_attr_button = False


# Enum Attributes
enum_attrs = []

for _ in enum_attrs:
  st.markdown(f"- {_.get("name")}\n")

enum_attr_name = st.text_input("Enum Attribute Name")

enums = []
enum_map = {}
for enum in st.session_state.get("enums"):
  e_name = enum.get("name")
  e_id = enum.get("ref_id")
  enums.append()
  enum_map[e_name] = e_id

enum_attr_type = st.selectbox("Enum Attribute Type", enums)
enum_attr_type_id = enum_map.get("enum_attr_type")

new_enum_button = st.button("New Enum")
if new_enum_button:
  enum_name = st.text_input("Enum Name")
  enum_values = []
  for value in enum_values:
    st.markdown(f"- {value}\n")
  new_enum_value_button = st.button("New Enum Value")
  if new_enum_value_button:
    enum_value = st.text_input("Enum Value")
    add_enum_value = st.button("Add Enum Value")
    if add_enum_value:
      enum_values.append(enum_value)
      add_enum_value = False

  add_enum_button = st.button("Add Enum")
  if add_enum_button:
    new_enum = create("classes", "enum", {"name": enum_name})
    for enum_value in enum_values:
      create("classes", "enum_attribute", {"value": enum_value, "enum": new_enum.get("ref_id")})
    new_enum_button = False
    add_enum_button = False

add_enum_type_attr_button = st.button("Add Enum Type Attribute")
if add_enum_type_attr_button:
  enum_attrs.append({"name": enum_attr_name, "attr_type": enum_attr_type_id})
  add_enum_type_attr_button = False

# Relations
# rcrs = []
rels = []

# for _ in rels:
  # st.markdown(f"{_.get("name")}\n")

classes = []
class_map = {}
cardinalities = [0, 1, "N"]
for klass in st.session_state.get("classes"):
  k_name = klass.get("name")
  k_id = klass.get("ref_id")
  classes.append()
  class_map[k_name] = k_id

other_class = st.selectbox("The Other Class of the Relation", classes)
is_src = st.toggle("The Created Class is the Source of the Relation?")
src_min_car = st.selectbox("Source Min Cardinality of the Relation", cardinalities)
src_max_car = st.selectbox("Source Max Cardinality of the Relation", cardinalities)
tgt_min_car = st.selectbox("Target Min Cardinality of the Relation", cardinalities)
tgt_max_car = st.selectbox("Target Max Cardinality of the Relation", cardinalities)

add_relation_button = st.button("Add Relation")
if add_relation_button:
  pair = (
    {"min": src_min_car, "max": src_max_car},
    {"min": tgt_min_car, "max": tgt_max_car}
  )
  if is_src:
    pair[1]["ref_class"] = class_map[other_class]
  else:
    pair[0]["ref_class"] = class_map[other_class]
    aux = pair[0]
    pair[0] = pair[1]
    pair[1] = pair[0]
  rels.append(pair)
  add_relation_button = False

add_class_button = st.button("Add Class")
if add_class_button:
  new_class = create("classes", "class", {"name"})
  new_class_id = new_class.get("ref_id")
  for prim_attr in prim_attrs:
    prim_attr["klass"] = new_class_id
    create("classes", "class_attribute_prim", prim_attr)
  for enum_attr in enum_attrs:
    enum_attr["klass"] = new_class_id
    create("classes", "class_attribute_enum", enum_attr)
  for rel in rels:
    rel[0]["ref_class"] = new_class_id
    src_rcr = create("classes", "relation_class_reference", rel[0])
    tgt_rcr = create("classes", "relation_class_reference", rel[1])
    create("classes", "relation", {"src": src_rcr.get("ref_id"), "tgt": tgt_rcr.get("ref_id")})
  add_class_button = False

footer()