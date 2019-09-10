import argparse

def take_action( parsed_args):
    if not parsed_args.init_saved_state:
        print ("Run  self._cleanup() ")
    else :
        print ("Don't run  self._cleanup() ")
            
def callingMethod():
    parser = argparse.ArgumentParser()
    parser.add_argument("init_saved_state")
    parsed_args = parser.parse_args()
    take_action(parsed_args)
        
callingMethod()
