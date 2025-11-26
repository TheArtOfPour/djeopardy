from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200, default="")
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    question1 = models.ForeignKey(Question, related_name='category_question1', on_delete=models.CASCADE)
    question2 = models.ForeignKey(Question, related_name='category_question2', on_delete=models.CASCADE)
    question3 = models.ForeignKey(Question, related_name='category_question3', on_delete=models.CASCADE)
    question4 = models.ForeignKey(Question, related_name='category_question4', on_delete=models.CASCADE)
    question5 = models.ForeignKey(Question, related_name='category_question5', on_delete=models.CASCADE)

    def __str__(self):
        return self.name