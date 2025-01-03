create type provider as enum ('openai', 'huggingface', 'ollama');

create table
    models
(
    id         uuid        default uuid_generate_v4() primary key ,
    name       varchar(255) not null unique,
    provider   provider not null default 'openai',
    created_at timestamptz default now()
);
