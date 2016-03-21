import sqlite3

class contestDB:
  sqlite_file = ''
  qsoTable = ''
  contestTable = ''

  def __init__(self):
    self.sqlite_file = '/home/swaite/radio/testdb'
    #qsotable is for data on a contact
    self.qsoTable = 'qso_table'
    #contestTable is for contest meta
    self.contestTable = 'contest_table'

  def createDB(self):

    conn = sqlite3.connect(self.sqlite_file)

    #create the tables
    
    c = conn.cursor()

    c.execute("CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
      .format(tn=self.qsoTable, nf='qso_id', ft='INTEGER'))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='their_call', ct='TEXT'))

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='operator', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='frequency', ct='REAL'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='band', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='mode', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.qsoTable, cn='exchange', ct='TEXT'))
    
    c.execute("CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
      .format(tn=self.contestTable, nf='callsign', ft='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.contestTable, cn='club', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.contestTable, cn='contest', ct='TEXT'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.contestTable, cn='soapbox', ct='BLOB'))
    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
      .format(tn=self.contestTable, cn='category', ct='TEXT'))

    conn.commit()
    conn.close()

  def addQSO(self, their_call, operator, frequency, band, mode, exchange):
    print "nope"
    conn = sqlite3.connect(self.sqlite_file)
    
    c = conn.cursor()

    c.execute("INSERT INTO {tn} (qso_id, their_call, operator, frequency, \
      band, mode, exchange) VALUES(3, {them}, {me}, {freq}, {band}, {mode},\
      {exch})".format(tn=self.qsoTable,them=their_call, me=operator, freq=frequency, \
      band=band, mode=mode, exch=exchange))

    conn.commit()
    conn.close()  
