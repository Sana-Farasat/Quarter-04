# Hooks

### Hooks kya hote hain?
<p>
Agar hum SDK ki terms mein baat karein to hooks 2 types ke hote hain:
- Agent Hooks
- Run Hooks
</p>

---

## Agent Hooks

Hooks agent ki lifecycle explain karte hain — ke agent kis time par kya kya behaviour show kar raha hai, agent kis waqt kaunsa tool call kar raha hai, tool ka kya response mil raha hai agent ko, kis sub-agent ko agent ne handoff kiya, agent loop mein kis point par error aaya — sab kuch agent hooks explain kar dete hain.

### Usage
Helpful for developers to debug each and everything related to the agent.

---

## Run Hooks

Jis tarah agent hooks hain usi tarah run hooks bhi hote hain. Agent hooks agent ka behaviour aur uski lifecycle batate hain, isi tarah run hooks runner ki lifecycle batate hain.

---

## Difference Between Agent Hooks and Run Hooks

- **Agent Hooks** local chalte hain — yani agent hook kisi ek specific agent ka behaviour aur uski lifecycle batate hain.  
- **Run Hooks** globally chalte hain — yani yeh har agent aur har tool par chalte hain.

---

## Hooks Types

- Basic Hooks  
- Intermediate Hooks  
- Advanced Hooks  

---

## Basic Hooks

1. **on_start**  
   Jab agent run hona start hota hai.

2. **on_text**  
   Jaise jaise agent text generate karta rehta hai, yeh hook active hota hai (Related to streaming).

3. **on_tool_start**  
   Jab agent tool ko call karta hai aur us tool ko input bhi deta hai.

4. **on_tool_end**  
   Jab tool apna output agent ko deta hai.

5. **on_handoff**  
   Jab agent kisi doosre sub-agent ko task delegate karta hai.

---

## Intermediate Hooks

6. **on_message**  
   Jab agent LLM ko prompt deta hai aur phir LLM ka response aata hai, phir agent LLM ko prompt deta hai aur phir response — jaise conversation ko record karte hain, yeh hook wahi kaam karta hai: raw conversation ko inspect karna.

7. **on_error**  
   Jab agent inner working kar raha hota hai (jise agent loop kehte hain — ke agent kaunsa tool call kare ya kaunse sub-agent ko task delegate kare), to is dauraan agar koi error aata hai to yeh hook batata hai.

8. **on_retry**  
   Jab agent kisi tool ko dubara call karne ki koshish karta hai ya LLM ko dubara call karta hai.

---

## Advanced Hooks

9. **on_step_start**  
   Jab agent reasoning karna start karta hai.

10. **on_step_end**  
    Jab agent reasoning complete kar leta hai.

11. **on_stop**  
    Jab agent ki execution / inner working complete ho jaati hai aur woh final output release kar deta hai.

12. **on_custom**  
    Yeh hook custom event ke liye user khud define karta hai.
