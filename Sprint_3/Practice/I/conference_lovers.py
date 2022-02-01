from functools import cmp_to_key


class ConferenceParticipants:
    def __init__(self):
        self.index = dict()
        self.participants = []

    @staticmethod
    def comparator(a, b):
        if a.get('count') > b.get('count'):
            return 1

        if a.get('count') < b.get('count'):
            return -1

        if a.get('id') > b.get('id'):
            return -1

        if a.get('id') < b.get('id'):
            return 1

        return 0

    def get_top(self, top_participants):
        top = sorted(self.participants, key=cmp_to_key(ConferenceParticipants.comparator), reverse=True)[
              :top_participants]

        return [str(p.get('id')) for p in top]

    def add(self, p_id):
        if self.index.get(p_id) is None:
            self.participants.append({'id': p_id, 'count': 1})
            self.index[p_id] = len(self.participants) - 1
        else:
            self.participants[self.index.get(p_id)]['count'] += 1


def main():
    n = int(input())
    IDs = list(map(int, input().strip().split()))[:n]
    top_participants = int(input())

    participants = ConferenceParticipants()

    for participant_id in IDs:
        participants.add(participant_id)

    print(' '.join(participants.get_top(top_participants)))


if __name__ == '__main__':
    main()
