from pydub import AudioSegment as AS
import wave
import os, shutil

class FileConverter:
    def __init__(self, file, file_name, sub_folder):
        self.file = file
        self.file_name = file_name
        self.sub_folder = sub_folder
        # self.output = AS.from_wav(file=self.file)
        self.ouput_file_name = file_name
        
        pass

    def convert(self, file_dir, format, setting_array):
        
        format = format.replace('configs_', '')
        format = format.replace('_cbr', '')
        format = format.replace('_vbr', '')
        format_dic = {'aac': 'adts', 'aiff': 'aiff', 'flac': 'flac', 'mp3': 'mp3', 'ogg': 'ogg', 'wav': 'wav'}
        self.format = format_dic[format]

        self.channel = setting_array[3]
        self.frame_rate = setting_array[1]
        self.setting_array = setting_array
        
        AS.from_wav(file=file_dir).export(self.get_file_name(self.ouput_file_name), 
                                          format=self.format,
                                          parameters=setting_array)

        


    # ======================================================================================================
    # ===============================================get file names=========================================
    # ======================================================================================================
    def get_file_name(self, file):
        final_file_name = self.file_name.replace('wav', self.format)

        dir = 'C:/Users/user/Python Projects/audio file converter/converted dataset/' \
             + self.sub_folder
        if not os.path.exists(dir):
             os.mkdir(dir)

        dir = 'C:/Users/user/Python Projects/audio file converter/converted dataset/' \
             + self.sub_folder + '/' + self.format 
        if not os.path.exists(dir):
             os.mkdir(dir)

        # sample_width = self.sample_width * 8
        if self.channel == '1' or self.channel == '1.0':
            channel = 'mono'
        else:
            channel = 'stereo'

        dir = 'C:/Users/user/Python Projects/audio file converter/converted dataset/' \
            + self.sub_folder + '/' + self.format + '/' + self.format + '-' + str(self.frame_rate) + 'HZ' \
                  + '-' + channel + '-' + self.setting_array[4] + '_' + str(self.setting_array[5])
        if not os.path.exists(dir):
            os.mkdir(dir)

        return 'C:/Users/user/Python Projects/audio file converter/converted dataset/' \
            + self.sub_folder + '/' + self.format + '/' + self.format + '-' + str(self.frame_rate) + 'HZ' \
                  + '-' + channel + '-' + self.setting_array[4] + '_' + str(self.setting_array[5]) \
                      + '/' + final_file_name
    
    