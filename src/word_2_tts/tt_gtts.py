from gtts import gTTS
from tkinter import Frame, Button, Tk, Text, Label
from tomorrow import threads



class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #
        self.tans_word_enter = Text(self)
        self.tans_word_enter["height"] = 20
        self.tans_word_enter["width"] = 90
        self.tans_word_enter.pack(side="top")
        self.pack(side="top")

        #
        self.label = Label(self)
        self.label["text"] = "等待转换指令"
        self.label["anchor"] = "w"
        self.label.pack(side="left")

        #
        self.tans_word_button = Button(self)
        self.tans_word_button["text"] = "转换为MP3"
        self.tans_word_button["command"] = self.tans_word_2_tts
        self.tans_word_button.pack(side="right")

    @threads(5)
    def tans_word_2_tts(self):
        self.label["text"] = "转换中"
        print()
        try:
            # "1.0" means that the input should be read from line one, character zero
            # (ie: the very first character). END is an imported constant which is set
            # to the string "end".
            #   -- from: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-box-widget
            #
            # Hope the author can make it more intuitive    ----t24kun
            Function.tans_tts(input_word=self.tans_word_enter.get(index1="1.0", index2="end"))
            self.label["text"] = "转换完成, 请在根目录下寻找output.mp3文件"
        except:
            self.label["text"] = "转换失败，请联系作者"
        from time import sleep
        sleep(5)
        self.label["text"] = "等待转换指令"


class Function:
    @staticmethod
    def tans_tts(input_word: str="", output_file_name: str="output"):
        output_file = gTTS(input_word)
        output_file.save(output_file_name + ".mp3")
        return True


if __name__ == '__main__':
    root = Tk("words_2_tts")
    app = Application(master=root)
    app.mainloop()
