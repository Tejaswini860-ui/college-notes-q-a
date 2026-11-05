# Project Decisions

## 1. Problem

College students often have large amounts of notes in PDF and DOC/DOCX formats. Finding specific information from these notes manually can be time-consuming.

## 2. Solution

Build an AI-powered College Notes Q&A application that allows students to upload their notes and ask questions about them.

## 3. MVP

The MVP accepts:

- College notes in PDF or DOC/DOCX format
- A natural-language user prompt

The system generates an answer according to the prompt using only the uploaded notes.

## 4. Knowledge Source

The uploaded notes are the only knowledge source.

External web information and the LLM's general knowledge must not be used to answer the user's question.

## 5. RAG Requirement

The project uses Retrieval-Augmented Generation.

The basic pipeline is:

Notes → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

## 6. User Interface

A web-based interface will be built using Streamlit.

## 7. Technology Decisions

- Language: Python
- Frontend/UI: Streamlit
- PDF processing: PyMuPDF
- DOC/DOCX processing: python-docx
- Embeddings: Sentence Transformers
- Vector database: FAISS
- LLM: Gemini 3.8 Flash
- Version control: Git + GitHub

## 8. RAG Guardrail

If relevant information cannot be found in the uploaded notes, the system must not answer using external or general model knowledge.

It should explicitly state that the information is not available in the uploaded notes.

## 9. Initial Evaluation

The system will be tested using:

1. Answerable questions
2. Rephrased questions
3. Multi-part questions
4. Unanswerable questions
5. Misleading questions

## 10. Development Principle

The RAG pipeline will initially be implemented without a high-level RAG framework so that the core concepts can be understood clearly.

Frameworks may be considered later if they provide a meaningful benefit.

## 11. GitHub Requirement

This project must be maintained as a public GitHub portfolio project with:

- Meaningful commits
- Clear README
- Documentation
- Testing/evaluation results
- Architecture documentation
- Known limitations
- Future improvements