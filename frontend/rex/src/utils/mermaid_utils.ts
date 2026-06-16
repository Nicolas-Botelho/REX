import mermaid from "mermaid"

export async function mermaidSvgCreator(steps: Array<any>) {
  mermaid.initialize({ startOnLoad: false })

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
    ${step.step_code} --> ${step.next_step.step_code}
`
      }
    }
  }

  const result = await mermaid.render(
    'my-diagram',
    diagram
  )

  return result.svg
}