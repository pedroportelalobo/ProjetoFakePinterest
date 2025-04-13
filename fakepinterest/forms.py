from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario
from fakepinterest import bcrypt

class FormLogin(FlaskForm):
    email= StringField("E-mail:", validators=[DataRequired(), Email()])
    senha= PasswordField("Senha:",validators=[DataRequired()])
    botao_confirmacao= SubmitField("Fazer Login",)

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário inexistente, crie uma conta.")
        elif not bcrypt.check_password_hash(usuario.senha, self.senha.data):
            raise ValidationError("Senha incorreta, tente novamente.")


class FormCriarConta(FlaskForm):
    email= StringField("E-mail:", validators=[DataRequired(), Email()])
    username= StringField("Usuário:", validators=[DataRequired()])
    senha= PasswordField("Senha:", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha= PasswordField("Confirmação de senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao= SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado. Faça login para continuar")
    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError("Usuário já existente.")

class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
    pass
