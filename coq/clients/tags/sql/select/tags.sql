SELECT
  tags.name     AS name,
  tags.text     AS text,
  tags.line_num AS line_num
FROM tags
JOIN files
ON files.filename = tags.filename
WHERE
  X_NORM(:word) <> ''
  AND
  files.filetype = X_NORM(:filetype)
  tags.lname LIKE X_LIKE_ESC(X_LOWER(X_NORM(:word))) ESCAPE '!'
  AND
  NOT INSTR(:word, tags.lname)

