SELECT
    *
EXCEPT
    (),
    CAST(id as string) as _id,
FROM
    _input