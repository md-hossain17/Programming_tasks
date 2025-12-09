# emperor_traveler.py
import os
import codecs
import time

class EmperorTraveler:
    def __init__(self):
        self.locations = {
            0: "Home",
            1: "Galba's palace",
            2: "Otho's palace",
            3: "Vitellius' palace",
            4: "Vespasian's palace"
        }
        self.progress_file = "player_progress.txt"
        self.initialize_system()
    
    def initialize_system(self):
        """Initialize all necessary files"""
        if not os.path.exists(self.progress_file):
            with open(self.progress_file, 'w') as f:
                f.write("current_location;next_location;passphrase\n")
                f.write("0;1;qvfpvcyvar\n")
    
    def rot13(self, text):
        """ROT13 decryption/encryption"""
        return codecs.encode(text, 'rot_13')
    
    def get_current_progress(self):
        """Read and return current progress"""
        if not os.path.exists(self.progress_file):
            return 0, 1, "qvfpvcyvar"
        
        with open(self.progress_file, 'r') as f:
            lines = f.readlines()
        
        if len(lines) < 2:
            return 0, 1, "qvfpvcyvar"
        
        # Get last data line
        last_line = lines[-1].strip()
        if ";" in last_line:
            parts = last_line.split(';')
            if len(parts) >= 3:
                return int(parts[0]), int(parts[1]), parts[2]
        
        return 0, 1, "qvfpvcyvar"
    
    def travel_animation(self, from_loc, to_loc):
        """Show travel animation"""
        from_name = self.locations[from_loc]
        to_name = self.locations[to_loc]
        
        print(f"\n📍 Currently at: {from_name}")
        print("🚶 Preparing to travel...")
        time.sleep(1)
        
        print(f"\n🗺️  Route: {from_name} → {to_name}")
        print("🛣️  Traveling ", end="", flush=True)
        
        # Simple travel animation
        for _ in range(5):
            print(".", end="", flush=True)
            time.sleep(0.5)
        
        print(f"\n🏰 Arrived at: {to_name}")
        time.sleep(1)
    
    def enter_palace(self, location_id, encrypted_pass):
        """Process palace entry"""
        plain_pass = self.rot13(encrypted_pass)
        
        print(f"\n🏛️  Approaching {self.locations[location_id]}")
        print("⚔️  Guard stands at the entrance...")
        time.sleep(1)
        
        print(f'🗣️  You shout: "{plain_pass.upper()}!"')
        print("✅ Guard nods and lets you pass")
        time.sleep(1)
        
        return plain_pass
    
    def find_message(self, location_id, encrypted_pass):
        """Find and decrypt message"""
        encrypted_file = f"{location_id}_{encrypted_pass}.gkg"
        
        if not os.path.exists(encrypted_file):
            print(f"❌ Could not find message file: {encrypted_file}")
            return None
        
        print(f"\n🔍 Searching for message...")
        print(f"📄 Found: {encrypted_file}")
        time.sleep(1)
        
        with open(encrypted_file, 'r') as f:
            encrypted_msg = f.read()
        
        print("🔓 Decrypting with ROT13...")
        time.sleep(1)
        
        plain_msg = self.rot13(encrypted_msg)
        
        # Save plain version
        plain_pass = self.rot13(encrypted_pass)
        plain_file = f"{location_id}-{plain_pass}.txt"
        
        with open(plain_file, 'w') as f:
            f.write(plain_msg)
        
        print(f"💾 Saved plain text: {plain_file}")
        
        return plain_msg
    
    def update_progress(self, current, next_loc, next_pass):
        """Update progress file"""
        with open(self.progress_file, 'a') as f:
            f.write(f"{current};{next_loc};{next_pass}\n")
        
        print("\n💾 [Game] Progress saved!")
    
    def display_message_preview(self, message):
        """Show message preview"""
        if message:
            lines = message.strip().split('\n')
            if lines:
                print(f"\n📜 Message from the Emperor:")
                print("-" * 50)
                print(lines[0])
                if len(lines) > 1:
                    print("...")
                print("-" * 50)
    
    def get_next_passphrase(self, next_loc):
        """Get passphrase for next location"""
        passphrases = {
            2: "gbur_ynfg",
            3: "ivgryyvhf_qbbe",
            4: "irfcnfvna_fgngr"
        }
        return passphrases.get(next_loc, "")
    
    def run(self):
        """Main program loop"""
        print("=" * 60)
        print("🏛️  YEAR OF THE FOUR EMPERORS 🏛️")
        print("=" * 60)
        print("Travel through Roman history in 69 AD")
        print("=" * 60)
        
        # Get current progress
        current, next_loc, passphrase = self.get_current_progress()
        
        # Check if completed
        if current >= 4:
            print("\n🎉 All palaces visited!")
            print("📚 Historical record complete.")
            return
        
        print("\n🚀 Travel starting...")
        
        # Travel to location
        self.travel_animation(current, next_loc)
        
        # Enter palace
        plain_pass = self.enter_palace(next_loc, passphrase)
        
        # Find and decrypt message
        message = self.find_message(next_loc, passphrase)
        
        if message:
            self.display_message_preview(message)
            
            # Prepare for next location
            new_current = next_loc
            new_next = next_loc + 1
            next_pass = self.get_next_passphrase(new_next)
            
            if next_pass:
                self.update_progress(new_current, new_next, next_pass)
            else:
                print("\n🏁 Journey complete!")
        
        print("\n👋 Time to leave...")
        
        if next_loc < 4:
            next_name = self.locations[next_loc + 1]
            print(f"\n➡️  Next destination: {next_name}")
        
        print("\n🏁 Travel ending.")

def create_test_files():
    """Create test message files"""
    messages = {
        "1_qvfpvcyvar.gkg": """Part 1 - Year of the Four Emperors:

In AD 68, after Nero's death, Rome plunged into chaos.
With no clear heir, the empire saw rapid power struggles.
Galba took the throne first, followed by Otho, Vitellius, and finally Vespasian,
each battling for control in what became the Year of the Four Emperors.""",
        
        "2_gbur_ynfg.gkg": """Otho's legacy:
Otho ruled for only three months,
but his story is one of ambition and tragedy.
He seized power after Galba's downfall,
only to face Vitellius' advancing armies.""",
        
        "3_ivgryyvhf_qbbe.gkg": """Vitellius' reign:
Vitellius was proclaimed emperor by his legions.
His rule was marked by excess and indulgence,
while his rivals gathered strength.
In the end, his reign was brief but memorable.""",
        
        "4_irfcnfvna_fgngr.gkg": """Vespasian's victory:
Vespasian emerged victorious from the civil war.
He founded the Flavian dynasty,
restored stability to Rome,
and began construction of the Colosseum.
His rule ended the Year of the Four Emperors."""
    }
    
    # Encrypt and save files
    for filename, plaintext in messages.items():
        encrypted = codecs.encode(plaintext, 'rot_13')
        with open(filename, 'w') as f:
            f.write(encrypted)
        print(f"Created: {filename}")

if __name__ == "__main__":
    # Create test files
    create_test_files()
    
    # Run the traveler
    traveler = EmperorTraveler()
    traveler.run()