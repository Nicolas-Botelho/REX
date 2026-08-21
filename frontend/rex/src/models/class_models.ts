export class Class {
  name: string
  stereotype: string
  class_attributes: Array<ClassAttribute>

  constructor (name: string, stereotype: string, class_attributes: Array<ClassAttribute>) {
    this.name = name
    this.stereotype = stereotype
    this.class_attributes = class_attributes
  }
}

export enum TypeEnum {
  STRING = "string",
  INTEGER = "integer",
  BOOLEAN = "boolean",
  FLOAT = "float"
}

export class ClassAttribute {
  name: string
  attr_type: TypeEnum
  is_multiple: boolean
  valid_values: Array<string>

  constructor (name: string, attr_type: TypeEnum, is_multiple: boolean, valid_values: Array<string>) {
    this.name = name
    this.attr_type = attr_type
    this.is_multiple = is_multiple
    this.valid_values = valid_values
  }
}

export class Association {
  src: AssociationClassReference
  tgt: AssociationClassReference

  constructor (src: AssociationClassReference, tgt: AssociationClassReference) {
    this.src = src
    this.tgt = tgt
  }
}

export class AssociationClassReference {
  class_name: string
  class_min: number
  class_max: number | null

  constructor (class_name: string, class_min: number, class_max: number | null) {
    this.class_name = class_name
    this.class_min = class_min
    this.class_max = class_max
  }
}

export class Inheritance {
  parent_class_name : string
  child_class_name : string

  constructor (parent: string, child: string) {
    this.parent_class_name = parent
    this.child_class_name = child
  }
}