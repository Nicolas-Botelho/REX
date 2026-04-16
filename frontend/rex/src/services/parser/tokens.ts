import { createToken, Lexer } from "chevrotain";

export const text = createToken({
  name: 'Text',
  pattern: /[A-Za-z_](?:[A-Za-z0-9_]*[A-Za-z0-9_])?/
})

export const blockStart = createToken({
  name: 'Block Start',
  pattern: /{\n/
})

export const blockEnd = createToken({
  name: 'Block End',
  pattern: /(}\n|})/
})

export const whiteSpace = createToken({
  name: 'White Space',
  pattern: /\s+/,
  group: Lexer.SKIPPED
})

export const breakLine = createToken({
  name: 'Break Line',
  pattern: /\n/
})

export const attribute = createToken({
  name: 'Attribute',
  pattern: /[A-Za-z_](?:[A-Za-z0-9_]*[A-Za-z0-9_])?:/
})

export const primitiveType = createToken({
  name: 'Primitive Type',
  pattern: /(string|integer|boolean|float)/
})

export const cardinality = createToken({
  name: 'Cardinality',
  pattern: /"[0-1]..[Nn1]"/
})

export const arrow = createToken({
  name: 'Arrow',
  pattern: /-->/
})

export const performer = createToken({
  name: 'Performer',
  pattern: /performer:/
})

export const actor = createToken({
  name: 'Actor',
  pattern: /(actor|system):/
})

export const allTokens = [
  arrow, attribute, blockEnd, blockStart, breakLine, cardinality, primitiveType, text, whiteSpace
]

export const selectLexer = new Lexer(allTokens);

export function lex(inputText: string) {
  const lexingResult = selectLexer.tokenize(inputText);

  if (lexingResult.errors.length > 0) {
    throw Error("Sad Sad Panda, lexing errors detected");
  }

  return lexingResult;
}