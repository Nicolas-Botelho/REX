import { CstParser } from "chevrotain";

import { allTokens, arrow, attribute, cardinality, primitiveType, selectLexer, blockEnd, blockStart, breakLine, text, whiteSpace } from "./tokens";
import { performer } from "./tokens";
import { actor } from "./tokens";

export class UseCaseParser extends CstParser {
  constructor () {
    super(allTokens)

    const $ = this

    $.RULE('useCaseDeclaration', () => {
      $.SUBRULE($.useCaseName)
      $.SUBRULE($.events)
      $.SUBRULE($.endUseCase)
    })

    $.RULE('useCaseName', () => {
      $.CONSUME(text)
      $.CONSUME(blockStart)
    })

    $.RULE('events', () => {
      $.MANY(() => {
        $.SUBRULE($.eventDeclaration)
      })
    })

    $.RULE('eventDeclaration', () => {
      $.CONSUME(text)
      $.CONSUME(blockStart)
      $.SUBRULE($.steps)
      $.CONSUME(blockEnd)
    })

    $.RULE('steps', () => {
      $.SUBRULE($.performer)
      $.MANY(() => {
        $.SUBRULE($.stepDeclaration)
        $.CONSUME(breakLine)
      })
    })

    $.RULE('performer', () => {
      $.CONSUME(performer)
      $.CONSUME(text)
      $.CONSUME(breakLine)
    })

    $.RULE('stepDeclaration', () => {
      $.CONSUME(actor)
      $.CONSUME(text)
      $.CONSUME(breakLine)
    })

    $.RULE('endUseCase', () => {
      $.CONSUME(blockEnd)
    })

    this.performSelfAnalysis();
  }
}

const parserInstance = new ClassParser();

export function parse(inputText: string) {
  const lexResult = selectLexer.tokenize(inputText);

  // ".input" is a setter which will reset the parser's internal state.
  parserInstance.input = lexResult.tokens;

  // No semantic actions so this won't return anything yet.
  parserInstance.classDeclaration();

  if (parserInstance.errors.length > 0) {
    throw Error(
      "Sad sad panda, parsing errors detected!\n" +
        parserInstance.errors[0].message,
    );
  }
}