# I want to write llm.py. I will write this by myself, This will be my llm.py which I would be using where ever I will working and needed.

# Most of the people follow OpenAI Library (SDK) for exposing the LLMs and also to access the LLMs. It has become like an industry standard, So I will use that.

from openai import OpenAI
import base64

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = "",
)

print(type(client))

# response = client.responses.create(
#   model="nvidia/nemotron-3.5-super-vl:free",
#   input="Generate an image of Taj Mahal."
# )

# giving the input as an image and expecting the output as text.

# convert image into base64
with open("/Users/ajaykrishna22/Documents/documentqa/documentqa/Screenshot 2026-11-21 at 12.09.37.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

response = client.responses.create(
    model="nvidia/nemotron-3.5-super-vl:free",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Extract all the text from this image"
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{image_base64}"
                }
            ]
        }
    ]
)

print(response.output_text)
print("****************")
print(response)
print("***************************")
print(response.output)

print("Output Type : ", response.output[0].type)
print("Length of the output list : ", len(response.output))
#print("All the variable and functions of the object respone.output[0] ",dir(response.output[0]))
#print(type(response.output[0].result))
#print(response.output[0].result)
# image_data = response.output[0].result
# image_base64 = image_data
# with open("tajmahal.png", "wb") as f:
#     f.write(base64.b64decode(image_base64))
    
print(type(response))
#print(response)

#Response(id='gen-1795264806-ECOZyyNMcfFwoU0vjA69', access_programs=None, created_at=1795264806.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='nvidia/nemotron-3.5-super-vl:free', object='response', output=[ResponseReasoningItem(id='rs_tmp_9hxrpmqlrer', summary=[], type='reasoning', content=[Content(text='The user wants me to extract all the text visible in the image.\n\n1.  **Analyze the image:**\n    *   It\'s a screenshot of a dark-themed text box, likely a code block or a terminal window.\n    *   There\'s a header "PROMPT" in green.\n    *   Below that is a block of white text on a dark background.\n\n2.  **Transcribe the text line by line:**\n    *   Line 1 (Header): PROMPT\n    *   Line 2: Create AGENTS.md describing only what is true\n    *   Line 3: today: the stack, a short module map, the\n    *   Line 4: commands, and these rules: write\n  *   Line 5: characterization tests before changing\n    *   Line 6: behaviour; change only the module the ticket is\n    *   Line 7: about; tests never touch data/db.json; add no\n    *   Line 8: dependencies.\n\n3.  **Refine the transcription:**\n    *   Check capitalization: "PROMPT" is uppercase. "AGENTS.md" is mixed case. "behaviour" is spelled with an \'u\' (British English).\n    *   Check punctuation: Colons, semicolons, periods.\n    *   Check line breaks: The text wraps, but I should probably present it as a coherent block or line-by-line as it appears. The prompt asks to "Extract all the text", so a direct transcription preserving the flow is best.\n\n4.  **Final Output Formulation:**\n    *   Combine the lines into a single block of text.\n\n    Text:\n    PROMPT\n    Create AGENTS.md describing only what is true today: the stack, a short module map, the commands, andthese rules: write characterization tests before changing behaviour; change only the module the ticket is about; tests never touch data/db.json; add no dependencies.\n\n    Let\'s double check against the image.\n    - "PROMPT" is clearly visible at top left.\n    - "Create AGENTS.md describing only what is true" matches.\n    - "today: the stack, a short module map, the" matches.\n    - "commands, and these rules: write" matches.\n    - "characterization tests before changing" matches.\n    - "behaviour; change only the module the ticket is" matches.\n    - "about; tests never touch data/db.json; add no" matches.\n    - "dependencies." matches.\n\n    The request is simple: "Extract all the text from this image". I will provide the text exactly as seen.', type='reasoning_text')], encrypted_content=None, status='completed', format='unknown'), ResponseOutputMessage(id='msg_tmp_xefqe220eq', content=[ResponseOutputText(annotations=[], text='PROMPT\n\nCreate AGENTS.md describing only what is true today: the stack, a short module map, the commands, and these rules: write characterization tests before changing behaviour; change only the module the ticket is about; tests never touch data/db.json; add no dependencies.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message', phase=None)], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[], top_p=1.0, background=False, completed_at=1795264812.0, conversation=None, image=None, input_transformations=None, max_output_tokens=None, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_diagnostics=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention=None, reasoning=None, safety_identifier=None, service_tier='auto', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity=None), tool_usage=None, top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=706, input_tokens_details=InputTokensDetails(cache_write_tokens=None, cached_tokens=0, cache_write_tokens_details=None), output_tokens=610, output_tokens_details=OutputTokensDetails(reasoning_tokens=551), total_tokens=1316, cost=0, is_byok=False, cost_details={'upstream_inference_cost': 0, 'upstream_inference_input_cost': 0, 'upstream_inference_output_cost': 0}), user=None, presence_penalty=0, frequency_penalty=0, store=False)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Response : ", response.output[0].content[0].text)
print("Number of Input tokens : ", response.usage.input_tokens)
print("Number of output tokens : ", response.usage.output_tokens)
print("Total Number of tokens : ", response.usage.total_tokens)
print("Total Cost : ", response.usage.cost_details['upstream_inference_cost'])

# ---------------- Input : text, Output : text ---------------------------------
#Response(
#   id='gen-1795177805-Bajz4uauJhrq9fEfPq6J', 
#   access_programs=None, 
#   created_at=1795177805.0, 
#   error=None, 
#   incomplete_details=None, 
#   instructions=None, 
#   metadata={}, 
#   model='nvidia/nemotron-3.5-super-vl:free', 
#   object='response', 
#   output=[ResponseReasoningItem(id='rs_tmp_unxii8rsxh', 
#                                 summary=[], 
#                                 type='reasoning', 
#                                 content=[Content(text='The user is asking "What is the meaning of life?" This is a classic philosophical question with no single definitive answer. I should provide a thoughtful, balanced overview of different perspectives rather than asserting one absolute truth.\n\nKey angles to cover:\n1. Philosophical perspectives (nihilism, existentialism, absurdism, religious/spiritual views)\n2. Scientific/biological perspective (survival, reproduction, evolution)\n3. Psychological/humanistic perspective (self-actualization, meaning-making, connection)\n4. Pop/personal approach (creating your own meaning, relationships, contribution, experiences)\n5. Pop culture reference (42 from Hitchhiker\'s Guide) - optional but can add levity\n\nTone should be respectful, open-ended, encouraging reflection. Avoid being preachy or dismissive. Acknowledge that it\'s subjective.\n\nStructure:\n- Direct acknowledgment that there\'s no single answer\n- Brief overview of major frameworks\n- Synthesis: meaning as something created rather than discovered\n- Practical suggestions for finding/creating meaning\n- Concluding thought\n\nLet me draft this carefully.\n\nPossible pitfalls:\n- Don\'t privilege one religion over others\n- Don\'t be overly bleak (nihilism) without balancing with optimistic existentialism\n- Don\'t oversimplify science\n\nDrafting content:\n\nIntroduction: The meaning of life is one of humanity\'s oldest questions, and answers depend entirely on who you ask.\n\nPerspectives:\n- Religious/Spiritual: divine purpose, serving God, karma, enlightenment, afterlife\n- Philosophical: \n  * Existentialism (Sartre, Camus): life has no inherent meaning, so we must create our own through authentic choices\n  * Absurdism: embrace the lack of meaning and live rebelliously/happily anyway\n  * Nihilism: no objective meaning (can be liberating or depressing)\n- Biological: survive, reproduce, pass on genes, contribute to species continuity\n- Psychological: Viktor Frankl (Man\'s Search for Meaning) - meaning found in work, love, courage in suffering; self-actualization (Maslow)\n- Human connections: relationships, community, helping others, leaving legacy\n\nPractical takeaways:\n- Meaning is often found in small moments, not just grand purpose\n- Connection, contribution, creativity, curiosity\n- It can change over life stages\n\nHumor: 42 (Hitchhiker\'s Guide)\n\nConclusion: Perhaps the question itself is the point—the search is where meaning happens.\n\nThis looks solid. I\'ll write it in a clear, accessible style.', type='reasoning_text')], encrypted_content=None, status='completed', format='unknown'), ResponseOutputMessage(id='msg_tmp_q8walhl7rle', content=[ResponseOutputText(annotations=[], text='There is no single, universally agreed-upon answer to “What is the meaning of life?” The response depends heavily on whether you ask a philosopher, a scientist, a theologian, an artist, or someone reflecting on their own experience.\n\nHere are some of the most common frameworks people use to think about it:\n\n### 1. You create it (Existentialism)\nThinkers like Jean-Paul Sartre and Albert Camus argued that life has no inherent, pre-assigned meaning. Instead, meaning is something *you* forge through your choices, actions, and values. In this view, freedom is both a burden and an opportunity: you are responsible for defining what matters to you.\n\n### 2. Connection and contribution (Humanistic/Psychological)\nMany psychologists, including Viktor Frankl (a Holocaust survivor and author of *Man’s Search for Meaning*), suggest that meaning is found in:\n- **Work or creative expression** — doing something that matters to you\n- **Love and relationships** — deep connections with other people\n- **Courage in suffering** — how you respond to unavoidable hardship\n\nIn this view, meaning isn’t a grand secret waiting to be discovered; it’s built through caring for others, growing as a person, and contributing to something beyond yourself.\n\n### 3. Biological purpose (Science/Evolution)\nFrom a strictly evolutionary standpoint, the “purpose” of life is survival and reproduction—passing on genes and helping the species continue. Of course, most people find this description too narrow to capture what makes a human life feel meaningful, but it does explain why we are wired for connection, care for offspring, and social belonging.\n\n### 4. Spiritual or religious purpose\nMany traditions teach that meaning comes from a relationship with the divine, living in accordance with spiritual principles, serving others, seeking enlightenment, or preparing for an afterlife. Answers vary widely across faiths, but common threads include love, moral duty, transcendence, and inner peace.\n\n### 5. There is no meaning (Nihilism / Absurdism)\nSome conclude that the universe is indifferent and life has no objective meaning. While that can sound bleak, many find it liberating: if nothing is preordained, you are free to enjoy life, be kind, and pursue what you love without the pressure of fulfilling a cosmic destiny.\n\n---\n\n### A practical way to think about it\nRather than searching for *the* meaning of life, many people find more peace by asking:\n- **What feels meaningful to me right now?**\n- **What relationships do I want to nurture?**\n- **What small actions make me feel connected or useful?**\n\nMeaning often shows up in ordinary moments—a conversation, a shared meal, a piece of music, helping someone, or creating something—rather than in one final answer.\n\nAnd, if you want the pop-culture shortcut: according to *The Hitchhiker’s Guide to the Galaxy*, the answer is **42**. The trick, the story suggests, is knowing the right question.', 
#                                                  type='output_text', 
#                                                  logprobs=[]
#                                                  )
#                                         ], 
#                                 role='assistant', 
#                                 status='completed', 
#                                 type='message', 
#                                 phase=None
#                                )
#           ], 
#   parallel_tool_calls=True, 
#   temperature=1.0, 
#   tool_choice='auto', 
#   tools=[], 
#   top_p=1.0, 
#   background=False, 
#   completed_at=1795177815.0, 
#   conversation=None, 
#   image=None, 
#   input_transformations=None, 
#   max_output_tokens=None, 
#   max_tool_calls=None, 
#   moderation=None, 
#   previous_response_id=None, 
#   prompt=None, 
#   prompt_cache_diagnostics=None, 
#   prompt_cache_key=None, 
#   prompt_cache_options=None, 
#   prompt_cache_retention=None, 
#   reasoning=None, 
#   safety_identifier=None, 
#   service_tier='auto', 
#   status='completed', 
#   text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity=None), 
#   tool_usage=None, 
#   top_logprobs=0, 
#   truncation='disabled', 
#   usage=ResponseUsage(
#                       input_tokens=23, input_tokens_details=InputTokensDetails(cache_write_tokens=None, cached_tokens=0, cache_write_tokens_details=None), 
#                       output_tokens=1156, output_tokens_details=OutputTokensDetails(reasoning_tokens=531), 
#                       total_tokens=1179, 
#                       cost=0, 
#                       is_byok=False, 
#                       cost_details={'upstream_inference_cost': 0, 'upstream_inference_input_cost': 0, 'upstream_inference_output_cost': 0}
#                       ), 
#   user=None, 
#   presence_penalty=0, 
#   frequency_penalty=0, 
#   store=False
#  )

# What do we need

# 1. Actual and Final response : response.output[0].content[0].text
# 2. Number of input tokens
# 3. Number of output tokens
# 4. Cost, Cost for input tokens, Cost for output tokens, Total Cost
# 5. Reasoning if done.
# 6. Reasoning tokens.


# text --> text
# text ---> Image
# image ---> text

