from src.data_preparation import read_and_clean_data, merge_data
from src.analysis import analyze_data
from src.visualization import plot_color_behavior, plot_heatmap
from src.report_generation import generate_report

def main():
    # Read and clean data
    lab_measurements, master_color_card = read_and_clean_data()
    merged_data = merge_data(lab_measurements, master_color_card)

    # Analyze data
    analyzed_data = analyze_data(merged_data)

    # Visualize data
    plot_color_behavior(analyzed_data, 'L11', 'L', 'Measured vs Intended L Values', 'Measured L', 'Intended L', 'output/color_behavior_L_plot.png')
    plot_heatmap(analyzed_data, 'Row', 'Column', 'Delta_E', 'ΔE Values Across Different Targets', 'output/delta_e_values_plot.png')

    # Generate report
    generate_report('output/Color_Card_Analysis_Report.pdf')

if __name__ == "__main__":
    main()
