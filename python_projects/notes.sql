SELECT mj.etl_process_id, 
       mj.etl_process_start_time, 
       Ifnull(mj.etl_process_end_time, Now()) AS etl_process_end_time, 
       ROUND(TIME_TO_SEC(TIMEDIFF(Ifnull(mj.etl_process_end_time, Now()), mj.etl_process_start_time))/60) AS duration_mins,
       mj.etl_process_name                    etl_process_name, 
       mj.etl_process_status, 
       (SELECT Group_concat(Concat('Job: ', cj.etl_process_name, ', Start:', 
               cj.etl_process_start_time, 
               ', Finish:', cj.etl_process_end_time)) 
        FROM   titan.v_etl_load_runs cj 
        WHERE  cj.etl_process_id != mj.etl_process_id 
               AND ( ( mj.etl_process_start_time >= cj.etl_process_start_time 
                       AND mj.etl_process_start_time <= 
                     cj.etl_process_end_time ) 
                      OR ( mj.etl_process_end_time >= cj.etl_process_start_time 
                           AND mj.etl_process_end_time <= 
                               cj.etl_process_end_time ) 
                      OR ( mj.etl_process_start_time <= 
                           cj.etl_process_start_time 
                           AND mj.etl_process_end_time >= 
                               cj.etl_process_end_time ) )) 
                                              AS concurrent_jobs 
FROM   titan.v_etl_load_runs mj 
WHERE  Date(mj.etl_process_start_time) = '2018-09-11'
LIMIT 10;


    cursor.execute('SELECT mj.etl_process_id, \
                           mj.etl_process_start_time, \
                           Ifnull(mj.etl_process_end_time, Now()) AS etl_process_end_time, \
                           ROUND(TIME_TO_SEC(TIMEDIFF(Ifnull(mj.etl_process_end_time, Now()), mj.etl_process_start_time))/60) AS duration_mins,\
                           mj.etl_process_name                    etl_process_name, \
                           mj.etl_process_status, \
                           (SELECT Group_concat(Concat(\'Job: \', cj.etl_process_name, \', Start:\', \
                                   cj.etl_process_start_time, \
                                   \', Finish:\', cj.etl_process_end_time)) \
                            FROM   titan.v_etl_load_runs cj \
                            WHERE  cj.etl_process_id != mj.etl_process_id \
                                   AND ( ( mj.etl_process_start_time >= cj.etl_process_start_time \
                                           AND mj.etl_process_start_time <= \
                                         cj.etl_process_end_time ) \
                                          OR ( mj.etl_process_end_time >= cj.etl_process_start_time \
                                               AND mj.etl_process_end_time <= \
                                                   cj.etl_process_end_time ) \
                                          OR ( mj.etl_process_start_time <= \
                                               cj.etl_process_start_time \
                                               AND mj.etl_process_end_time >= \
                                                   cj.etl_process_end_time ) )) \
                                                                  AS concurrent_jobs \
                    FROM   titan.v_etl_load_runs mj \
                    WHERE  Date(mj.etl_process_start_time) = \'2018-09-11\'');

    rows = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] #this will extract row headers





