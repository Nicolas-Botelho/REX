export class Usecase {
  name: string
  usecase_events: Array<Event>

  constructor (name: string, events: Array<Event>) {
    this.name = name
    this.usecase_events = events
  }
}

export class Event {
  name: string
  functional_requirements_codes: Array<string>
  event_steps: Array<Action | Decision>
  actor_name: Array<string>

  constructor (name: string, frs: Array<string>, event_steps: Array<Action | Decision>, actor_name: Array<string>) {
    this.name = name
    this.functional_requirements_codes = frs
    this.event_steps = event_steps
    this.actor_name = actor_name
  }
}

export class Step {
  step_code : string
  description : string

  constructor (code: string, description: string) {
    this.step_code = code
    this.description = description
  }
}

export class Action extends Step {
  next_step : string
  category: DataOperation | ComplexOperation | NavOperation | IOOperation// | null

  constructor (code: string, description: string, next_step: string, category: DataOperation | ComplexOperation | NavOperation | IOOperation) {
    super(code, description)
    this.next_step = next_step
    this.category = category
  }
}

export enum DataOperationEnum {
  VALIDATION = 'validation',
  CREATE = 'create',
  READ = 'read',
  UPDATE = 'update',
  DELETE = 'delete'
}

export enum ComplexOperationEnum{
  HTTP = 'http api call',
  SMTP = 'smtp api call',
  MATH = 'math',
  OTHER = 'other'
}

export enum NavOperationEnum {
  INCLUDE = 'include',
  MODAL = 'modal',
  NAVIGATE = 'navigate'
}

export enum IOOutputEnum {
  INPUT = 'input',
  OUTPUT = 'output'
}

export class DataOperation {
  attributes: any
  operation_type: DataOperationEnum

  constructor (attributes: any, operation: DataOperationEnum) {
    this.attributes = attributes
    this.operation_type = operation
  }
}

export class ComplexOperation {
  description: string
  operation_type: ComplexOperationEnum

  constructor (description: string, operation: ComplexOperationEnum) {
    this.description = description
    this.operation_type = operation
  }
}

export class NavOperation {
  usecase_name: string
  event_name: string
  operation_type: NavOperationEnum

  constructor (usecase_name: string, event_name: string, operation: NavOperationEnum) {
    this.usecase_name = usecase_name
    this.event_name = event_name
    this.operation_type = operation
  }
}

export class IOOperation {
  description: string
  operation_type: IOOutputEnum

  constructor (description: string, operation: IOOutputEnum) {
    this.description = description
    this.operation_type = operation
  }
}

export class Decision extends Step {
  next_steps: Array<string>

  constructor (code: string, description: string, next_steps: Array<string>) {
    super(code, description)
    this.next_steps = next_steps  
  }
}