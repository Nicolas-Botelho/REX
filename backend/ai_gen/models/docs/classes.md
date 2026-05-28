# Class Model Definition

## Class
Definition of a class.

- id (int): integer class id
- name (str): unique name of the class
- stereotype (str | None): defined category of a class
- class_attributes (list[Primitive Type Attribute | Enum Type Attribute]): attributes of the class
- class_relations (list[Relation Class Reference]): relations among classes
- class_childs (list[Inheritance]): inheritances where the class is a parent of other classes
- class_parents (list[Inheritance]): inheritances where the class is a child of other classes

### Stereotypes
- Kind
- Subkind
- Role

## Class Attribute
Definition of the attributes of a class. A class attribute must be one from one of the types below.

### Primitive Type Attribute
An attribute that it's value is from a primitive type.

- id (int): integer attribute id;
- name (str): unique name of the attribute;
- attr_type (str): type of the attribute. must be one of the following: string, boolean, integer or float; and
- klass (int): integer class id. represent the class that this attribute is part of.

### Enum Type Attribute
An attribute that it's valid values are from an enum.

- id (int): integer attribute id;
- name (str): unique name of the attribute;
- enum (int): integer enum id. represent the enum that this attribute uses for its valid values; and
- klass (int): integer class id. represent the class that this attribute is part of.

## Class Relation
Definition of the relations of a class.

### Relation Class Reference
One end of a relation.

- id (int): integer relation class reference id;
- rcr_as_src (Relation | None): associated relation when the relation class reference is the source of the relation. otherwise rcr_as_src value is None. if rcr_as_src has a value, rcr_as_tgt is None;
- rcr_as_tgt (Relation | None): associated relation when the relation class reference is the target of the relation. otherwise rcr_as_tgt value is None. if rcr_as_tgt has a value, rcr_as_src is None;
- minim (int): minimal value of this end of the relation;
- maxim (int | None): maximal value if this end of the relation. if there is no defined maximal value, the value is None; and
- ref_class (ref_Class): reference to the class where this end of the relation is connected.

### Relation
The source and target of the relation.

- id (int): integer relation id;
- src (ref_RelationClassReference): reference to the relation class reference that is the source of the relation; and
- tgt (ref_RelationClassReference): reference to the relation class reference that is the target of the relation.

## Class Inheritance
Definition of the relations of a class.

### Inheritance
An inheritance between two classes.

- id (int): integer inheritance id;
- parent (ref_Class): reference to the class that is the parent (superclass); and
- child (ref_Class): reference to the class that is the child (subclass).

## Enum
Definition of the used enums.

### Enum
An enum.

- id (int): integer enum id;
- name (str): name of the enum; and
- enum_values (list[Enum Value]): values of the enum.

### Enum Value
A value used in an enum.

- id (int): integer enum value id;
- value (str): a value of the enum; and
- enum (ref_Enum): reference to the enum that this class is associated with.

## Final Observations
- ref_*: A copy of the class in place of *.