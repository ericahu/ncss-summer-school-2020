import random, re, yaml

class Pun_Selector():

    def __init__(self):
        self.puns = []
        self.similarity_score = {}

    def input(self, filename=r'app/puns.yml'):
        with open(filename) as file:
            puns_list = yaml.full_load(file)
            for pun in puns_list:
                pun['Topics'] = pun['Topics'].replace(' ','').split(',') if 'Topics' in pun else []
                pun['Owner'] = pun['Owner'].replace(' ','').split(',') if 'Owner' in pun else []
                pun['Unique Words'] = self._get_unique_words(pun['Description'])
            self.puns = puns_list

    def print(self):
        for pun in self.puns:
            print(f'Description  - {pun["Description"]}')
            print(f'Topics       - {", ".join(pun["Topics"])}')
            print(f'Unique Words - {", ".join(pun["Unique Words"])}')
            print()

    def random_choice(self):
        return random.choice(self.puns)

    def show_similarity(self):
        print(self.similarity_score)

    def _get_unique_words(self, text):
        stripped_text = re.sub('[^a-zA-Z0-9\s\n]', '', text).lower()
        text_list = stripped_text.split(' ')
        return set(text_list)

    def generate(self, user_input):
        similarity_score = {}
        unique_user_words = self._get_unique_words(user_input)
        for p in self.puns:
            common_words = unique_user_words.intersection(p['Unique Words'])
            self.similarity_score[p] = len(common_words)

        # print(self.puns['Unique Words'])
        # print(unique_user_words)
        # common_words = unique_user_words.intersection(self.puns['Unique Words'])
        # return 0

    # def calculate_common_words(self, user_input):
    #     unique_user_words = set(user_input)



    # def select(self, topic=''):
    #     pun_pool = [pun if topic  for pun in puns]

# p = Pun_Selector()
# p.input()
# (print(p.random_choice()))
