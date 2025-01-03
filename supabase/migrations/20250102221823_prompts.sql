create table
    prompts
(
    id         uuid        default uuid_generate_v4() primary key,
    name       varchar(255) not null,
--     TODO: reactivate user_id
--     user_id    uuid references auth.users (id) not null,
    content    text not null unique,
    created_at timestamptz default now()
);
