class Friend:
    def __init__(self, name): 
        self.invite = 'No party...'
    def get_invite(self, invite):
        self.invite = invite
    def show_invite(self):
        return self.invite        


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []
    def add_friend(self, friend):
        self.friends.append(friend)
    def del_friend(self, friend):
        self.friends.remove(friend)
    def send_invites(self, invite):
        for friend in self.friends:
            friend.get_invite(f'{self.place}: {invite}')                


party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
chuck.show_invite() == "No party..."    