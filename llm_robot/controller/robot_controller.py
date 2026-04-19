class RobotController:
    def __init__(self, llm_model, speech_model, view, robot):
        self.llm = llm_model
        self.speech = speech_model
        self.view = view
        self.robot = robot

    def run(self):
        mode = self.view.choose_input_mode()

        if mode == "f":
            text = self.speech.listen()
            self.view.show_feedback(f"Comando: {text}")
        else:
            text = self.view.get_text_command()

        command = self.llm.interpret(text)

        action = command["action"]

        if action == "forward":
            self.robot.move_forward()

        elif action == "rotate":
            self.robot.rotate()

        elif action == "stop":
            self.robot.stop()

