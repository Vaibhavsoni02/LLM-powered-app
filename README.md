# 📦 LangChain tutorial #1: Build an LLM-powered app in 18 lines of code
```
⬆️ (Replace above with your app's name)
```

Description of the app ...

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-starter-kit.streamlit.app/)

## GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/app-starter-kit?quickstart=1)

## Section Heading

This is filler text, please replace this with text for this section.

## Further Reading

This is filler text, please replace this with a explanatory text about further relevant resources for this repo
- Resource 1
- Resource 2
- Resource 3

A step-by-step guide using OpenAI, LangChain, and Streamlit

In the dynamic landscape of artificial intelligence (AI), generative AI and large language models (LLMs) have emerged as game-changers, revolutionizing how we process and understand massive amounts of text data. You can use LLMs for text generation, sentiment analysis, question answering, text summarization, document translation, document classification, and much more.

If you're captivated by the transformative powers of generative AI and LLMs, then this LangChain how-to tutorial series is for you. As it progresses, it’ll tackle increasingly complex topics.

In this first part, I’ll introduce the overarching concept of LangChain and help you build a very simple LLM-powered Streamlit app in four steps:

Get an OpenAI API key
Set up the coding environment
Build the app
Deploy the app

But first, let's take a deeper look at LangChain.

What is LangChain?
LangChain is a framework that uses LLMs to build applications for various use cases. Created by Harrison Chase, it was first released as an open-source project in October 2022. To date, it has accumulated 41,900 stars on GitHub and has over 800 contributors.

star-history-2023525-1

At a high level, LangChain connects LLM models (such as OpenAI and HuggingFace Hub) to external sources like Google, Wikipedia, Notion, and Wolfram. It provides abstractions (chains and agents) and tools (prompt templates, memory, document loaders, output parsers) to interface between text input and output. LLM models and components are linked into a pipeline "chain," making it easy for developers to rapidly prototype robust applications. Simply put, Langchain orchestrates the LLM pipeline.

LangChain's power lies in its six key modules:

Model I/O: Facilitates the interface of model input (prompts) with the LLM model (closed or open-source) to produce the model output (output parsers)
Data connection: Enables user data to be loaded (document loaders), transformed (document transformers), stored (text embedding models and vector stores) and queried (retrievers)
Memory: Confer chains or agents with the capacity for short-term and long-term memory so that it remembers previous interactions with the user
Chains: A way to combine several components or other chains in a single pipeline (or “chain”)
Agents: Depending on the input, the agent decides on a course of action to take with the available tools/data that it has access to
Callbacks: Functions that are triggered to perform at specific points during the duration of an LLM run

https://blog.streamlit.io/content/images/2023/05/schematic-1.jpeg
