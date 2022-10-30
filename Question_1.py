class DataStream():
    def __init__(self):
        self.dict_={}

    def should_output_data_str(self,timestamp,data_string):
            if self.dict_.get(data_string) is None:
                self.dict_[data_string]=timestamp
                return True
            else:
                if self.dict_[data_string]<=timestamp-5:
                    self.dict_[data_string]=timestamp
                    return True
                else:
                    return False


data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string='hello'))
print(data_stream.should_output_data_str(timestamp=1, data_string='world'))
print(data_stream.should_output_data_str(timestamp=6, data_string='hello'))
print(data_stream.should_output_data_str(timestamp=7, data_string='hello'))
print(data_stream.should_output_data_str(timestamp=8, data_string='world'))
