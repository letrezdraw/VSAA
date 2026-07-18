CREATE extension if not exists timescaledb;

create table raw_heartbeat (
    user_id text NOT NULL,
    video_id text not null,
    watch_duration INT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

select create_hypertable('raw_heartbeat', 'timestamp');