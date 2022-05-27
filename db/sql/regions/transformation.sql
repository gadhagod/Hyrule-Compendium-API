-- Casts name as ID
SELECT
    *
EXCEPT
    (),
    CAST(name as string) as _id,
FROM
    _input