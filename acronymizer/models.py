from django.db import models
from django.utils import timezone

# The longest word in Spanish is "Electroencefalografista" with 23 characters
class Submission(models.Model):
    status_choices = {
        'P': 'Pending',
        'A': 'Approved',
        'R': 'Rejected'
    }

    word = models.CharField(max_length=25)
    sent_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=status_choices, default='P') 
    updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}: {} / status: [{}], created: {}, last update: {}'.format(
            self.word,
            self.definition(),
            self.status,
            self.sent_date.strftime('%Y-%m-%d %H:%M:%S'),
            self.updated_date.strftime('%Y-%m-%d %H:%M:%S') if self.updated_date else '-'
        )
    
    def definition(self):
        return ' '.join(map(str, sorted(self.acronymtoken_set.all(), key=lambda token: token.order)))

    def perfect(self):
        return all(token.perfect() for token in self.acronymtoken_set.all())


class AcronymToken(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

    # Prepositions/conjunctions *may* optionally be part of the acronym
    prepositions_and_conjunctions = ('a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre',
                                     'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras',
                                     'y', 'o', 'e', 'u')
    # Sort the allowed words to make them easier to search in the admin interface
    prepositions_and_conjunctions_choices = {
        preposition_or_conjunction: 
        preposition_or_conjunction for preposition_or_conjunction in sorted(prepositions_and_conjunctions)
    }
    preposition_or_conjunction = models.CharField(max_length=8, choices=prepositions_and_conjunctions_choices, null=True, blank=True)

    token = models.CharField(max_length=25)
    order = models.IntegerField()

    def perfect(self):
        return self.preposition_or_conjunction is None

    def __str__(self):
        return ("({}) ".format(self.preposition_or_conjunction) if self.preposition_or_conjunction else '') + self.token
               


