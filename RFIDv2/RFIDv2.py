import csv, serial,time

arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(1)
passenger_database = [['52 F6 E1 1C','Ayush','100'],['91 C3 BD 08','Shounak','100'],['A9 9C 2E 5A','Vishwesh','100'],['2E B3 54 D3','Soham','50']]
current_passengers = []
#f=open('Book1.csv','r+')
#csv_f=csv.reader(f)
def bus_recieve():
	while arduino.in_waiting:
		bus_stop=arduino.readline().strip().decode('utf-8')
	str(bus_stop)
	print(bus_stop)
def search_pass(dat):
	flag=0
	for x in current_passengers:
		if dat == x:
			flag = 1
	return flag
def fetch_pass(data):
	flag=0
	for records in passenger_database:
		if(records[0]==data and int(records[2])>75):
			flag=1
			print(records)
	return flag
def Recieve_entry():
	data = ''
	while (arduino.in_waiting>0):
		data = arduino.readline().strip().decode('utf-8')
		stat=int(data[0])
		str(data)
		data=data[2:]
		#print(data)
		if stat == 0:
			if(search_pass(data)==0):
				current_passengers.append(data)
			else:
				current_passengers.remove(data)
			print("Passengers in the bus")
			print(current_passengers)
		elif stat== 1:
			if(search_pass(data)):
				current_passengers.remove(data)
			else:
				current_passengers.append(data)
			print("Passengers in the bus")
			print(current_passengers)
	approval=fetch_pass(data)
	if(approval == 0 and data!=''):
		print("Access denied to current user")
		current_passengers.remove(data)
		print(current_passengers)
		
while True:
	Recieve_entry()
print(current_passengers)

# #include <SPI.h>
# #include <MFRC522.h>

# #define RST_PIN         9          // Configurable, see typical pin layout above
# #define SS_1_PIN        10         // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 2
# #define SS_2_PIN        8          // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 1

# #define NR_OF_READERS   2

# byte ssPins[] = {SS_1_PIN, SS_2_PIN};

# MFRC522 mfrc522[NR_OF_READERS];   // Create MFRC522 instance.

# void setup() {

  # Serial.begin(9600); // Initialize serial communications with the PC
  # while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  # SPI.begin();        // Init SPI bus

  # for (uint8_t reader = 0; reader < NR_OF_READERS; reader++) {
    # mfrc522[reader].PCD_Init(ssPins[reader], RST_PIN); // Init each MFRC522 card
    # Serial.print(F("Reader "));
    # Serial.print(reader);
    # Serial.print(F(": "));
    # mfrc522[reader].PCD_DumpVersionToSerial();
  # }
# }


# void loop() {

  # for (uint8_t reader = 0; reader < NR_OF_READERS; reader++) {
   
    # // Look for new cards
    # if (mfrc522[reader].PICC_IsNewCardPresent() && mfrc522[reader].PICC_ReadCardSerial()) {
      
      # Serial.print(reader);
      # dump_byte_array(mfrc522[reader].uid.uidByte, mfrc522[reader].uid.size);
      # Serial.println();
      
      # // Halt PICC
      # mfrc522[reader].PICC_HaltA();
      # // Stop encryption on PCD
      # mfrc522[reader].PCD_StopCrypto1();
    # } 
  # } 
# }

# void dump_byte_array(byte *buffer, byte bufferSize) {
  # for (byte i = 0; i < bufferSize; i++) {
    # Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    # Serial.print(buffer[i], HEX);
  # }
# }