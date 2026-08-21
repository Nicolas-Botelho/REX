export class Question {
  id: number
  question: string

  constructor (id: number, question: string) {
    this.id = id
    this.question = question
  }
}

export class NarrativeQuestion extends Question {
  constructor(id: number, question: string) {
    super(id, question)
  }
}

export class RequirementQuestion extends Question {
  requirement_codes: string[]

  constructor(id: number, question: string, requirement_codes: string[]) {
    super(id, question)
    this.requirement_codes = requirement_codes
  }
}

export class UsecaseQuestion extends Question {
  usecase_names: string[]
  
  constructor(id: number, question: string, usecase_names: string[]) {
    super(id, question)
    this.usecase_names = usecase_names
  }
}

export class ClassQuestion extends Question {
  class_names: string[]

  constructor(id: number, question: string, class_names: string[]) {
    super(id, question)
    this.class_names = class_names
  }
}