# 🛠️ Agent Tool & Handoff Handling Logic

## 🔧 Tools

### Available Tools:
- `weather`
- `dollar_rate`

### Rules for Tool Invocation:
- Jb user_input mein query `weather` aur `dollar_rate` dono ki ho to **dono tools hi call honge**.
- Tools ek time mein **multiple baar call ho sakte hain** based on user query.
- Pehle `weather`, phir `dollar_rate` tool banaya gaya.
- Lekin agar **user_input mein dono tools se related query hai**, to:

### ❓ Agent pehle kaunsa tool call karega?
- Kya jo tool pehle banaya gaya wo?
- Ya jo tool pehle tools ke parameter mein diya gaya wo?

✅ **Answer**:  
Agent **pehle wo tool call karega** jo **user query mein pehle mention hai**.  
Chahe tools ke parameter mein kisi bhi sequence mein ho.

---

### 🧪 Example

#### Tools:
- `weather`
- `dollar_rate`

#### User Input:
> Tell me today’s weather and also dollar rate.

**Explanation**:  
Input mein jis tool ki query pehle hogi, **triage agent wahi tool pehle call karega**,  
chahe tools ke parameter mein tools kisi bhi order mein ho.

---

## 🔁 Handoffs

### Rules for Handoffs:
- **Handoffs ek time mein ek hi hota hai**, chahe kitne bhi handoffs agent ko available ho.
- Agar user input mein multiple handoff related queries hoon, agent **sirf pehle wali query** ko handoff karega, baaqi ko ignore karega.
- Lekin agar **ek hi query** aisi ho jisme agent ko **dono handoff ek hi time pe execute kiye bina jawab nahi mil sakta**, to agent **confuse ho jayega**.

✅ **Solution**:  
Aise case ke liye input guardrail mein logic lagaana zaroori hai taake aise user_inputs triage agent tak jaye hi nahi.

---

### 🧪 Example

#### Sub-Agents:
- Frontend Developer
- Backend Developer

#### User Input:
> Tell me roadmap for fullstack development.

**Explanation**:  
Yeh ek aisi query hai jisme agent ko **ek hi time mein dono sub-agents ko handoff karna padega**.  
Lekin handoff ek time mein **ek hi hota hai**.  
Is situation mein agent **confuse ho jayega**.

✅ **Solution**:  
Input guardrail ka use lazmi hai taake aisi query triage agent tak na jaye.

---

## 🔄 Tools vs Handoff: Priority

### Question:
Agar query mein tools bhi ho aur handoff bhi, to agent pehle kya call karega?

### Answer:
Agent **hamesha pehle tools call karega**, uske baad handoff.

---

## ✅ Summary

| Situation                            | Agent Behavior                                              |
|-------------------------------------|-------------------------------------------------------------|
| Multiple tools in user input        | Dono tools call honge, input mein jiski query pehle hogi usse pehle call karega |
| Tools order in parameter list       | Ignore hota hai – user input ka order hi follow hota hai    |
| Multiple handoff related queries    | Sirf pehli matching query ko handoff karega                 |
| One query needs multiple handoffs   | Agent confuse ho jayega → Use input guardrails              |
| Tools + handoffs in same query      | Pehle tools call honge, phir handoff                        |

