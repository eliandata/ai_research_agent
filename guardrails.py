from agents import input_guardrail, GuardrailFunctionOutput

@input_guardrail(name="Check insults")
def no_profanity(ctx, agent, user_input: str) -> GuardrailFunctionOutput:
    forbidden = ["idiot", "stupid", "dumb", "hate"]
    text = str(user_input).lower()
    if any(word in text for word in forbidden):
        return GuardrailFunctionOutput(
            tripwire_triggered=True,
            output_info="Inappropriate input detected: offensive language"
        )
    return GuardrailFunctionOutput(tripwire_triggered=False, output_info=None)