-- upgrade --
CREATE TABLE IF NOT EXISTS "guild" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "owner_id" BIGINT NOT NULL,
    "icon_url" TEXT NOT NULL,
    "config" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "infraction" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "type" INT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "user_name" VARCHAR(255) NOT NULL,
    "mod_id" BIGINT NOT NULL,
    "mod_name" VARCHAR(255) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "expires_at" TIMESTAMPTZ,
    "is_expired" BOOL NOT NULL  DEFAULT False,
    "is_hidden" BOOL NOT NULL  DEFAULT False,
    "metadata" JSONB
);
CREATE INDEX IF NOT EXISTS "idx_infraction_user_id_ad0053" ON "infraction" ("user_id");
CREATE INDEX IF NOT EXISTS "idx_infraction_mod_id_f89819" ON "infraction" ("mod_id");
CREATE TABLE IF NOT EXISTS "log" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "type" INT NOT NULL,
    "data" JSONB NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
