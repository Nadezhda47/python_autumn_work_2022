CREATE TABLE "composition" (
  "id" SERIAL PRIMARY KEY,
  "music_track" VARCHAR(100) NOT NULL
);

CREATE TABLE "music_artist" (
  "id" SERIAL PRIMARY KEY,
  "artist_name" VARCHAR(100) NOT NULL,
  "description" TEXT NOT NULL,
  "genre" VARCHAR(100) NOT NULL,
  "country" VARCHAR(100) NOT NULL
);

CREATE TABLE "album" (
  "id" SERIAL PRIMARY KEY,
  "id_music_artist" INTEGER NOT NULL,
  "album_title" VARCHAR(50) NOT NULL,
  "description" TEXT NOT NULL,
  "release_year" INTEGER,
  "genre" VARCHAR(100) NOT NULL,
  "label" VARCHAR(50) NOT NULL,
  "media_type" TEXT NOT NULL,
  "location" VARCHAR(10) NOT NULL
);

CREATE TABLE "artist_track" (
  "id_music_artist" INTEGER PRIMARY KEY,
  "id_composition" INTEGER NOT NULL
);

CREATE TABLE "composition_album" (
  "id" TEXT PRIMARY KEY,
  "id_album" INTEGER NOT NULL,
  "id_composition" INTEGER NOT NULL
);





CREATE INDEX "idx_album__id_music_artist" ON "album" ("id_music_artist");

ALTER TABLE "album" ADD CONSTRAINT "fk_album__id_music_artist" FOREIGN KEY ("id_music_artist") REFERENCES "music_artist" ("id") ON DELETE CASCADE;

CREATE INDEX "idx_artist_track__id_composition" ON "artist_track" ("id_composition");

ALTER TABLE "artist_track" ADD CONSTRAINT "fk_artist_track__id_composition" FOREIGN KEY ("id_composition") REFERENCES "composition" ("id") ON DELETE CASCADE;

ALTER TABLE "artist_track" ADD CONSTRAINT "fk_artist_track__id_music_artist" FOREIGN KEY ("id_music_artist") REFERENCES "music_artist" ("id") ON DELETE CASCADE;


CREATE INDEX "idx_composition_album__id_album" ON "composition_album" ("id_album");

CREATE INDEX "idx_composition_album__id_composition" ON "composition_album" ("id_composition");

ALTER TABLE "composition_album" ADD CONSTRAINT "fk_composition_album__id_album" FOREIGN KEY ("id_album") REFERENCES "album" ("id") ON DELETE CASCADE;

ALTER TABLE "composition_album" ADD CONSTRAINT "fk_composition_album__id_composition" FOREIGN KEY ("id_composition") REFERENCES "composition" ("id") ON DELETE CASCADE

