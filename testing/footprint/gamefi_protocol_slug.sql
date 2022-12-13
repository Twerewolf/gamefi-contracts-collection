SELECT  "footprint"."gamefi_protocol_daily_stats"."on_date"                AS "on_date"
       ,"footprint"."gamefi_protocol_daily_stats"."protocol_name"          AS "protocol_name"
       ,"footprint"."gamefi_protocol_daily_stats"."logo"                   AS "logo"
       ,"footprint"."gamefi_protocol_daily_stats"."protocol_slug"          AS "protocol_slug"
       ,"footprint"."gamefi_protocol_daily_stats"."number_of_transactions" AS "number_of_transactions"
       ,"footprint"."gamefi_protocol_daily_stats"."number_of_active_users" AS "number_of_active_users"
       ,"footprint"."gamefi_protocol_daily_stats"."chain"                  AS "chain"
       ,"footprint"."gamefi_protocol_daily_stats"."volume"                 AS "volume"
FROM "footprint"."gamefi_protocol_daily_stats"
WHERE "footprint"."gamefi_protocol_daily_stats"."chain" = 'BNB Chain'
ORDER BY "footprint"."gamefi_protocol_daily_stats"."volume" DESC
LIMIT 10000