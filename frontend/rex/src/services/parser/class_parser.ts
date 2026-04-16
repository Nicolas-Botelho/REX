import { CstParser } from "chevrotain";

import { allTokens, arrow, attribute, cardinality, primitiveType, selectLexer, blockEnd, blockStart, breakLine, text, whiteSpace } from "./tokens";

export class ClassParser extends CstParser {
  constructor () {
    super(allTokens)

    const $ = this

    $.RULE('classDeclaration', () => {
      $.SUBRULE($.className)
      $.SUBRULE($.attributes)
      $.SUBRULE($.endClass)
      $.SUBRULE($.relations)
    })

    $.RULE('className', () => {
      $.CONSUME(text)
      $.CONSUME(blockStart)
    })

    $.RULE('attributes', () => {
      $.MANY(() => {
        $.SUBRULE($.attributeDeclaration)
      })
    })

    $.RULE('attributeDeclaration', () => {
      $.CONSUME(attribute)
      $.OR([
        { ALT: () => $.CONSUME(primitiveType)},
        { ALT: () => $.CONSUME(text)}
      ])
      $.CONSUME(breakLine)
    })

    $.RULE('endClass', () => {
      $.CONSUME(blockEnd)
    })

    $.RULE('relations', () => (
      $.MANY(() => {
        $.SUBRULE($.relationDeclaration)
        $.CONSUME(breakLine)
      })
    ))

    $.RULE('relationDeclaration', () => {
      $.SUBRULE($.source)
      $.CONSUME(arrow)
      $.SUBRULE($.target)
    })

    $.RULE('source', () => {
      $.CONSUME(text)
      $.CONSUME(cardinality)
    })

    $.RULE('target', () => {
      $.CONSUME(cardinality)
      $.CONSUME(text)
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