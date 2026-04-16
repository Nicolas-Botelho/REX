import { CstParser } from "chevrotain";

import { allTokens, arrow, attribute, cardinality, primitiveType, selectLexer, blockEnd, blockStart, breakLine, text, whiteSpace } from "./tokens";

export class EnumParser extends CstParser {
  constructor () {
    super(allTokens)

    const $ = this

    $.RULE('enumDeclaration', () => {
      $.SUBRULE($.enumName)
      $.SUBRULE($.attributes)
      $.SUBRULE($.endEnum)
    })

    $.RULE('enumName', () => {
      $.CONSUME(text)
      $.CONSUME(blockStart)
    })

    $.RULE('attributes', () => {
      $.MANY(() => {
        $.SUBRULE($.attributeDeclaration)
      })
    })

    $.RULE('attributeDeclaration', () => {
      $.CONSUME(text)
      $.CONSUME(breakLine)
    })

    $.RULE('endEnum', () => {
      $.CONSUME(blockEnd)
    })

    this.performSelfAnalysis();
  }
}

const parserInstance = new EnumParser();

export function parse(inputText: string) {
  const lexResult = selectLexer.tokenize(inputText);

  // ".input" is a setter which will reset the parser's internal state.
  parserInstance.input = lexResult.tokens;

  // No semantic actions so this won't return anything yet.
  parserInstance.enumDeclaration();

  if (parserInstance.errors.length > 0) {
    throw Error(
      "Sad sad panda, parsing errors detected!\n" +
        parserInstance.errors[0].message,
    );
  }
}