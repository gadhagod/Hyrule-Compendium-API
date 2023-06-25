SELECT
    * EXCEPT(_meta, _event_time),
    CAST(id as string) as _id,
    CONCAT(
        'https://botw-compendium.herokuapp.com/api/v3/compendium/entry/', 
        REPLACE (name, ' ', '_') ,
        '/image?game=totk'
    ) as image,
    false as dlc,
    'equipment' as category
FROM _input