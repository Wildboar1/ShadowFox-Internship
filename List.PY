Justice_League = ["Superman","Batman","Wonder Woman","Flash","Aquaman", "Green Lantern"]
print(f"Initial Justice League = {Justice_League}")
num_memebers = len(Justice_League)
print(f"\n1. Number of memebers = {num_memebers}")

Justice_League.append("Batgirl")
Justice_League.append("NightWing")
print(f"\n2. After recuitment = {Justice_League}")

Justice_League.remove("Wonder Woman")
Justice_League.insert(0, "Wonder Woman")
print(f"\n3. Wonder is the new leader = {Justice_League}")

member_to_move = "Green Lantern"
memeber_index = Justice_League.index(member_to_move)

Justice_League.pop(memeber_index)
Justice_League.insert(5, member_to_move)

print(f"\n4. After seperating Aquaman and Flash with {member_to_move} = {Justice_League}")

new_memebr = ["Cyborg", "Shazam" , "Hawkgirl","Martian MAnhuntert"]
Justice_League = new_memebr
print(f"\n5. new assemble team = {Justice_League}")
Justice_League.sort()
new_leader=Justice_League[0]

print(f"\n6. Alphabetically sorted Justice League = {Justice_League}")
print(f"Bonus = The new leader (0 index) will be = {new_leader}")