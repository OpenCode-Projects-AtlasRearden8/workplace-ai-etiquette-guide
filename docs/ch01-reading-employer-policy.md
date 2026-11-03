# Chapter 1: Reading Your Employer's Policy

Before you type a single prompt into an AI tool at work, do one thing: find out what your employer's rules actually say. Most people skip this, which is how trouble starts. The good news is that finding and reading a policy is easier than it sounds.

## Why the policy matters first

AI policies answer three big questions:

- What tools am I allowed to use?
- What information am I allowed to put into them?
- Do I have to tell anyone when I use them?

If your company has no written AI policy yet, that does not mean "anything goes." It means you should use extra care with anything confidential, and stay tuned — a policy is probably coming.

## Step 1: Find the policy

Your AI rules usually live in one of these places (or several):

- The employee handbook or intranet
- An "Acceptable Use" or "Information Security" policy
- An "Acceptable Technology Use" or "Data Protection" policy
- IT announcements or an all-staff email

If you can search company documents, a text search beats skimming. Here are commands for searching a folder of company documents you have saved locally (adjust the folder name). They were tested and work:

```console
$ find ~/company-docs -iname "*handbook*" -o -iname "*policy*" -o -iname "*acceptable*"
/home/dylan/company-docs/employee-handbook-2026.pdf
/home/dylan/company-docs/acceptable-use-policy.txt
```

> The folder `~/company-docs` is just an example. Save your own documents somewhere like that first, and never upload confidential files to a public location.

To pull every "AI" mention out of the documents you copied, saving your search to a file:

```console
$ grep -riE "artificial intelligence|ai tools|chatgpt|copilot|llm" ~/company-docs > ai-mentions.txt
$ wc -l ai-mentions.txt
13 ai-mentions.txt
```

Your numbers will differ, of course. On any platform, `grep -i` means "ignore upper/lower case", so "AI tools" and "ai tools" both match; the tilde is just a shortcut for your home folder, or skip the redirect and let the results print to the screen instead.

## Step 2: Read like this

Instead of trying to absorb every word, hunt for answers in this order:

1. **Scope** — Does it cover you? ("applies to all employees using...", yes, that's you)
2. **Approved tools list** — Names of what you may use. If a tool you like isn't on the list, don't use it; ask.
3. **Confidentiality rules** — Words like "company data", "customer data", "confidential", or "internal use only".
4. **Disclosure requirements** — Phrases like "must disclose", "review required", or "supervisor approval".
5. **Consequences** — Usually near the end: "violation may result in..."

## Step 3: Turn it into plain English

Summarize the policy in three sentences using that structure. If you can't — or the wording is vague — the next best move is a simple, non-confrontational question to HR or your manager:

> "I want to make sure I'm following our AI rules. Could you point me to the part of the policy that applies to [the task you want to do]?"

That's it. Asking a genuine question is never a red flag; guessing and hoping is.

## Checklist from this chapter

- Find the policy (search local copies first)
- Note the approved-tools list
- Note what data is off-limits
- Note whether disclosure is required
- Write your three-sentence summary

---

*Education only, not legal advice. The Workplace AI Etiquette Guide, by Asdale Dynamics, LLC.*
