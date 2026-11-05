# College Notes Q&A

An AI-powered question-answering application that allows college students to upload their notes and ask questions about them.

## Project Goal

The goal of this project is to build a Retrieval-Augmented Generation (RAG) application that answers user prompts using only the information available in the uploaded college notes.

The system should not use external web information or the LLM's general knowledge when answering questions.

## MVP

### Input
- PDF notes
- DOC/DOCX notes
- User prompt

### Output
An answer generated according to the user's prompt using only the uploaded notes.

If the required information cannot be found in the uploaded notes, the system should clearly state that the information is not available in the notes.

## Planned Architecture

```text
College Notes
     ↓
Text Extraction
     ↓
Chunking
     ↓
Embeddings
     ↓
FAISS Vector Store
     ↓
Relevant Context Retrieval
     ↓
Gemini 3.8 Flash
     ↓
Grounded Answer