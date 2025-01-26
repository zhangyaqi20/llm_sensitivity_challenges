prompt_vanilla_bin_hatespeech_nh = ("Classify the post delimited by three backticks as non-hatespeech or hatespeech. Provide the answer as either non-hatespeech or hatespeech only."
                                   "\nExample output for non-hatespeech : non-hatespeech"
                                   "\nExample output for hatespeech : hatespeech"
                                   "\n``` {text}```")
prompt_vanilla_bin_hatespeech_hn = ("Classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only."
                                   "\nExample output for hatespeech : hatespeech"
                                   "\nExample output for non-hatespeech : non-hatespeech"
                                   "\n``` {text}```")
prompt_vanilla_bin_offensive_hn = ("Classify the post delimited by three backticks as offensive or non-offensive. Provide the answer as either offensive or non-offensive only."
                                   "\nExample output for offensive : offensive"
                                   "\nExample output for non-offensive : non-offensive"
                                   "\n``` {text}```")
prompt_vanilla_bin_offensive_nh = ("Classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only."
                                   "\nExample output for non-offensive : non-offensive"
                                   "\nExample output for offensive : offensive"
                                   "\n``` {text}```")
prompt_vanilla_bin_toxic_hn = ("Classify the post delimited by three backticks as toxic or non-toxic. Provide the answer as either toxic or non-toxic only."
                                   "\nExample output for toxic : toxic"
                                   "\nExample output for non-toxic : non-toxic"
                                   "\n``` {text}```")
prompt_vanilla_bin_toxic_nh = ("Classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only."
                                   "\nExample output for non-toxic : non-toxic"
                                   "\nExample output for toxic : toxic"
                                   "\n``` {text}```")
prompt_vanilla_bin_hof_hn = ("Classify the post delimited by three backticks as hatespeech-or-offensive or non-hatespeech-or-offensive. Provide the answer as either hatespeech-or-offensive or non-hatespeech-or-offensive only."
                                   "\nExample output for hatespeech-or-offensive : hatespeech-or-offensive"
                                   "\nExample output for non-hatespeech-or-offensive : non-hatespeech-or-offensive"
                                   "\n``` {text}```")
prompt_vanilla_bin_hof_nh = ("Classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only."
                                   "\nExample output for non-hatespeech-or-offensive : non-hatespeech-or-offensive"
                                   "\nExample output for hatespeech-or-offensive : hatespeech-or-offensive"
                                   "\n``` {text}```")

prompt_vanilla_multi_hno = ("Classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only."
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for normal : normal"
                                 "\nExample output for offensive : offensive"
                                 "\n``` {text}```")
prompt_vanilla_multi_hon = ("Classify the post delimited by three backticks as hatespeech, offensive, or normal. Provide the answer as either hatespeech, offensive, or normal only."
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for normal : normal"
                                 "\n``` {text}```")
prompt_vanilla_multi_nho = ("Classify the post delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only."
                                 "\nExample output for normal : normal"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for offensive : offensive"
                                 "\n``` {text}```")
prompt_vanilla_multi_noh = ("Classify the post delimited by three backticks as normal, offensive, or hatespeech. Provide the answer as either normal, offensive, or hatespeech only."
                                 "\nExample output for normal : normal"
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\n``` {text}```")
prompt_vanilla_multi_ohn = ("Classify the post delimited by three backticks as offensive, hatespeech, or normal. Provide the answer as either offensive, hatespeech, or normal only."
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for normal : normal"
                                 "\n``` {text}```")
prompt_vanilla_multi_onh = ("Classify the post delimited by three backticks as offensive, normal, or hatespeech. Provide the answer as either offensive, normal, or hatespeech only."
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for normal : normal"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\n``` {text}```")

prompt_vanilla_multi_hpo = ("Classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only."
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for profane : profane"
                                 "\nExample output for offensive : offensive"
                                 "\n``` {text}```")
prompt_vanilla_multi_hop = ("Classify the post delimited by three backticks as hatespeech, offensive, or profane. Provide the answer as either hatespeech, offensive, or profane only."
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for profane : profane"
                                 "\n``` {text}```")
prompt_vanilla_multi_pho = ("Classify the post delimited by three backticks as profane, hatespeech, or offensive. Provide the answer as either profane, hatespeech, or offensive only."
                                 "\nExample output for profane : profane"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for offensive : offensive"
                                 "\n``` {text}```")
prompt_vanilla_multi_poh = ("Classify the post delimited by three backticks as profane, offensive, or hatespeech. Provide the answer as either profane, offensive, or hatespeech only."
                                 "\nExample output for profane : profane"
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\n``` {text}```")
prompt_vanilla_multi_ohp = ("Classify the post delimited by three backticks as offensive, hatespeech, or profane. Provide the answer as either offensive, hatespeech, or profane only."
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\nExample output for profane : profane"
                                 "\n``` {text}```")
prompt_vanilla_multi_oph = ("Classify the post delimited by three backticks as offensive, profane, or hatespeech. Provide the answer as either offensive, profane, or hatespeech only."
                                 "\nExample output for offensive : offensive"
                                 "\nExample output for profane : profane"
                                 "\nExample output for hatespeech : hatespeech"
                                 "\n``` {text}```")

# Davidson
prompt_gpt_davidson_multi_onh_ratio_hno = """Text: ``` {text}```
Consider that the post originates from a dataset where 5.8% labels are HATESPEECH, 16.8% labels are NORMAL, and 77.4% labels are OFFENSIVE.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_hon = """Text: ``` {text}```
Consider that the post originates from a dataset where 5.8% labels are HATESPEECH, 77.4% labels are OFFENSIVE, and 16.8% labels are NORMAL.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_nho = """Text: ``` {text}```
Consider that the post originates from a dataset where 16.8% labels are NORMAL, 5.8% labels are HATESPEECH, and 77.4% labels are OFFENSIVE.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_noh = """Text: ``` {text}```
Consider that the post originates from a dataset where 16.8% labels are NORMAL, 77.4% labels are OFFENSIVE, and 5.8% labels are HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_ohn = """Text: ``` {text}```
Consider that the post originates from a dataset where 77.4% labels are OFFENSIVE, 5.8% labels are HATESPEECH, and 16.8% labels are NORMAL.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_onh = """Text: ``` {text}```
Consider that the post originates from a dataset where 77.4% labels are OFFENSIVE, 16.8% labels are NORMAL, and 5.8% labels are HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_ratio_onh_333 = """Text: ``` {text}```
Consider that the post originates from a dataset where 33.3% labels are OFFENSIVE, 33.3% labels are NORMAL, and 33.3% labels are HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""

prompt_gpt_davidson_multi_onh_feedback = """Text: ``` {text}```
You wrongly predicted as much OFFENSIVE, almost twice as much HATESPEECH, and less NORMAL compare to what is actually present in the dataset.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""

prompt_gpt_davidson_multi_onh_occurrence_same = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE, NORMAL, and HATESPEECH occur with the same frequency.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_123 = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE occurs more frequently than NORMAL, NORMAL occurs more frequently than HATESPEECH, and OFFENSIVE occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_132 = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE occurs more frequently than NORMAL, OFFENSIVE occurs more frequently than HATESPEECH, and NORMAL occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_213 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than HATESPEECH, OFFENSIVE occurs more frequently than NORMAL, and OFFENSIVE occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_231 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than HATESPEECH, OFFENSIVE occurs more frequently than HATESPEECH, and OFFENSIVE occurs more frequently than NORMAL.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_312 = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE occurs more frequently than HATESPEECH, OFFENSIVE occurs more frequently than NORMAL, and NORMAL occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_davidson_multi_onh_occurrence_321 = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE occurs more frequently than HATESPEECH, NORMAL occurs more frequently than HATESPEECH, and OFFENSIVE occurs more frequently than NORMAL.
Is this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""

prompt_vanilla_multi_nho_ratio_nho_333 = """Consider that the text originates from a dataset where 33.3% labels are normal, 33.3% labels are hatespeech, and 33.3% labels are offensive.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_nho = """Consider that the text originates from a dataset where 16.8% labels are normal, 5.8% labels are hatespeech, and 77.4% labels are offensive.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_noh = """Consider that the text originates from a dataset where 16.8% labels are normal, 77.4% labels are offensive, and 5.8% labels are hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_ohn = """Consider that the text originates from a dataset where 77.4% labels are offensive, 5.8% labels are hatespeech, and 16.8% labels are normal.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_onh = """Consider that the text originates from a dataset where 77.4% labels are offensive, 16.8% labels are normal, and 5.8% labels are hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_hno = """Consider that the text originates from a dataset where 5.8% labels are hatespeech, 16.8% labels are normal, and 77.4% labels are offensive.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_ratio_hon = """Consider that the text originates from a dataset where 5.8% labels are hatespeech, 77.4% labels are offensive, and 16.8% labels are normal.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""

prompt_vanilla_multi_nho_occurrence_same = """Consider that the text originates from a dataset where normal, hatespeech, and offensive occur with the same frequency.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_123 = """Consider that the text originates from a dataset where offensive occurs more frequently than normal, normal occurs more frequently than hatespeech, and offensive occurs more frequently than hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_132 = """Consider that the text originates from a dataset where offensive occurs more frequently than normal, offensive occurs more frequently than hatespeech, and normal occurs more frequently than hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_231 = """Consider that the text originates from a dataset where normal occurs more frequently than hatespeech, offensive occurs more frequently than hatespeech, and offensive occurs more frequently than normal.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_213 = """Consider that the text originates from a dataset where normal occurs more frequently than hatespeech, offensive occurs more frequently than normal, and offensive occurs more frequently than hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_312 = """Consider that the text originates from a dataset where offensive occurs more frequently than hatespeech, offensive occurs more frequently than normal, and normal occurs more frequently than hatespeech.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_nho_occurrence_321 = """Consider that the text originates from a dataset where offensive occurs more frequently than hatespeech, normal occurs more frequently than hatespeech, and offensive occurs more frequently than normal.
Based on this classify the text delimited by three backticks as normal, hatespeech, or offensive. Provide the answer as either normal, hatespeech, or offensive only.
Example output for normal : normal
Example output for hatespeech : hatespeech
Example output for offensive : offensive
``` {text}```"""

prompt_llama_multi_noh_ratio_noh = """The following text originates from a dataset where 16.8% labels are "NORMAL", 77.4% labels are "OFFENSIVE", and 5.8% labels are "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_noh_333 = """The following text originates from a dataset where 33.3% labels are "NORMAL", 33.3% labels are "OFFENSIVE", and 33.3% labels are "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_nho = """The following text originates from a dataset where 16.8% labels are "NORMAL", 5.8% labels are "HATESPEECH", and 77.4% labels are "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_onh = """The following text originates from a dataset where 77.4% labels are "OFFENSIVE", 16.8% labels are "NORMAL", and 5.8% labels are "HATESPEECH.
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_ohn = """The following text originates from a dataset where 77.4% labels are "OFFENSIVE", 5.8% labels are "HATESPEECH, and 16.8% labels are "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_hon = """The following text originates from a dataset where 5.8% labels are "HATESPEECH, 77.4% labels are "OFFENSIVE", and 16.8% labels are "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_ratio_hno = """The following text originates from a dataset where 5.8% labels are "HATESPEECH, 16.8% labels are "NORMAL", and 77.4% labels are "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """

prompt_llama_multi_noh_occurrence_same = """The following text originates from a dataset where "NORMAL", "OFFENSIVE", and "HATESPEECH" occur with the same frequency.
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_123 = """The following text originates from a dataset where "OFFENSIVE" occurs more frequently than "NORMAL", "NORMAL" occurs more frequently than "HATESPEECH", and "OFFENSIVE" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_132 = """The following text originates from a dataset where "OFFENSIVE" occurs more frequently than "NORMAL", "OFFENSIVE" occurs more frequently than "HATESPEECH", and "NORMAL" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_213 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "HATESPEECH", "OFFENSIVE" occurs more frequently than "NORMAL", and "OFFENSIVE" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_231 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "HATESPEECH", "OFFENSIVE" occurs more frequently than "HATESPEECH", and "OFFENSIVE" occurs more frequently than "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_312 = """The following text originates from a dataset where "OFFENSIVE" occurs more frequently than "HATESPEECH", "OFFENSIVE" occurs more frequently than "NORMAL", and "NORMAL" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_noh_occurrence_321 = """The following text originates from a dataset where "OFFENSIVE" occurs more frequently than "HATESPEECH", "NORMAL" occurs more frequently than "HATESPEECH", and "OFFENSIVE" occurs more frequently than "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """

prompt_llama_multi_noh_prevalance = """The following text originates from a dataset where "OFFENSIVE" occurs the most, "NORMAL" the second, and then "HATESPEECH" the last.
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """


prompt_gpt_bin_hatespeech_hn = "Text: ``` {text}```\nIs this text hatespeech? Answer in one word with YES or NO only."
prompt_gpt_bin_hatespeech_nh = "Text: ``` {text}```\nIs this text hatespeech? Answer in one word with NO or YES only."
prompt_gpt_bin_offensive_hn = "Text: ``` {text}```\nIs this text offensive? Answer in one word with YES or NO only."
prompt_gpt_bin_offensive_nh = "Text: ``` {text}```\nIs this text offensive? Answer in one word with NO or YES only."
prompt_gpt_bin_toxic_hn = "Text: ``` {text}```\nIs this text toxic? Answer in one word with YES or NO only."
prompt_gpt_bin_toxic_nh = "Text: ``` {text}```\nIs this text toxic? Answer in one word with NO or YES only."
prompt_gpt_bin_hof_hn = "Text: ``` {text}```\nIs this text hatespeech or offensive? Answer in one word with YES or NO only."
prompt_gpt_bin_hof_nh = "Text: ``` {text}```\nIs this text hatespeech or offensive? Answer in one word with NO or YES only."

prompt_gpt_multi_hon = """Text: ``` {text}```\nIs this text HATESPEECH, OFFENSIVE, or NORMAL? Answer in one word with HATESPEECH, OFFENSIVE, or NORMAL only."""
prompt_gpt_multi_hno = """Text: ``` {text}```\nIs this text HATESPEECH, NORMAL, or OFFENSIVE? Answer in one word with HATESPEECH, NORMAL, or OFFENSIVE only."""
prompt_gpt_multi_onh = """Text: ``` {text}```\nIs this text OFFENSIVE, NORMAL, or HATESPEECH? Answer in one word with OFFENSIVE, NORMAL, or HATESPEECH only."""
prompt_gpt_multi_ohn = """Text: ``` {text}```\nIs this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_multi_nho = """Text: ``` {text}```\nIs this text NORMAL, HATESPEECH, or OFFENSIVE? Answer in one word with NORMAL, HATESPEECH, or OFFENSIVE only."""
prompt_gpt_multi_noh = """Text: ``` {text}```\nIs this text NORMAL, OFFENSIVE, or HATESPEECH? Answer in one word with NORMAL, OFFENSIVE, or HATESPEECH only."""

prompt_gpt_multi_hop = """Text: ``` {text}```\nIs this text HATESPEECH, OFFENSIVE, or PROFANE? Answer in one word with HATESPEECH, OFFENSIVE, or PROFANE only."""
prompt_gpt_multi_hpo = """Text: ``` {text}```\nIs this text HATESPEECH, PROFANE, or OFFENSIVE? Answer in one word with HATESPEECH, PROFANE, or OFFENSIVE only."""
prompt_gpt_multi_oph = """Text: ``` {text}```\nIs this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_ohp = """Text: ``` {text}```\nIs this text OFFENSIVE, HATESPEECH, or PROFANE? Answer in one word with OFFENSIVE, HATESPEECH, or PROFANE only."""
prompt_gpt_multi_pho = """Text: ``` {text}```\nIs this text PROFANE, HATESPEECH, or OFFENSIVE? Answer in one word with PROFANE, HATESPEECH, or OFFENSIVE only."""
prompt_gpt_multi_poh = """Text: ``` {text}```\nIs this text PROFANE, OFFENSIVE, or HATESPEECH? Answer in one word with PROFANE, OFFENSIVE, or HATESPEECH only."""

prompt_llama_bin_hatespeech_nh = """Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """
prompt_llama_bin_hatespeech_hn = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "NON-HATESPEECH". Answer 0 for "HATESPEECH", and 1 for "NON-HATESPEECH". The answer is """
prompt_llama_bin_hatespeech_hn01 = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "NON-HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """
prompt_llama_bin_offensive_nh = """Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_offensive_hn = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "NON-OFFENSIVE". Answer 0 for "OFFENSIVE", and 1 for "NON-OFFENSIVE". The answer is """
prompt_llama_bin_offensive_hn01 = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "NON-OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_toxic_nh = """Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_hn = """Text: ``` {text}```\nClassify this text with "TOXIC" / "NON-TOXIC". Answer 0 for "TOXIC", and 1 for "NON-TOXIC". The answer is """
prompt_llama_bin_toxic_hn01 = """Text: ``` {text}```\nClassify this text with "TOXIC" / "NON-TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_hof_nh = """Text: ``` {text}```\nClassify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_hn = """Text: ``` {text}```\nClassify this text with "HATESPEECH-OR-OFFENSIVE" / "NON-HATESPEECH-OR-OFFENSIVE". Answer 0 for "HATESPEECH-OR-OFFENSIVE", and 1 for "NON-HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_hn01 = """Text: ``` {text}```\nClassify this text with "HATESPEECH-OR-OFFENSIVE" / "NON-HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_multi_nho = """Text: ``` {text}```\nClassify this text with "NORMAL" / "HATESPEECH" / "OFFENSIVE". Answer 0 for "NORMAL", 1 for "HATESPEECH", and 2 for "OFFENSIVE". The answer is """
prompt_llama_multi_noh = """Text: ``` {text}```\nClassify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_hon = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "NORMAL". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "NORMAL". The answer is """
prompt_llama_multi_hno = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "NORMAL" / "OFFENSIVE". Answer 0 for "HATESPEECH", 1 for "NORMAL", and 2 for "OFFENSIVE". The answer is """
prompt_llama_multi_ohn = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "HATESPEECH" / "NORMAL". Answer 0 for "OFFENSIVE", 1 for "HATESPEECH", and 2 for "NORMAL". The answer is """
prompt_llama_multi_onh = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "NORMAL" / "HATESPEECH". Answer 0 for "OFFENSIVE", 1 for "NORMAL", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_pho = """Text: ``` {text}```\nClassify this text with "PROFANE" / "HATESPEECH" / "OFFENSIVE". Answer 0 for "PROFANE", 1 for "HATESPEECH", and 2 for "OFFENSIVE". The answer is """
prompt_llama_multi_poh = """Text: ``` {text}```\nClassify this text with "PROFANE" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "PROFANE", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_hop = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hpo = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "PROFANE" / "OFFENSIVE". Answer 0 for "HATESPEECH", 1 for "PROFANE", and 2 for "OFFENSIVE". The answer is """
prompt_llama_multi_ohp = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "HATESPEECH" / "PROFANE". Answer 0 for "OFFENSIVE", 1 for "HATESPEECH", and 2 for "PROFANE". The answer is """
prompt_llama_multi_oph = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "PROFANE" / "HATESPEECH". Answer 0 for "OFFENSIVE", 1 for "PROFANE", and 2 for "HATESPEECH". The answer is """
prompt_llama_multi_pho_shift0 = """Text: ``` {text}```\nClassify this text with "PROFANE" / "HATESPEECH" / "OFFENSIVE". Answer 1 for "PROFANE", 2 for "HATESPEECH", and 3 for "OFFENSIVE". The answer is """
prompt_llama_multi_poh_shift0 = """Text: ``` {text}```\nClassify this text with "PROFANE" / "OFFENSIVE" / "HATESPEECH". Answer 1 for "PROFANE", 2 for "OFFENSIVE", and 3 for "HATESPEECH". The answer is """
prompt_llama_multi_hop_shift0 = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 1 for "HATESPEECH", 2 for "OFFENSIVE", and 3 for "PROFANE". The answer is """
prompt_llama_multi_hpo_shift0 = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "PROFANE" / "OFFENSIVE". Answer 1 for "HATESPEECH", 2 for "PROFANE", and 3 for "OFFENSIVE". The answer is """
prompt_llama_multi_ohp_shift0 = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "HATESPEECH" / "PROFANE". Answer 1 for "OFFENSIVE", 2 for "HATESPEECH", and 3 for "PROFANE". The answer is """
prompt_llama_multi_oph_shift0 = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "PROFANE" / "HATESPEECH". Answer 1 for "OFFENSIVE", 2 for "PROFANE", and 3 for "HATESPEECH". The answer is """
prompt_llama_multi_pho_text = """Text: ``` {text}```\nClassify this text with "PROFANE" / "HATESPEECH" / "OFFENSIVE". Answer in one word with "PROFANE" / "HATESPEECH" / "OFFENSIVE". Do not provide any explanation. The answer is """
prompt_llama_multi_poh_text = """Text: ``` {text}```\nClassify this text with "PROFANE" / "OFFENSIVE" / "HATESPEECH". Answer in one word with "PROFANE" / "OFFENSIVE" / "HATESPEECH". Do not provide any explanation. The answer is """
prompt_llama_multi_hop_text = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer in one word with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Do not provide any explanation. The answer is """
prompt_llama_multi_hpo_text = """Text: ``` {text}```\nClassify this text with "HATESPEECH" / "PROFANE" / "OFFENSIVE". Answer in one word with "HATESPEECH" / "PROFANE" / "OFFENSIVE". Do not provide any explanation. The answer is """
prompt_llama_multi_ohp_text = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "HATESPEECH" / "PROFANE". Answer in one word with "OFFENSIVE" / "HATESPEECH" / "PROFANE". Do not provide any explanation. The answer is """
prompt_llama_multi_oph_text = """Text: ``` {text}```\nClassify this text with "OFFENSIVE" / "PROFANE" / "HATESPEECH". Answer in one word with "OFFENSIVE" / "PROFANE" / "HATESPEECH". Do not provide any explanation. The answer is """

# HatEval
prompt_gpt_bin_hatespeech_nh_ratio_nh_7525 = """Text: ``` {text}```
Consider that the text originates from a dataset where 75% labels are non-hatespeech and 25% labels are hatespeech.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_ratio_nh = """Text: ``` {text}```
Consider that the text originates from a dataset where 58% labels are non-hatespeech and 42% labels are hatespeech.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_feedback = """Text: ``` {text}```
You predicted a bit less hatespeech than what is actually present in the dataset.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_ratio_nh_55 = """Text: ``` {text}```
Consider that the text originates from a dataset where 50% labels are non-hatespeech and 50% labels are hatespeech.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_ratio_hn = """Text: ``` {text}```
Consider that the text originates from a dataset where 42% labels are hatespeech and 58% labels are non-hatespeech.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_occurrence = """Text: ``` {text}```
Consider that the text originates from a dataset where non-hatespeech occurs more frequently than hatespeech.
Is this text hatespeech? Answer in one word with NO or YES only."""
prompt_gpt_bin_hatespeech_nh_occurrence_same = """Text: ``` {text}```
Consider that the text originates from a dataset where non-hatespeech and hatespeech occur with the same frequency.
Is this text hatespeech? Answer in one word with NO or YES only."""

# prompt_gpt_bin_hatespeech_nh_feedback_nh_eval = """Text: ``` {text}```
# Consider that the text originates from a dataset where 57.3% labels are non-hatespeech and 42.7% labels are hatespeech.
# Is this text hatespeech? Answer in one word with NO or YES only."""

prompt_llama_bin_hatespeech_nh_ratio_nh = """The following text originates from a dataset where 58% labels are "NON-HATESPEECH" and 42% labels are "HATESPEECH".
Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """
prompt_llama_bin_hatespeech_nh_ratio_hn = """The following text originates from a dataset where 42% labels are "HATESPEECH" and 58% labels are "NON-HATESPEECH".
Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """
prompt_llama_bin_hatespeech_nh_ratio_hn_55 = """The following text originates from a dataset where 50% labels are "HATESPEECH" and 50% labels are "NON-HATESPEECH".
Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """

prompt_llama_bin_hatespeech_nh_occurrence = """The following text originates from a dataset where "NON-HATESPEECH" occurs more frequently than "HATESPEECH".
Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """
prompt_llama_bin_hatespeech_nh_occurrence_same = """The following text originates from a dataset where "NON-HATESPEECH" and "HATESPEECH" occur with the same frequency.
Text: ``` {text}```\nClassify this text with "NON-HATESPEECH" / "HATESPEECH". Answer 0 for "NON-HATESPEECH", and 1 for "HATESPEECH". The answer is """

prompt_vanilla_bin_hatespeech_hn_ratio_nh = """Consider that the text originates from a dataset where 58% labels are non-hatespeech and 42% labels are hatespeech.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_hn_ratio_nh_eval = """Consider that the text originates from a dataset where 57.3% labels are non-hatespeech and 42.7% labels are hatespeech.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_hn_ratio_nh_55 = """Consider that the text originates from a dataset where 50% labels are non-hatespeech and 50% labels are hatespeech.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_hn_ratio_nh_2575 = """Consider that the text originates from a dataset where 25% labels are non-hatespeech and 75% labels are hatespeech.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
# prompt_vanilla_bin_hatespeech_hn_ratio_hn = """Consider that the text originates from a dataset where 42% labels are hatespeech and 58% labels are non-hatespeech.
# Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
# Example output for hatespeech : hatespeech
# Example output for non-hatespeech : non-hatespeech
# ``` {text}```"""
# prompt_vanilla_bin_hatespeech_nh_ratio_nh = """Consider that the text originates from a dataset where 58% labels are non-hatespeech and 42% labels are hatespeech.
# Based on this classify the post delimited by three backticks as non-hatespeech or hatespeech. Provide the answer as either non-hatespeech or hatespeech only.
# Example output for non-hatespeech : non-hatespeech
# Example output for hatespeech : hatespeech
# ``` {text}```"""
# prompt_vanilla_bin_hatespeech_nh_ratio_nh_55 = """Consider that the text originates from a dataset where 50% labels are non-hatespeech and 50% labels are hatespeech.
# Based on this classify the post delimited by three backticks as non-hatespeech or hatespeech. Provide the answer as either non-hatespeech or hatespeech only.
# Example output for non-hatespeech : non-hatespeech
# Example output for hatespeech : hatespeech
# ``` {text}```"""

prompt_vanilla_bin_hatespeech_hn_occurrence = """Consider that the text originates from a dataset where non-hatespeech occurs more frequently than hatespeech.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_nh_occurrence = """Consider that the text originates from a dataset where non-hatespeech occurs more frequently than hatespeech.
Based on this classify the post delimited by three backticks as non-hatespeech or hatespeech. Provide the answer as either non-hatespeech or hatespeech only.
Example output for non-hatespeech : non-hatespeech
Example output for hatespeech : hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_hn_occurrence_same = """Consider that the text originates from a dataset where non-hatespeech and hatespeech occur with the same frequency.
Based on this classify the post delimited by three backticks as hatespeech or non-hatespeech. Provide the answer as either hatespeech or non-hatespeech only.
Example output for hatespeech : hatespeech
Example output for non-hatespeech : non-hatespeech
``` {text}```"""
prompt_vanilla_bin_hatespeech_nh_occurrence_same = """Consider that the text originates from a dataset where non-hatespeech and hatespeech occur with the same frequency.
Based on this classify the post delimited by three backticks as non-hatespeech or hatespeech. Provide the answer as either non-hatespeech or hatespeech only.
Example output for non-hatespeech : non-hatespeech
Example output for hatespeech : hatespeech
``` {text}```"""

# OLID
prompt_gpt_bin_offensive_nh_ratio_nh = """Text: ``` {text}```
Consider that the text originates from a dataset where 66.8% labels are non-offensive and 33.2% labels are offensive.
Is this text offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_offensive_nh_ratio_hn = """Text: ``` {text}```
Consider that the text originates from a dataset where 33.2% labels are offensive and 66.8% labels are non-offensive.
Is this text offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_offensive_nh_ratio_hn_eval = """Text: ``` {text}```
Consider that the text originates from a dataset where 27.9% labels are offensive and 72.1% labels are non-offensive.
Is this text offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_offensive_nh_ratio_hn_55 = """Text: ``` {text}```
Consider that the text originates from a dataset where 50% labels are offensive and 50% labels are non-offensive.
Is this text offensive? Answer in one word with NO or YES only."""

prompt_gpt_bin_offensive_nh_feedback = """Text: ``` {text}```
You predicted as much offensive as what is actually present in the dataset.
Is this text offensive? Answer in one word with NO or YES only."""

prompt_gpt_bin_offensive_nh_occurrence = """Text: ``` {text}```
Consider that the text originates from a dataset where non-offensive occurs more frequently than offensive.
Is this text offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_offensive_nh_occurrence_same = """Text: ``` {text}```
Consider that the text originates from a dataset where non-offensive and offensive occur with the same frequency.
Is this text offensive? Answer in one word with NO or YES only."""

prompt_llama_bin_offensive_nh_ratio_nh = """The following text originates from a dataset where 66.8% labels are "NON-OFFENSIVE" and 33.2% labels are "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_offensive_nh_ratio_nh_eval = """The following text originates from a dataset where 72.1% labels are "NON-OFFENSIVE" and 27.9% labels are "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_offensive_nh_ratio_nh_55 = """The following text originates from a dataset where 50% labels are "NON-OFFENSIVE" and 50% labels are "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_offensive_nh_ratio_hn = """The following text originates from a dataset where 33.2% labels are "OFFENSIVE" and 66.8% labels are "NON-OFFENSIVE".
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """

prompt_llama_bin_offensive_nh_occurrence = """The following text originates from a dataset where "NON-OFFENSIVE" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """
prompt_llama_bin_offensive_nh_occurrence_same = """The following text originates from a dataset where "NON-OFFENSIVE" and "OFFENSIVE" occur with the same frequency.
Text: ``` {text}```\nClassify this text with "NON-OFFENSIVE" / "OFFENSIVE". Answer 0 for "NON-OFFENSIVE", and 1 for "OFFENSIVE". The answer is """

prompt_vanilla_bin_offensive_nh_ratio_nh = """Consider that the text originates from a dataset where 66.8% labels are non-offensive and 33.2% labels are offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_bin_offensive_nh_ratio_hn = """Consider that the text originates from a dataset where 33.2% labels are offensive and 66.8% labels are non-offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_bin_offensive_nh_ratio_nh_eval = """Consider that the text originates from a dataset where 72.1% labels are non-offensive and 27.9% labels are offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_bin_offensive_nh_ratio_nh_55 = """Consider that the text originates from a dataset where 50% labels are non-offensive and 50% labels are offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_bin_offensive_nh_ratio_nh_2575 = """Consider that the text originates from a dataset where 25% labels are non-offensive and 75% labels are offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""

prompt_vanilla_bin_offensive_nh_occurrence = """Consider that the text originates from a dataset where non-offensive occurs more frequently than offensive.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_bin_offensive_nh_occurrence_same = """Consider that the text originates from a dataset where non-offensive and offensive occur with the same frequency.
Based on this classify the post delimited by three backticks as non-offensive or offensive. Provide the answer as either non-offensive or offensive only.
Example output for non-offensive : non-offensive
Example output for offensive : offensive
``` {text}```"""

# CC
prompt_gpt_bin_toxic_hn_ratio_nh = """Text: ``` {text}```
Consider that the text originates from a dataset where 92% labels are non-toxic and 8% labels are toxic.
Is this text toxic? Answer in one word with YES or NO only."""
prompt_gpt_bin_toxic_hn_ratio_nh_55 = """Text: ``` {text}```
Consider that the text originates from a dataset where 50% labels are non-toxic and 50% labels are toxic.
Is this text toxic? Answer in one word with YES or NO only."""
prompt_gpt_bin_toxic_hn_ratio_hn = """Text: ``` {text}```
Consider that the text originates from a dataset where 8% labels are toxic and 92% labels are non-toxic.
Is this text toxic? Answer in one word with YES or NO only."""
prompt_gpt_bin_toxic_hn_feedback = """Text: ``` {text}```
You predicted almost twice as much toxic as what is actually present in the dataset.
Is this text toxic? Answer in one word with YES or NO only."""
prompt_gpt_bin_toxic_hn_occurrence = """Text: ``` {text}```
Consider that the text originates from a dataset where non-toxic occurs more frequently than toxic.
Is this text toxic? Answer in one word with YES or NO only."""
prompt_gpt_bin_toxic_hn_occurrence_same = """Text: ``` {text}```
Consider that the text originates from a dataset where non-toxic and toxic occur with the same frequency.
Is this text toxic? Answer in one word with YES or NO only."""

prompt_llama_bin_toxic_nh_ratio_nh = """The following text originates from a dataset where 92% labels are "NON-TOXIC" and 8% labels are "TOXIC".
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_nh_ratio_hn = """The following text originates from a dataset where 8% labels are "TOXIC" and 92% labels are "NON-TOXIC".
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_nh_ratio_hn_55 = """The following text originates from a dataset where 50% labels are "TOXIC" and 50% labels are "NON-TOXIC".
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_nh_feedback = """You predicted about six times as much "TOXIC" as what is actually present in the dataset.
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_nh_occurrence = """The following text originates from a dataset where "NON-TOXIC" occurs more frequently than "TOXIC".
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """
prompt_llama_bin_toxic_nh_occurrence_same = """The following text originates from a dataset where "NON-TOXIC" and "TOXIC" occur with the same frequency.
Text: ``` {text}```\nClassify this text with "NON-TOXIC" / "TOXIC". Answer 0 for "NON-TOXIC", and 1 for "TOXIC". The answer is """

prompt_vanilla_bin_toxic_hn_ratio_hn = """Consider that the text originates from a dataset where 8% labels are toxic and 92% labels are non-toxic.
Based on this classify the post delimited by three backticks as toxic or non-toxic. Provide the answer as either toxic or non-toxic only.
Example output for toxic : toxic
Example output for non-toxic : non-toxic
``` {text}```"""
prompt_vanilla_bin_toxic_hn_ratio_nh = """Consider that the text originates from a dataset where 92% labels are non-toxic and 8% labels are toxic.
Based on this classify the post delimited by three backticks as toxic or non-toxic. Provide the answer as either toxic or non-toxic only.
Example output for toxic : toxic
Example output for non-toxic : non-toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_ratio_hn = """Consider that the text originates from a dataset where 8% labels are toxic and 92% labels are non-toxic.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_ratio_nh = """Consider that the text originates from a dataset where 92% labels are non-toxic and 8% labels are toxic.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_ratio_nh_55 = """Consider that the text originates from a dataset where 50% labels are non-toxic and 50% labels are toxic.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_ratio_nh_2575= """Consider that the text originates from a dataset where 25% labels are non-toxic and 75% labels are toxic.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_feedback = """Consider that there are more toxic content in the dataset than you think.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_hn_occurrence = """Consider that the text originates from a dataset where non-toxic occurs more frequently than toxic.
Based on this classify the post delimited by three backticks as toxic or non-toxic. Provide the answer as either toxic or non-toxic only.
Example output for toxic : toxic
Example output for non-toxic : non-toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_occurrence = """Consider that the text originates from a dataset where non-toxic occurs more frequently than toxic.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""
prompt_vanilla_bin_toxic_nh_occurrence_same = """Consider that the text originates from a dataset where non-toxic and toxic occur with the same frequency.
Based on this classify the post delimited by three backticks as non-toxic or toxic. Provide the answer as either non-toxic or toxic only.
Example output for non-toxic : non-toxic
Example output for toxic : toxic
``` {text}```"""

# HASOC 2019
prompt_gpt_bin_hof_nh_ratio_nh = """Text: ``` {text}```
Consider that the text originates from a dataset where 61.4% labels are non-hatespeech-or-offensive and 38.6% labels are hatespeech-or-offensive.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_ratio_hn = """Text: ``` {text}```
Consider that the text originates from a dataset where 38.6% labels are hatespeech-or-offensive and 61.4% labels are non-hatespeech-or-offensive.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_ratio_hn_eval = """Text: ``` {text}```
Consider that the text originates from a dataset where 25.0% labels are hatespeech-or-offensive and 75.0% labels are non-hatespeech-or-offensive.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_ratio_hn_55 = """Text: ``` {text}```
Consider that the text originates from a dataset where 50% labels are hatespeech-or-offensive and 50% labels are non-hatespeech-or-offensive.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_feedback = """Text: ``` {text}```
You predicted as much hatespeech or offensive as what is actually present in the dataset.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_occurrence = """Text: ``` {text}```
Consider that the text originates from a dataset where non-hatespeech-or-offensive occurs more frequently than hatespeech-or-offensive.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""
prompt_gpt_bin_hof_nh_occurrence_same = """Text: ``` {text}```
Consider that the text originates from a dataset where non-hatespeech-or-offensive and hatespeech-or-offensive occur with the same frequency.
Is this text hatespeech or offensive? Answer in one word with NO or YES only."""

prompt_llama_bin_hof_nh_ratio_nh = """The following text originates from a dataset where 61.4% labels are "NON-HATESPEECH-OR-OFFENSIVE" and 38.6% labels are "HATESPEECH-OR-OFFENSIVE".
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_nh_ratio_nh_eval = """The following text originates from a dataset where 75.0% labels are "NON-HATESPEECH-OR-OFFENSIVE" and 25.0% labels are "HATESPEECH-OR-OFFENSIVE".
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_nh_ratio_nh_55 = """The following text originates from a dataset where 50% labels are "NON-HATESPEECH-OR-OFFENSIVE" and 50% labels are "HATESPEECH-OR-OFFENSIVE".
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_nh_ratio_hn = """The following text originates from a dataset where 38.6% labels are "HATESPEECH-OR-OFFENSIVE" and 61.4% labels are "NON-HATESPEECH-OR-OFFENSIVE".
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """

prompt_llama_bin_hof_nh_occurrence = """The following text originates from a dataset where "NON-HATESPEECH-OR-OFFENSIVE" occurs more frequently than "HATESPEECH-OR-OFFENSIVE".
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """
prompt_llama_bin_hof_nh_occurrence_same = """The following text originates from a dataset where "NON-HATESPEECH-OR-OFFENSIVE" and "HATESPEECH-OR-OFFENSIVE" occur with the same frequency.
Text: ``` {text}```
Classify this text with "NON-HATESPEECH-OR-OFFENSIVE" / "HATESPEECH-OR-OFFENSIVE". Answer 0 for "NON-HATESPEECH-OR-OFFENSIVE", and 1 for "HATESPEECH-OR-OFFENSIVE". The answer is """

prompt_vanilla_bin_hof_nh_ratio_nh = """Consider that the text originates from a dataset where 61.4% labels are non-hatespeech-or-offensive and 38.6% labels are hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""
prompt_vanilla_bin_hof_nh_ratio_nh_eval = """Consider that the text originates from a dataset where 75% labels are non-hatespeech-or-offensive and 25% labels are hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""
prompt_vanilla_bin_hof_nh_ratio_hn = """Consider that the text originates from a dataset where 38.6% labels are hatespeech-or-offensive and 61.4% labels are non-hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""
prompt_vanilla_bin_hof_nh_ratio_nh_55 = """Consider that the text originates from a dataset where 50% labels are non-hatespeech-or-offensive and 50% labels are hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""
prompt_vanilla_bin_hof_nh_ratio_nh_2575 = """Consider that the text originates from a dataset where 25% labels are non-hatespeech-or-offensive and 75% labels are hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""

prompt_vanilla_bin_hof_nh_occurrence = """Consider that the text originates from a dataset where non-hatespeech-or-offensive occurs more frequently than hatespeech-or-offensive.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""
prompt_vanilla_bin_hof_nh_occurrence_same = """Consider that the text originates from a dataset where non-hatespeech-or-offensive and hatespeech-or-offensive occur with the same frequency.
Based on this classify the post delimited by three backticks as non-hatespeech-or-offensive or hatespeech-or-offensive. Provide the answer as either non-hatespeech-or-offensive or hatespeech-or-offensive only.
Example output for non-hatespeech-or-offensive : non-hatespeech-or-offensive
Example output for hatespeech-or-offensive : hatespeech-or-offensive
``` {text}```"""

# HateXplain
prompt_gpt_hateXplain_multi_ohn_feedback_hno = """Text: ``` {text}```
You wrongly predicted less NORMAL, less HATESPEECH, but much more OFFENSIVE than what are actually present in the dataset.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_hno = """Text: ``` {text}```
Consider that the post originates from a dataset where 30.9% labels are HATESPEECH, 40.6% labels are NORMAL, and 28.5% labels are OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_hno_333 = """Text: ``` {text}```
Consider that the post originates from a dataset where 33.3% labels are HATESPEECH, 33.3% labels are NORMAL, and 33.3% labels are OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_hon = """Text: ``` {text}```
Consider that the post originates from a dataset where 30.9% labels are HATESPEECH, 28.5% labels are OFFENSIVE, and 40.6% labels are NORMAL.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_nho = """Text: ``` {text}```
Consider that the post originates from a dataset where 40.6% labels are NORMAL, 30.9% labels are HATESPEECH, and 28.5% labels are OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_noh = """Text: ``` {text}```
Consider that the post originates from a dataset where 40.6% labels are NORMAL, 28.5% labels are OFFENSIVE, and 30.9% labels are HATESPEECH.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_ohn = """Text: ``` {text}```
Consider that the post originates from a dataset where 28.5% labels are OFFENSIVE, 30.9% labels are HATESPEECH, and 40.6% labels are NORMAL.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_ratio_onh = """Text: ``` {text}```
Consider that the post originates from a dataset where 28.5% labels are OFFENSIVE, 40.6% labels are NORMAL, and 30.9% labels are HATESPEECH.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""

prompt_gpt_hateXplain_multi_ohn_occurrence_same = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE, HATESPEECH, and NORMAL occur with the same frequency.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_123 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than HATESPEECH, HATESPEECH occurs more frequently than OFFENSIVE, and NORMAL occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_132 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than HATESPEECH, NORMAL occurs more frequently than OFFENSIVE, and HATESPEECH occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_213 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than OFFENSIVE, NORMAL occurs more frequently than HATESPEECH, and NORMAL occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_231 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than OFFENSIVE, NORMAL occurs more frequently than OFFENSIVE, and NORMAL occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_312 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than OFFENSIVE, NORMAL occurs more frequently than HATESPEECH, and HATESPEECH occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""
prompt_gpt_hateXplain_multi_ohn_occurrence_321 = """Text: ``` {text}```
Consider that the post originates from a dataset where NORMAL occurs more frequently than OFFENSIVE, HATESPEECH occurs more frequently than OFFENSIVE, and NORMAL occurs more frequently than HATESPEECH.
Is this text OFFENSIVE, HATESPEECH, or NORMAL? Answer in one word with OFFENSIVE, HATESPEECH, or NORMAL only."""

prompt_vanilla_hateXplain_multi_hno_ratio_hno = """Consider that the post originates from a dataset where 30.9% posts are hatespeech, 40.6% posts are normal, and 28.5% posts are offensive."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_hon = """Consider that the post originates from a dataset where 30.9% posts are hatespeech, 28.5% posts are offensive, and 40.6% posts are normal."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_hon_333 = """Consider that the post originates from a dataset where 33.3% posts are hatespeech, 33.3% posts are offensive, and 33.3% posts are normal."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_nho = """Consider that the post originates from a dataset where 40.6% posts are normal, 30.9% posts are hatespeech, and 28.5% posts are offensive."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_noh = """Consider that the post originates from a dataset where 40.6% posts are normal, 28.5% posts are offensive, and 30.9% posts are hatespeech."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_ohn = """Consider that the post originates from a dataset where 28.5% posts are offensive, 30.9% posts are hatespeech, and 40.6% posts are normal."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_ratio_onh = """Consider that the post originates from a dataset where 28.5% posts are offensive, 40.6% posts are normal, and 30.9% posts are hatespeech."
Based on this classify the text delimited by three backticks as hatespeech, normal, or offensive. Provide the answer as either hatespeech, normal, or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""

prompt_vanilla_hateXplain_multi_hno_occurrence_same = """Consider that this text originates from a dataset where hatespeech, normal, and offensive occur with the same frequency.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_123 = """Consider that this text originates from a dataset where normal occurs more frequently than hatespeech, hatespeech occurs more frequently than offensive, and normal occurs more frequently than offensive.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_132 = """Consider that this text originates from a dataset where normal occurs more frequently than hatespeech, normal occurs more frequently than offensive, and hatespeech occurs more frequently than offensive.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_213 = """Consider that this text originates from a dataset where hatespeech occurs more frequently than offensive, normal occurs more frequently than hatespeech, and normal occurs more frequently than offensive.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_231 = """Consider that this text originates from a dataset where hatespeech occurs more frequently than offensive, normal occurs more frequently than offensive, and normal occurs more frequently than hatespeech.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_312 = """Consider that this text originates from a dataset where normal occurs more frequently than offensive, normal occurs more frequently than hatespeech, and hatespeech occurs more frequently than offensive.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_hateXplain_multi_hno_occurrence_321 = """Consider that this text originates from a dataset where normal occurs more frequently than offensive, hatespeech occurs more frequently than offensive, and normal occurs more frequently than hatespeech.
Based on this classify the post delimited by three backticks as hatespeech, normal or offensive. Provide the answer as either hatespeech, normal or offensive only.
Example output for hatespeech : hatespeech
Example output for normal : normal
Example output for offensive : offensive
``` {text}```"""

prompt_llama_hateXplain_multi_noh_ratio_noh = """The following text originates from a dataset where 40.6% labels are "NORMAL", 28.5% labels are "OFFENSIVE", and 30.9% labels are "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_nho = """The following text originates from a dataset where 40.6% labels are "NORMAL", 30.9% labels are "HATESPEECH", and 28.5% labels are "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_onh = """The following text originates from a dataset where 28.5% labels are "OFFENSIVE", 40.6% labels are "NORMAL", and 30.9% labels are "HATESPEECH.
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_ohn = """The following text originates from a dataset where 28.5% labels are "OFFENSIVE", 30.9% labels are "HATESPEECH, and 40.6% labels are "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_hon = """The following text originates from a dataset where 30.9% labels are "HATESPEECH, 28.5% labels are "OFFENSIVE", and 40.6% labels are "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_hon_333 = """The following text originates from a dataset where 33.3% labels are "HATESPEECH, 33.3% labels are "OFFENSIVE", and 33.3% labels are "NORMAL".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_ratio_hno = """The following text originates from a dataset where 30.9% labels are "HATESPEECH, 40.6% labels are "NORMAL", and 28.5% labels are "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """

prompt_llama_hateXplain_multi_noh_occurrence_same = """The following text originates from a dataset where "NORMAL", "OFFENSIVE", and "HATESPEECH" occur with the same frequency.
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_123 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "HATESPEECH", "HATESPEECH" occurs more frequently than "OFFENSIVE", and "NORMAL" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_132 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "HATESPEECH", "NORMAL" occurs more frequently than "OFFENSIVE", and "HATESPEECH" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_213 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "OFFENSIVE", "NORMAL" occurs more frequently than "HATESPEECH", and "NORMAL" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_231 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "OFFENSIVE", "NORMAL" occurs more frequently than "OFFENSIVE", and "NORMAL" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_312 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "OFFENSIVE", "NORMAL" occurs more frequently than "HATESPEECH", and "HATESPEECH" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """
prompt_llama_hateXplain_multi_noh_occurrence_321 = """The following text originates from a dataset where "NORMAL" occurs more frequently than "OFFENSIVE", "HATESPEECH" occurs more frequently than "OFFENSIVE", and "NORMAL" occurs more frequently than "HATESPEECH".
Text: ``` {text}```
Classify this text with "NORMAL" / "OFFENSIVE" / "HATESPEECH". Answer 0 for "NORMAL", 1 for "OFFENSIVE", and 2 for "HATESPEECH". The answer is """


# Hasoc-2019 multi
prompt_gpt_multi_oph_ratio_hpo = """Text: ``` {text}```
Consider that the post originates from a dataset where 50.5% labels are HATESPEECH, 29.5% labels are PROFANE, and 19.9% labels are OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_hop = """Text: ``` {text}```
Consider that the post originates from a dataset where 50.5% labels are HATESPEECH, 19.9% labels are OFFENSIVE, and 29.5% labels are PROFANE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_pho = """Text: ``` {text}```
Consider that the post originates from a dataset where 29.5% labels are PROFANE, 50.5% labels are HATESPEECH, and 19.9% labels are OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_poh = """Text: ``` {text}```
Consider that the post originates from a dataset where 29.5% labels are PROFANE, 19.9% labels are OFFENSIVE, and 50.5% labels are HATESPEECH.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_ohp = """Text: ``` {text}```
Consider that the post originates from a dataset where 19.9% labels are OFFENSIVE, 50.5% labels are HATESPEECH, and 29.5% labels are PROFANE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_oph = """Text: ``` {text}```
Consider that the post originates from a dataset where 19.9% labels are OFFENSIVE, 29.5% labels are PROFANE, and 50.5% labels are HATESPEECH.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_oph_eval = """Text: ``` {text}```
Consider that the post originates from a dataset where 24.7% labels are OFFENSIVE, 32.3% labels are PROFANE, and 43.1% labels are HATESPEECH.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_ratio_oph_333 = """Text: ``` {text}```
Consider that the post originates from a dataset where 33.3% labels are OFFENSIVE, 33.3% labels are PROFANE, and 33.3% labels are HATESPEECH.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""

prompt_gpt_multi_oph_feedback = """Text: ``` {text}```
You wrongly predicted much more OFFENSIVE, but less HATESPEECH and less PROFANE than what are actually present in the dataset.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""

prompt_gpt_multi_oph_occurrence_123 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than PROFANE, PROFANE occurs more frequently than OFFENSIVE, and HATESPEECH occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_132 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than PROFANE, HATESPEECH occurs more frequently than OFFENSIVE, and PROFANE occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_213 = """Text: ``` {text}```
Consider that the post originates from a dataset where PROFANE occurs more frequently than OFFENSIVE, HATESPEECH occurs more frequently than PROFANE, and HATESPEECH occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_231 = """Text: ``` {text}```
Consider that the post originates from a dataset where PROFANE occurs more frequently than OFFENSIVE, HATESPEECH occurs more frequently than OFFENSIVE, and HATESPEECH occurs more frequently than PROFANE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_312 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than OFFENSIVE, HATESPEECH occurs more frequently than PROFANE, and PROFANE occurs more frequently than OFFENSIVE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_321 = """Text: ``` {text}```
Consider that the post originates from a dataset where HATESPEECH occurs more frequently than OFFENSIVE, PROFANE occurs more frequently than OFFENSIVE, and HATESPEECH occurs more frequently than PROFANE.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""
prompt_gpt_multi_oph_occurrence_same = """Text: ``` {text}```
Consider that the post originates from a dataset where OFFENSIVE, PROFANE, and HATESPEECH occur with the same frequency.
Is this text OFFENSIVE, PROFANE, or HATESPEECH? Answer in one word with OFFENSIVE, PROFANE, or HATESPEECH only."""

prompt_llama_multi_hop_ratio_hop = """The following text originates from a dataset where 50.5% labels are "HATESPEECH", 19.9% labels are "OFFENSIVE", and 29.5% labels are "PROFANE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_hop_333 = """The following text originates from a dataset where 33.3% labels are "HATESPEECH", 33.3% labels are "OFFENSIVE", and 33.3% labels are "PROFANE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_hpo = """The following text originates from a dataset where 50.5% labels are "HATESPEECH", 29.5% labels are "PROFANE", and 19.9% labels are "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_ohp = """The following text originates from a dataset where 19.9% labels are "OFFENSIVE", 50.5% labels are "HATESPEECH", and 29.5% labels are "PROFANE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_oph = """The following text originates from a dataset where 19.9% labels are "OFFENSIVE", 29.5% labels are "PROFANE", and 50.5% labels are "HATESPEECH".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_pho = """The following text originates from a dataset where 29.5% labels are "PROFANE", 50.5% labels are "HATESPEECH", and 19.9% labels are "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_ratio_poh = """The following text originates from a dataset where 29.5% labels are "PROFANE", 19.9% labels are "OFFENSIVE", and 50.5% labels are "HATESPEECH".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """

prompt_llama_multi_hop_occurrence_same = """The following text originates from a dataset where "HATESPEECH", "OFFENSIVE", and "PROFANE" occur with the same frequency.
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_123 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "PROFANE", "PROFANE" occurs more frequently than "OFFENSIVE", and "HATESPEECH" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_132 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "PROFANE", "HATESPEECH" occurs more frequently than "OFFENSIVE", and "PROFANE" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_213 = """The following text originates from a dataset where "PROFANE" occurs more frequently than "OFFENSIVE", "HATESPEECH" occurs more frequently than "PROFANE", and "HATESPEECH" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_231 = """The following text originates from a dataset where "PROFANE" occurs more frequently than "OFFENSIVE", "HATESPEECH" occurs more frequently than "OFFENSIVE", and "HATESPEECH" occurs more frequently than "PROFANE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_312 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "OFFENSIVE", "HATESPEECH" occurs more frequently than "PROFANE", and "PROFANE" occurs more frequently than "OFFENSIVE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """
prompt_llama_multi_hop_occurrence_321 = """The following text originates from a dataset where "HATESPEECH" occurs more frequently than "OFFENSIVE", "PROFANE" occurs more frequently than "OFFENSIVE", and "HATESPEECH" occurs more frequently than "PROFANE".
Text: ``` {text}```\nClassify this text with "HATESPEECH" / "OFFENSIVE" / "PROFANE". Answer 0 for "HATESPEECH", 1 for "OFFENSIVE", and 2 for "PROFANE". The answer is """

prompt_vanilla_multi_hpo_ratio_hpo = """Consider that the text originates from a dataset where 50.5% labels are hatespeech, 29.5% labels are profane, and 19.9% labels are offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_hop = """Consider that the text originates from a dataset where 50.5% labels are hatespeech, 19.9% labels are offensive, and 29.5% labels are profane.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_ohp = """Consider that the text originates from a dataset where 19.9% labels are offensive, 50.5% labels are hatespeech, and 29.5% labels are profane.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_ohp_333 = """Consider that the text originates from a dataset where 33.3% labels are offensive, 33.3% labels are hatespeech, and 33.3% labels are profane.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_oph = """Consider that the text originates from a dataset where 19.9% labels are offensive, 29.5% labels are profane, and 50.5% labels are hatespeech.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_pho = """Consider that the text originates from a dataset where 29.5% labels are profane, 50.5% labels are hatespeech, and 19.9% labels are offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_ratio_poh = """Consider that the text originates from a dataset where 29.5% labels are profane, 19.9% labels are offensive, and 50.5% labels are hatespeech.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""

prompt_vanilla_multi_hpo_occurrence_same = """Consider that the text originates from a dataset where hatespeech, profane, and offensive occur with the same frequency.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_123 = """Consider that the text originates from a dataset where hatespeech occurs more frequently than profane, profane occurs more frequently than offensive, and hatespeech occurs more frequently than offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_132 = """Consider that the text originates from a dataset where hatespeech occurs more frequently than profane, hatespeech occurs more frequently than offensive, and profane occurs more frequently than offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_213 = """Consider that the text originates from a dataset where profane occurs more frequently than offensive, hatespeech occurs more frequently than profane, and hatespeech occurs more frequently than offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_231 = """Consider that the text originates from a dataset where profane occurs more frequently than offensive, hatespeech occurs more frequently than offensive, and hatespeech occurs more frequently than profane.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_321 = """Consider that the text originates from a dataset where hatespeech occurs more frequently than offensive, profane occurs more frequently than offensive, and hatespeech occurs more frequently than profane.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""
prompt_vanilla_multi_hpo_occurrence_312 = """Consider that the text originates from a dataset where hatespeech occurs more frequently than offensive, hatespeech occurs more frequently than profane, and profane occurs more frequently than offensive.
Based on this classify the text delimited by three backticks as hatespeech, profane, or offensive. Provide the answer as either hatespeech, profane, or offensive only.
Example output for hatespeech : hatespeech
Example output for profane : profane
Example output for offensive : offensive
``` {text}```"""

# Civil Comments
promtp_optiml_bin_toxic_nh = """
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_toxic_nh_ratio_nh = """
Consider that the text originates from a dataset where 92% labels are non-toxic and 8% labels are toxic.
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_toxic_nh_ratio_nh_55 = """
Consider that the text originates from a dataset where 50% labels are non-toxic and 50% labels are toxic.
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_toxic_nh_ratio_nh_75 = """
Consider that the text originates from a dataset where 25% labels are non-toxic and 75% labels are toxic.
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_toxic_nh_occurrence = """
Consider that the text originates from a dataset where non-toxic occurs more frequently than toxic.
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_toxic_nh_occurrence_same = """
Consider that the text originates from a dataset where non-toxic and toxic occur with the same frequency.
Is this comment toxic?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
# promtp_optiml_bin_toxic_nh_ratio_hn = """
# Consider that the text originates from a dataset where 8% labels are toxic and 92% labels are non-toxic.
# Is this comment toxic?
# " {text}
# "

# OPTIONS:
# - no
# - yes

# Answer:
# """
# promtp_optiml_bin_toxic_hn = """
# Is this comment toxic?
# " {text}
# "

# OPTIONS:
# - yes
# - no

# Answer:
# """

# Hasoc-2019
promtp_optiml_bin_hof_nh = """
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_ratio_nh = """
Consider that the text originates from a dataset where 61.4% labels are non-hatespeech-or-offensive and 38.6% labels are hatespeech-or-offensive.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_ratio_nh_eval = """
Consider that the text originates from a dataset where 75% labels are non-hatespeech-or-offensive and 25% labels are hatespeech-or-offensive.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_ratio_nh_55 = """
Consider that the text originates from a dataset where 50% labels are non-hatespeech-or-offensive and 50% labels are hatespeech-or-offensive.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_ratio_nh_75 = """
Consider that the text originates from a dataset where 25% labels are non-hatespeech-or-offensive and 75% labels are hatespeech-or-offensive.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_occurrence = """
Consider that the text originates from a dataset where non-hatespeech-or-offensive occurs more frequently than hatespeech-or-offensive.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hof_nh_occurrence_same = """
Consider that the text originates from a dataset where non-hatespeech-or-offensive and hatespeech-or-offensive occur with the same frequency.
Is this text hatespeech or offensive?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
# promtp_optiml_bin_hof_nh_ratio_hn = """
# Consider that the text originates from a dataset where 38.6% labels are hatespeech-or-offensive and 61.4% labels are non-hatespeech-or-offensive.
# Is this text hatespeech or offensive?
# " {text}
# "

# OPTIONS:
# - no
# - yes

# Answer:
# """
# promtp_optiml_bin_hof_hn = """
# Is this text hatespeech or offensive?
# " {text}
# "

# OPTIONS:
# - yes
# - no

# Answer:
# """

# HatEval
promtp_optiml_bin_hatespeech_nh = """
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hatespeech_nh_ratio_nh = """
Consider that the text originates from a dataset where 58% labels are non-hatespeech and 42% labels are hatespeech.
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hatespeech_nh_ratio_nh_55 = """
Consider that the text originates from a dataset where 50% labels are non-hatespeech and 50% labels are hatespeech.
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hatespeech_nh_ratio_nh_75 = """
Consider that the text originates from a dataset where 25% labels are non-hatespeech and 75% labels are hatespeech.
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
# promtp_optiml_bin_hatespeech_nh_ratio_hn = """
# Consider that the text originates from a dataset where 42% labels are hatespeech and 58% labels are non-hatespeech.
# Is this text hatespeech?
# " {text}
# "

# OPTIONS:
# - no
# - yes

# Answer:
# """
promtp_optiml_bin_hatespeech_nh_occurrence = """
Consider that the text originates from a dataset where non-hatespeech occurs more frequently than hatespeech.
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
promtp_optiml_bin_hatespeech_nh_occurrence_same = """
Consider that the text originates from a dataset where non-hatespeech and hatespeech occur with the same frequency.
Is this text hatespeech?
" {text}
"

OPTIONS:
- no
- yes

Answer:
"""
# promtp_optiml_bin_hatespeech_hn = """
# Is this text hatespeech?
# " {text}
# "

# OPTIONS:
# - yes
# - no

# Answer:
# """

# OLID
# promtp_optiml_bin_offensive_nh = """
# Is this text offensive?
# " {text}
# "

# OPTIONS:
# - no
# - yes

# Answer:
# """
promtp_optiml_bin_offensive_hn = """
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
promtp_optiml_bin_offensive_hn_ratio_nh = """
Consider that the text originates from a dataset where 66.8% labels are non-offensive and 33.2% labels are offensive.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
promtp_optiml_bin_offensive_hn_ratio_nh_eval = """
Consider that the text originates from a dataset where 72.1% labels are non-offensive and 27.9% labels are offensive.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
promtp_optiml_bin_offensive_hn_ratio_nh_55 = """
Consider that the text originates from a dataset where 50% labels are non-offensive and 50% labels are offensive.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
promtp_optiml_bin_offensive_hn_ratio_nh_75 = """
Consider that the text originates from a dataset where 25% labels are non-offensive and 75% labels are offensive.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
# promtp_optiml_bin_offensive_hn_ratio_hn = """
# Consider that the text originates from a dataset where 33.2% labels are offensive and 66.8% labels are non-offensive.
# Is this text offensive?
# " {text}
# "

# OPTIONS:
# - yes
# - no

# Answer:
# """
promtp_optiml_bin_offensive_hn_occurrence = """
Consider that the text originates from a dataset where non-offensive occurs more frequently than offensive.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""
promtp_optiml_bin_offensive_hn_occurrence_same = """
Consider that the text originates from a dataset where non-offensive and offensive occur with the same frequency.
Is this text offensive?
" {text}
"

OPTIONS:
- yes
- no

Answer:
"""

# Davidson
prompt_optiml_multi_hon = """
Is this text hatespeech, offensive, or normal?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- normal

Answer:
"""
prompt_optiml_davidson_multi_hon_occurrence_same = """
Consider that the post originates from a dataset where hatespeech, offensive, and normal occur with the same frequency.
Is this text hatespeech, offensive, or normal?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- normal

Answer:
"""
prompt_optiml_davidson_multi_hon_ratio_hno = """
Consider that the post originates from a dataset where 5.8% labels are hatespeech, 16.8% labels are normal, and 77.4% labels are offensive.
Is this text hatespeech, offensive, or normal?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- normal

Answer:
"""
prompt_optiml_davidson_multi_hon_ratio_hno_333 = """
Consider that the post originates from a dataset where 33.3% labels are hatespeech, 33.3% labels are normal, and 33.3% labels are offensive.
Is this text hatespeech, offensive, or normal?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- normal

Answer:
"""
prompt_optiml_davidson_multi_hon_occurrence_231 = """
Consider that the post originates from a dataset where normal occurs more frequently than hatespeech, offensive occurs more frequently than hatespeech, and offensive occurs more frequently than normal.
Is this text hatespeech, offensive, or normal?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- normal

Answer:
"""
# prompt_optiml_davidson_multi_hon_occurrence_123 = """
# Consider that the post originates from a dataset where offensive occurs more frequently than normal, normal occurs more frequently than hatespeech, and offensive occurs more frequently than hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_occurrence_132 = """
# Consider that the post originates from a dataset where offensive occurs more frequently than normal, offensive occurs more frequently than hatespeech, and normal occurs more frequently than hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_occurrence_213 = """
# Consider that the post originates from a dataset where normal occurs more frequently than hatespeech, offensive occurs more frequently than normal, and offensive occurs more frequently than hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_occurrence_312 = """
# Consider that the post originates from a dataset where offensive occurs more frequently than hatespeech, offensive occurs more frequently than normal, and normal occurs more frequently than hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_occurrence_321 = """
# Consider that the post originates from a dataset where offensive occurs more frequently than hatespeech, normal occurs more frequently than hatespeech, and offensive occurs more frequently than normal.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_ratio_hon = """
# Consider that the post originates from a dataset where 5.8% labels are hatespeech, 77.4% labels are offensive, and 16.8% labels are normal.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_ratio_nho = """
# Consider that the post originates from a dataset where 16.8% labels are normal, 5.8% labels are hatespeech, and 77.4% labels are offensive.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_ratio_noh = """
# Consider that the post originates from a dataset where 16.8% labels are normal, 77.4% labels are offensive, and 5.8% labels are hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_ratio_ohn = """
# Consider that the post originates from a dataset where 77.4% labels are offensive, 5.8% labels are hatespeech, and 16.8% labels are normal.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """
# prompt_optiml_davidson_multi_hon_ratio_onh = """
# Consider that the post originates from a dataset where 77.4% labels are offensive, 16.8% labels are normal, and 5.8% labels are hatespeech.
# Is this text hatespeech, offensive, or normal?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - normal

# Answer:
# """

# HateXplain
prompt_optiml_multi_hno = """
Is this text hatespeech, normal, or offensive?
" {text}
"

OPTIONS:
- hatespeech
- normal
- offensive

Answer:
"""
prompt_optiml_hateXplain_multi_hno_occurrence_same = """
Consider that the post originates from a dataset where hatespeech, normal, and offensive occur with the same frequency.
Is this text hatespeech, normal, or offensive?
" {text}
"

OPTIONS:
- hatespeech
- normal
- offensive

Answer:
"""
prompt_optiml_hateXplain_multi_hno_ratio_hno = """
Consider that the post originates from a dataset where 30.9% labels are hatespeech, 40.6% labels are normal, and 28.5% labels are offensive.
Is this text hatespeech, normal, or offensive?
" {text}
"

OPTIONS:
- hatespeech
- normal
- offensive

Answer:
"""
prompt_optiml_hateXplain_multi_hno_ratio_hno_333 = """
Consider that the post originates from a dataset where 33.3% labels are hatespeech, 33.3% labels are normal, and 33.3% labels are offensive.
Is this text hatespeech, normal, or offensive?
" {text}
"

OPTIONS:
- hatespeech
- normal
- offensive

Answer:
"""
prompt_optiml_hateXplain_multi_hno_occurrence_231 = """
Consider that the post originates from a dataset where hatespeech occurs more frequently than offensive, normal occurs more frequently than offensive, and normal occurs more frequently than hatespeech.
Is this text hatespeech, normal, or offensive?
" {text}
"

OPTIONS:
- hatespeech
- normal
- offensive

Answer:
"""
# prompt_optiml_hateXplain_multi_hno_occurrence_123 = """
# Consider that the post originates from a dataset where normal occurs more frequently than hatespeech, hatespeech occurs more frequently than offensive, and normal occurs more frequently than offensive.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_occurrence_132 = """
# Consider that the post originates from a dataset where normal occurs more frequently than hatespeech, normal occurs more frequently than offensive, and hatespeech occurs more frequently than offensive.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_occurrence_213 = """
# Consider that the post originates from a dataset where hatespeech occurs more frequently than offensive, normal occurs more frequently than hatespeech, and normal occurs more frequently than offensive.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_occurrence_312 = """
# Consider that the post originates from a dataset where normal occurs more frequently than offensive, normal occurs more frequently than hatespeech, and hatespeech occurs more frequently than offensive.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_occurrence_321 = """
# Consider that the post originates from a dataset where normal occurs more frequently than offensive, hatespeech occurs more frequently than offensive, and normal occurs more frequently than hatespeech.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_ratio_hon = """
# Consider that the post originates from a dataset where 30.9% labels are hatespeech, 28.5% labels are offensive, and 40.6% labels are normal.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_ratio_ohn = """
# Consider that the post originates from a dataset where 28.5% labels are offensive, 30.9% labels are hatespeech, and 40.6% labels are normal.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_ratio_onh = """
# Consider that the post originates from a dataset where 28.5% labels are offensive, 40.6% labels are normal, and 30.9% labels are hatespeech.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_ratio_noh = """
# Consider that the post originates from a dataset where 40.6% labels are normal, 28.5% labels are offensive, and 30.9% labels are hatespeech.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_hateXplain_multi_hno_ratio_nho = """
# Consider that the post originates from a dataset where 40.6% labels are normal, 30.9% labels are hatespeech, and 28.5% labels are offensive.
# Is this text hatespeech, normal, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - normal
# - offensive

# Answer:
# """
# prompt_optiml_multi_noh = """
# Is this text normal, offensive, or hatespeech?
# " {text}
# "

# OPTIONS:
# - normal
# - offensive
# - hatespeech

# Answer:
# """
# prompt_optiml_multi_nho = """
# Is this text normal, hatespeech, or offensive?
# " {text}
# "

# OPTIONS:
# - normal
# - hatespeech
# - offensive

# Answer:
# """
# prompt_optiml_multi_ohn = """
# Is this text offensive, hatespeech, or normal?
# " {text}
# "

# OPTIONS:
# - offensive
# - hatespeech
# - normal

# Answer:
# """
# prompt_optiml_multi_onh = """
# Is this text offensive, normal, or hatespeech?
# " {text}
# "

# OPTIONS:
# - offensive
# - normal
# - hatespeech

# Answer:
# """

# HASOC-2019 multi
prompt_optiml_multi_hop = """
Is this text hatespeech, offensive, or profane?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- profane

Answer:
"""
prompt_optiml_multi_hop_occurrence_same = """
Consider that the post originates from a dataset where hatespeech, offensive, and profane occur with the same frequency.
Is this text hatespeech, offensive, or profane?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- profane

Answer:
"""
prompt_optiml_multi_hop_ratio_ohp = """
Consider that the post originates from a dataset where 19.9% labels are offensive, 50.5% labels are hatespeech, and 29.5% labels are profane.
Is this text hatespeech, offensive, or profane?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- profane

Answer:
"""
prompt_optiml_multi_hop_ratio_ohp_333 = """
Consider that the post originates from a dataset where 33.3% labels are offensive, 33.3% labels are hatespeech, and 33.3% labels are profane.
Is this text hatespeech, offensive, or profane?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- profane

Answer:
"""
prompt_optiml_multi_hop_occurrence_321 = """
Consider that the text originates from a dataset where hatespeech occurs more frequently than offensive, profane occurs more frequently than offensive, and hatespeech occurs more frequently than profane.
Is this text hatespeech, offensive, or profane?
" {text}
"

OPTIONS:
- hatespeech
- offensive
- profane

Answer:
"""
# prompt_optiml_multi_hop_occurrence_123 = """
# Consider that the text originates from a dataset where hatespeech occurs more frequently than profane, profane occurs more frequently than offensive, and hatespeech occurs more frequently than offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_occurrence_132 = """
# Consider that the text originates from a dataset where hatespeech occurs more frequently than profane, hatespeech occurs more frequently than offensive, and profane occurs more frequently than offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_occurrence_213 = """
# Consider that the text originates from a dataset where profane occurs more frequently than offensive, hatespeech occurs more frequently than profane, and hatespeech occurs more frequently than offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_occurrence_231 = """
# Consider that the text originates from a dataset where profane occurs more frequently than offensive, hatespeech occurs more frequently than offensive, and hatespeech occurs more frequently than profane.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_occurrence_312 = """
# Consider that the text originates from a dataset where hatespeech occurs more frequently than offensive, hatespeech occurs more frequently than profane, and profane occurs more frequently than offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_ratio_hop = """
# Consider that the post originates from a dataset where 50.5% labels are hatespeech, 19.9% labels are offensive, and 29.5% labels are profane.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_ratio_hpo = """
# Consider that the post originates from a dataset where 50.5% labels are hatespeech, 29.5% labels are profane, and 19.9% labels are offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_ratio_pho = """
# Consider that the post originates from a dataset where 29.5% labels are profane, 50.5% labels are hatespeech, and 19.9% labels are offensive.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_ratio_poh = """
# Consider that the post originates from a dataset where 29.5% labels are profane, 19.9% labels are offensive, and 50.5% labels are hatespeech.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_hop_ratio_oph = """
# Consider that the post originates from a dataset where 19.9% labels are offensive, 29.5% labels are profane, and 50.5% labels are hatespeech.
# Is this text hatespeech, offensive, or profane?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - offensive
# - profane

# Answer:
# """
# prompt_optiml_multi_poh = """
# Is this text profane, offensive, or hatespeech?
# " {text}
# "

# OPTIONS:
# - profane
# - offensive
# - hatespeech

# Answer:
# """
# prompt_optiml_multi_pho = """
# Is this text profane, hatespeech, or offensive?
# " {text}
# "

# OPTIONS:
# - profane
# - hatespeech
# - offensive

# Answer:
# """
# prompt_optiml_multi_ohp = """
# Is this text offensive, hatespeech, or profane?
# " {text}
# "

# OPTIONS:
# - offensive
# - hatespeech
# - profane

# Answer:
# """
# prompt_optiml_multi_oph = """
# Is this text offensive, profane, or hatespeech?
# " {text}
# "

# OPTIONS:
# - offensive
# - profane
# - hatespeech

# Answer:
# """
# prompt_optiml_multi_hpo = """
# Is this text hatespeech, profane, or offensive?
# " {text}
# "

# OPTIONS:
# - hatespeech
# - profane
# - offensive

# Answer:
# """