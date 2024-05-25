# synthtot.template.thought_templates.py


system_user_assistant = '{"messages": [{"role": "system", "content": "EcoBot is an eco-friendly AI assistant passionate about sustainability and environmental awareness."}, {"role": "user", "content": "What are some benefits of using solar panels?"}, {"role": "assistant", "content": "Solar panels can significantly reduce electricity bills, decrease your carbon footprint, and even increase the value of your property. Plus, they\'re a renewable energy source, helping to combat climate change."}]}'
instruct = "<s>[INST] <POTENTIAL_GENERATED_USER_QUESTION_ABOUT_SEED_CONTENT> [/INST] <YOUR_ANSWER_FOR_USER_QUESTION> </s>"


template_step1 = """
Step 1:
You are presented with a problem related to {input}. Can you brainstorm three different initial solutions in detailed?

Consider various aspects such as {perfect_consideration}.

A:
"""

template_step2 = """
Step 2:
For each of the three proposed solutions, apply your solution by considering the following aspects:
- Pros and Cons
- Initial effort needed
- Implementation difficulty
- Potential challenges
- Expected outcomes

Assign a probability of success and a confidence level to each option based on these factors.

{solutions}

A:
"""

template_step3 = """
Step 3:
For each solution, deepen the thought process by generating potential scenarios, strategies for implementation, identifying necessary partnerships or resources, and how potential obstacles might be overcome. Consider any potential unexpected outcomes and how they might be handled.

{review}

A:
"""

template_step4 = """
Step 4:
Based on the evaluations and scenarios, rank the solutions in order of promise. Provide a justification for each ranking and offer any final thoughts or considerations for each solution.

{thought_process}

A:
"""

template_step5 = """
Step 5:

Utilize natural language processing techniques and generative AI prompting techniques to create new question for {input}. 
Then, create long answers for pair textual training data for large language model training by drawing inspiration from your ranked solutions: {sorted_solutions} 

Here are the steps to follow:

1. Examine the provided random solutions to identify significant and important topics, entities, relationships, and themes. You should use each important topic, entity, relationship, and theme you recognize. You can employ methods such as named entity recognition, content summarization, keyword/keyphrase extraction, and semantic analysis to comprehend the content deeply.

2. Based on the reasoning you conducted in the first step, employ a generative language model to generate fresh, new synthetic text samples. These samples should cover the same topic, entities, relationships, and themes present in the seed data. Aim to generate {number} high-quality variations that accurately explore different Question and Answer possibilities within the data space.

3. Ensure that the generated synthetic samples exhibit language diversity. Vary elements like wording, sentence structure, tone, and complexity while retaining the core concepts. The objective is to produce diverse, representative data rather than repetitive instances.

4. The desired output length is could be more than the length of the seed content.

5. 

Create these generated synthetic samples as if you are writing from the {perspective} perspective.

Only output the resulting in the format of this example, do not change format: {prompt_template}

Do not include any commentary or extraneous casualties.

"""
