-- 1. user1= 7
-- select * from tasks_activity_log WHERE user_id=7;
-- SELECT * from tasks_user_log WHERE user_id=7;

-- 2. user2= 8
-- SELECT task_id,title,description, timeOf_action as time_of_deletion from tasks_activity_log where user_id=8 AND action= 'delete';

-- 3.
-- select id, first_name, last_name from auth_user where id IN
-- 	(SELECT user_id from tasks_user_log WHERE action='login' and timeOf_action BETWEEN '2024-08-06 14:00:00' AND '2024-08-06 15:00:00');

-- 4. user3=9
-- SELECT * from tasks_tasks WHERE user_id=9 LIMIT 1000 OFFSET 3 ;

-- 5.
select id, first_name, last_name, email from auth_user where id = (
	SELECT user_id from (
		select user_id, max(total_time) from (select user_id, sum(duration) as total_time from tasks_session_time GROUP by user_id)
		)
	);


SELECT tab2.user_id, tab1.first_name, tab1.last_name, tab1.email, max(tab2.total_session) as total_session_time from auth_user as tab1, (
	select user_id, first_name, last_name, sum(session_time) as total_session from auth_user as tab1, (
	select t1.user_id, (julianday(t2.logout_time)*24*60*60 - julianday(t1.login_time)*24*60*60 ) as session_time from
	(select ROW_NUMBER() OVER() AS row_id, user_id, timeOf_action as login_time from tasks_user_log where action='login' ORDER by user_id) as t1,
	(select ROW_NUMBER() OVER() AS row_id, user_id, timeOf_action as logout_time from tasks_user_log where action='logout' ORDER by user_id) as t2 
	WHERE t1.row_id=t2.row_id ORDER by t1.user_id
	)as tab2 where tab1.id=tab2.user_id  GROUP by user_id
) as tab2 WHERE tab1.id=tab2.user_id;





-- Helper queries
-- select user_id, sum(duration) as total_time from tasks_session_time GROUP by user_id;
-- select user_id, max(total_time) from (select user_id, sum(duration) as total_time from tasks_session_time GROUP by user_id);

-- select user_id, sum(session_time) as total_session from (
-- 	select t1.user_id, (julianday(t2.logout_time)*24*60*60 - julianday(t1.login_time)*24*60*60 ) as session_time from
-- 	(select ROW_NUMBER() OVER() AS row_id, user_id, timeOf_action as login_time from tasks_user_log where action='login' ORDER by user_id) as t1,
-- 	(select ROW_NUMBER() OVER() AS row_id, user_id, timeOf_action as logout_time from tasks_user_log where action='logout' ORDER by user_id) as t2 
-- 	WHERE t1.row_id=t2.row_id ORDER by t1.user_id
-- 	) GROUP by user_id;

