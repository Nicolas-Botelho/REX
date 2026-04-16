import { CstParser } from "chevrotain";

import { allTokens, arrow, attribute, cardinality, primitiveType, selectLexer, blockEnd, blockStart, breakLine, text, whiteSpace } from "./tokens";

export class ActorParser extends CstParser {
  constructor () {
    super(allTokens)

    const $ = this

    $.RULE('actorDeclaration', () => {
      $.SUBRULE($.actorName)
      $.SUBRULE($.description)
      $.SUBRULE($.endActor)
    })

    $.RULE('actorName', () => {
      $.CONSUME(text)
      $.CONSUME(blockStart)
    })

    $.RULE('description', () => {
      $.MANY(() => {
        $.SUBRULE($.paragraph)
      })
    })

    $.RULE('paragraph', () => {
      $.CONSUME(text)
      $.CONSUME(breakLine)
    })

    $.RULE('endActor', () => {
      $.CONSUME(blockEnd)
    })

    this.performSelfAnalysis();
  }
}

const parserInstance = new ActorParser();

export function parse(inputText: string) {
  const lexResult = selectLexer.tokenize(inputText);

  // ".input" is a setter which will reset the parser's internal state.
  parserInstance.input = lexResult.tokens;

  // No semantic actions so this won't return anything yet.
  parserInstance.actorDeclaration();

  if (parserInstance.errors.length > 0) {
    throw Error(
      "Sad sad panda, parsing errors detected!\n" +
        parserInstance.errors[0].message,
    );
  }
}