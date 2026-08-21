export class Actor {
  name: string
  description: string

  constructor (name: string, description: string) {
    this.name = name
    this.description = description
  }
}

export enum PriorityEnum {
  MUST = 'must',
  SHOULD = 'should',
  COULD = 'could',
  WONT = 'wont'
}

export enum CategoryEnum {
  RELIABILITY = 'reliability',
  USABILITY = 'usability',
  PERFORMANCE = 'performance',
  SECURITY = 'security',
  COMPATIBILITY = 'compatibility',
  MAINTAINABILITY = 'maintainability',
  FLEXIBILITY = 'flexibility'
}

export class FunctionalRequirement {
  code: string
  description: string
  actor_name: string
  objective: string
  priority: PriorityEnum
  apply_business_rules_codes: Array<string>
  depends_on_requirements_codes: Array<string>

  constructor (code: string, description: string, actor_name: string, objective: string, priority: PriorityEnum, brs: Array<string>, frs: Array<string>) {
    this.code = code
    this.description = description
    this.actor_name = actor_name
    this.objective = objective
    this.priority = priority
    this.apply_business_rules_codes = brs
    this.depends_on_requirements_codes = frs
  }
}

export class NonFunctionalRequirement {
  code: string
  description: string
  category: CategoryEnum
  priority: PriorityEnum
  applies_on_requirements_codes: Array<string>

  constructor (code: string, description: string, category: CategoryEnum, priority: PriorityEnum, frs: Array<string>) {
    this.code = code
    this.description = description
    this.category = category
    this.priority = priority
    this.applies_on_requirements_codes = frs
  }
}

export class BusinessRule {
  code: string
  description: string

  constructor (code: string, description: string) {
    this.code = code
    this.description = description
  }
}