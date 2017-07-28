import psycopg2

# Below we set the 3 questions and the SQL queries to be run
questionOne = "What are the most popular three articles of all time?"

queryOne = ("select title, count(*) as num from articles "
            "join log on path like CONCAT('%',slug) group by title "
            "order by num desc limit 3")

questionTwo = "Who are the most popular article authors of all time?"

queryTwo = ("select name, count(path) as num from authors "
            "join articles on authors.id = author join log "
            "on path like CONCAT('%', slug) group by name order by num desc")

questionThree = "On which days did more than 1% of requests lead to errors?"

queryThree = ("select dte, dayavg from ("
              "select dte, (sum(dayerror) / (select count(*) "
              "from log where (time::date) = dte)) as dayavg "
              "from (select (time::date) as dte, count(*) as dayerror "
              "from log where status like '4%' group by dte) "
              "as error_perc group by dte order by dayavg  desc) as final "
              "where dayavg >= .01")


def openTable(x):
    """Opens news database and returns result of query x"""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(x)
    return c.fetchall()
    close()


def printResult(results, question):
    """Prints a formatted result of the queries counting views"""
    print (question)
    for result in results:
        print ("\t" + result[0] + " — " + str(result[1]) + ' views')


def printAltResult(results, question):
    """Prints a formatted result of the query with percentage error"""
    print (question)
    for result in results:
        print ('\t' + str(result[0]) + " — " + str(round((result[1]*100), 2)) +
               '%')

printResult(openTable(queryOne), questionOne)
printResult(openTable(queryTwo), questionTwo)
printAltResult(openTable(queryThree), questionThree)
