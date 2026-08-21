export enum CategoryEnum {
  INPUT = 'input',
  OUTPUT = 'output',
  VALIDATION = 'validation',
  CREATE = 'create',
  READ = 'read',
  UPDATE = 'update',
  DELETE = 'delete',
  INTEGRATION = 'integration',
  SUCCESS = 'success',
  FAILURE = 'failure',
  CANCEL = 'cancel'
}

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
  class_name: string

  constructor (code: string, description: string, class_name: string) {
    this.step_code = code
    this.description = description
    this.class_name = class_name
  }
}

export class Action extends Step {
  next_step : string
  category: CategoryEnum

  constructor (code: string, description: string, class_name: string, next_step: string, category: CategoryEnum) {
    super(code, description, class_name)
    this.next_step = next_step
    this.category = category
  }
}

export class Decision extends Step {
  next_steps: Array<string>

  constructor (code: string, description: string, class_name: string, next_steps: Array<string>) {
    super(code, description, class_name)
    this.next_steps = next_steps  
  }
}