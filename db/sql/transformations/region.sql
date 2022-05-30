-- transformation for region collection
SELECT
    *
EXCEPT
    (),
    CAST(name as string) as _id,
FROM
    _input