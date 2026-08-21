import mermaid from "mermaid"

mermaid.initialize({ startOnLoad: false })

export async function mermaidSvgCreator(steps: Array<any>) {
  let diagram = `
    graph TD
  `

  for (let step of steps) {
    if (step.next_steps) {
      for (let next of step.next_steps) {
        diagram +=
`
    ${step.step_code} --> ${next}
`
        }
      }
    else {
      if (step.next_step) {
        diagram += 
`
    ${step.step_code} --> ${step.next_step}
`
      }
    }
  }

  const result = await mermaid.render(
    `mermaid-${Math.random().toString(36).substring(2, 9)}`,
    diagram
  )

  return result.svg
}