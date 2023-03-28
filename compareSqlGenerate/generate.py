import re


typeSet = set()
compareSqlTemplate = "select '%s' as table, f.db, f.cc  from (select 'oracle' as db, count(1) as cc from lion_dw_tmp.activiti_pro_%s where dt = '2023-03-26' union select 'mysql' as db, count(1) as cc from lion_dw_test.activiti_core_%s where dt = '2023-03-26') f "
# compareSqlTemplate = "select '%s', count(1) as diff from ( select %s from ( select * from lion_dw_tmp.activiti_pro_%s where dt = '2023-03-26') f left join ( select * from lion_dw_test.activiti_core_%s where dt = '2023-03-26') ff on %s) filter where %s"
caseTemplate = " case coalesce(f.%s, %s) when coalesce(ff.%s, %s) then 'true' else 'false' end as %s "
whereTemplate = " filter.%s = 'false' "
primaryKeyTemplate = " f.%s = ff.%s "

def getDefault(columnType):
    if columnType.lower() in ('datetime', 'timestamp'):
        return '\'2022-01-01 00:00:00.100\''
    elif columnType.lower() in ('bigint', 'tinyint', 'int', 'decimal', 'double'):
        return -1
    else:
        return '\'-\''

def getColumnMap(fileName):
    columnMap = {}
    with open(fileName, 'r', encoding='UTF-8-sig') as inp:
        for line in inp:
            ss = line.strip().split(',')
            tableName, columnName, columnType = ss[0], ss[1], ss[2]
            typeSet.add(columnType)
            if tableName in columnMap.keys():
                columnMap[tableName][columnName] = columnType
            else:
                columnMap[tableName] = {columnName: columnType}
    
    return columnMap

def getPrimaryKeyMap(fileName):
    primaryKeyMap = {}
    with open(fileName, 'r') as inp:
        for line in inp:
            tableName = re.findall('create table `.*?`', line.strip().lower())[0][13:]
            tableName = tableName[1 : len(tableName) - 1]
            primaryKey = re.findall('primary key \(`.*?`\)', line.strip().lower())[0][12:]
            primaryKeyMap[tableName] = primaryKey[2 : len(primaryKey) - 2].replace('`', '').split(',')
    return primaryKeyMap

def getStingTable(fileName):
    tables = []
    with open(fileName, 'r') as inp:
        for line in inp:
            tables.append(line.strip().split(' ')[0])
    
    return tables

if __name__ == '__main__':
    columnMap = getColumnMap('center-activiti-all-columns.csv')
    primaryKeyMap = getPrimaryKeyMap('activiti_core.sql')
    tables = getStingTable('stingTable')
    

    for tableName in columnMap:
        casePart = []
        wherePart = []
        for columnName in columnMap[tableName]:
            columnType = columnMap[tableName][columnName]
            if columnType.lower() not in ('datetime', 'timestamp'):
                casePart.append(caseTemplate % (columnName, getDefault(columnType), columnName, getDefault(columnType), columnName))
                wherePart.append(whereTemplate % (columnName))
        
        primaryKeyPart = []
        for key in primaryKeyMap[tableName]:
            primaryKeyPart.append(primaryKeyTemplate % (key, key))
        
        if tableName.upper() in tables:
            print(compareSqlTemplate % (tableName, tableName, tableName))
            # print(compareSqlTemplate % (tableName, ','.join(casePart), tableName, tableName, 'and'.join(primaryKeyPart), 'or'.join(wherePart)))
            print('union')

