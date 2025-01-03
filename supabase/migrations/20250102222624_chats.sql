create table
    chats
(
    id         uuid        default uuid_generate_v4() primary key,
    title      varchar(255),
    prompt_id  uuid references prompts (id) not null ,
    model_id   uuid references models (id) not null ,
--     TODO: reactivate user_id
--     user_id    uuid references auth.users (id) not null ,
    content    text not null,
    created_at timestamptz default now()
);
