import sqlite3

class contestDB:
  def createDB():
    sqlite_file = '/home/swaite/radio/testdb'
    
    conn = sqlite3.connect(sqlite_file)

    #create the tables
    #qsotable is for data on a contact
    qsoTable = 'qso_table'
    #contestTable is for contest meta
    contestTable = 'contest_table'
    
    c = conn.cursor()

    c.execute("CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
      .format(tn=qsoTable, nf='qso_id', ft='INTEGER'))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='their_call', ct='TEXT'))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='operator', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='frequency', ct='REAL'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='band', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='mode', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=qsoTable, cn='exchange', ct='TEXT'))
    
    c.execute("CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
      .format(tn=contestTable, nf='callsign', ft='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=contestTable, cn='club', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=contestTable, cn='contest', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=contestTable, cn='soapbox', ct='BLOB'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=contestTable, cn='category', ct='TEXT'))

    conn.commit()
    conn.close()
