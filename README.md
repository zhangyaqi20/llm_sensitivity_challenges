This repository contains the code used in the experiments for the paper [LLM Sensitivity Challenges in Abusive Language Detection: Instruction-Tuned vs. Human Feedback](https://aclanthology.org/2025.coling-main.188/) (Zhang et al., COLING 2025).

# Abstract

The capacity of large language models (LLMs) to understand and distinguish socially unacceptable texts enables them to play a promising role in abusive language detection. However, various factors can affect their sensitivity. In this work, we test whether LLMs have an unintended bias in abusive language detection, i.e., whether they predict more or less of a given abusive class than expected in zero-shot settings. Our results show that instruction-tuned LLMs tend to under-predict positive classes, since datasets used for tuning are dominated by the negative class. On the contrary, models fine-tuned with human feedback tend to be overly sensitive. In an exploratory approach to mitigate these issues, we show that label frequency in the prompt helps with the significant over-prediction.

# Conclusion

In this work, we analyzed the abusive language bias of four popular LLMs. Our results show that instruction-tuned models tend to under-predict the abusive labels, while RLHF models have the opposite tendency. Our work raises awareness about potential pitfalls in current LLM fine-tuning strategies when imbalanced training data is used for instruction-tuning as well as about achieving a better trade-off in the helpfulness and safety of LLMs
in RLHF when abusive language is included. We experimented with a preliminary method to mitigate model bias and showed promising results in the case of biased models.

# Citation

Yaqi Zhang, Viktor Hangya, and Alexander Fraser. 2025. LLM Sensitivity Challenges in Abusive Language Detection: Instruction-Tuned vs. Human Feedback. In Proceedings of the 31st International Conference on Computational Linguistics, pages 2765–2780, Abu Dhabi, UAE. Association for Computational Linguistics.
