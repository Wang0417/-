    id=request.form.get("student_id")
    name=request.form.get("name")
    major=request.form.get("major")
    sql=f"""
    insert into user(id,name,major)
    values ({id},'{name}','{major}')
    """
    print(sql)