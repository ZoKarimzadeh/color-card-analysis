import pandas as pd
import os

def read_and_clean_data():
    lab_measurements_path = 'data/LabMeasurements-Color-Card.csv'
    master_color_card_path = 'data/MasterColorCard.csv'

    if not os.path.exists(lab_measurements_path):
        raise FileNotFoundError(f"{lab_measurements_path} does not exist.")
    if not os.path.exists(master_color_card_path):
        raise FileNotFoundError(f"{master_color_card_path} does not exist.")

    lab_measurements = pd.read_csv(lab_measurements_path, sep=';', decimal=',')
    master_color_card = pd.read_csv(master_color_card_path, sep=';', decimal=',')
    return lab_measurements, master_color_card

def merge_data(lab_measurements, master_color_card):
    # Create a combined 'Field' column in lab_measurements to match with 'Field' in master_color_card
    lab_measurements['Field'] = lab_measurements['Row'].astype(str) + lab_measurements['Column'].astype(str)
    
    # Ensure both 'Field' columns are of the same type (string)
    lab_measurements['Field'] = lab_measurements['Field'].astype(str)
    master_color_card['Field'] = master_color_card['Field'].astype(str)
    
    merged_data = pd.merge(lab_measurements, master_color_card, on='Field')
    return merged_data
