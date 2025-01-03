create table
    users
(
    id               uuid references auth.users (id) primary key,
    default_model_id uuid references models (id),
    open_ai_api_key  text,
    huggingface_key  text,
    anthropic_key    text,
    perplexity_key   text,
    ollama_url       text default 'http://localhost:11434',
    created_at       timestamptz default now()
);
