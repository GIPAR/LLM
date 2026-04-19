class UserView:
    def choose_input_mode(self):
        mode = input("Digite 't' para texto ou 'f' para fala: ")
        return mode.lower()

    def get_text_command(self):
        return input("Digite o comando do robô: ")

    def show_feedback(self, msg):
        print(f"[ROBO]: {msg}")
