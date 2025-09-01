# Model Settings

Hmari agentic application me hm jo model integrate karte hen uska behaviour `model_settings` se control karte hen.

---

## model_settings
Ye ek parameter hai jo hme agent k module se milti hai.

---

## ModelSetting
Ye ek class hai jo hme agent k module se milti hai.

---

## Where to Pass
Isko hm apni agent ki class me pass karte hen aur LLM ka behaviour control karte hen.

---

## Common Parameters of ModelSettings

### temperature
- Controls creativity vs accuracy.
- (Means apka answer kitna focused/predictable way me ana chaiye ya kitna creative answer hona chaiye)

**For Example:**
- Agar koi maths question hai → predictable answer chahiye.
- Agar koi essay hai → creative answer chahiye.
- Agar koi out-of-the-box / brainstorming idea ho → random answer chahiye.

**Temperature Range:** 0.0 – 2.0
- Predictable answers (math, factual Q/A): 0.1 – 0.5
- Creative answers (essays, stories, poems): 0.6 – 1.0
- Very random (brainstorming, out-of-box ideas): 1.1 – 2.0

---

### max_output_tokens
- Limit the length of responses.
- (Means LLM se jo response aaye wo kitna short ya long hona chaiye)

**Use Case:**
- Customer service / factual lookups → short response
- Tutorial / email → medium answer
- Blogging / essay / articles → long response
- Books / chapters / full code → very long response

**Tokens Limit:**
- Short answers ≤100 tokens
- Medium answers 100 – 500 tokens
- Long answers 500 – 2000 tokens
- Very long >2000 tokens

---

### top_p (nucleus sampling)
- Controls diversity of words picked.
- (LLM ke pass bahut sara data hai, `top_p` control karta hai ke model kitni variety wale words consider kare response generate karte waqt)

**For Example:**
- `top_p = 1` → Full creativity
- `top_p = 0.2` → Only pick the most likely words

**Range:** 0.0 – 1.0
- Highly focused (factual Q/A, math, coding): 0.0 – 0.3
- Balanced creativity (essays, tutorials, storytelling): 0.4 – 0.7
- Very diverse & random (brainstorming, poetry, jokes): 0.8 – 1.0

---

### top_k
- Top_k ek aur sampling technique hai jo model ke output ko control karti hai.
- Ye batata hai ke model sirf top k words consider kare agla word predict karte waqt.

**Use Case:**
- Low top_k (1–5) → Exact, deterministic answers (maths, facts, coding)
- Medium top_k (20–50) → Balanced answers (Q/A with some variety)
- High top_k (100–500) → Creative tasks (story writing, brainstorming)

---

### stop_sequences
- Tell the model to stop generating when a certain word/character is seen.
- (stop_sequences batata hai ke model response kahan stop kare)

**Range / Values:** List of strings

**Use Cases:**
- Code generation → `stop_sequences=["```"]` → code block ke baad generate band ho jaye.
- Chatbot conversation → `stop_sequences=["User:"]` → jab user ka next input start ho → model stop kare.

---

### response_format
- Force the model to output in developer's desired format, not free text.

**For Example:**
- **Text / String:** Default, plain text
  - Use Case: Chatbots, Q/A, essays, stories
- **JSON Object / Dict:** Structured JSON/dict
  - Use Case: Weather app, dashboard
- **List / Array:** Multiple items
  - Use Case: Brainstorming, recommendation lists
- **Custom / Mixed:** Nested JSON or custom structure
  - Use Case: Step-by-step guides, tutorials, structured tasks

---

### frequency_penalty
- Discourages repetition of same word/phrase
- Use Case: Prevents model from repeating "love love love..." in generated text

---

### presence_penalty
- Encourages introducing new topics
- Use Case: Brainstorming new startup ideas

---

### tool_choice
- By default, model auto-selects which tool to call.
- Values:
  - `auto` (default) → Model decides whether to use a tool
  - `required` → Must use a tool for every response
  - `None` → Forbid tool usage
  - `name_of_tool` → Force a specific tool

---

### parallel_tool_calls
- Run multiple tools at the same time.
- Boolean value (True / False)

**Use Case:**
- Without it → first gets weather, then date
- With it → calls both tools in parallel → faster

---

### truncation ("auto" vs "disabled")
- LLMs have a context window (e.g., 128k tokens)
- If input is too long, it can be truncated

**Use Case:**
- Long docs → ensures model doesn’t crash
- Text cut → shows "..." at the end

---

### max_tokens
- Same as `max_output_tokens`, just newer name in some SDKs

---

### verbosity
- Controls how much detail the model includes

**Use Case:**
- low → short answers (customer support)
- high → detailed breakdown (education, tutoring)
