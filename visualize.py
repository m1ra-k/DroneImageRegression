import cv2
import argparse

from arrow import calculate_endpoint


# Create the parser
parser = argparse.ArgumentParser(description="Process some inputs.")

# Add arguments
parser.add_argument('--datapath', type=str, default="./Data/", help="The path to the labels and data")
parser.add_argument('--filename', type=str, default="labels.csv", help="The name of the labels file")

# Parse arguments
args = parser.parse_args()

# Load the labels
labels_filename = '{}{}'.format(args.datapath, args.filename)
with open(labels_filename, 'r') as label_file:

    # Previous angle
    previous_angle = -999

    # For each line
    for line in label_file:

        # Get the data
        data = line.strip().split(" : ")
        x_size = 0

        # Save the data
        timestamp       = data[0]
        framenumber     = data[1]
        trial           = data[2]
        notsure         = data[3]
        orientation     = float(data[4])
        rotation        = 0

        # Compute steering angle
        if previous_angle == - 999:
            steering_angle = 0
        else:
            steering_angle = previous_angle - orientation
        previous_angle = orientation

        # Load the image
        img_path = '{}Screenshots/{}_{}.png'.format(args.datapath, trial, framenumber)

        # Read the image
        img = cv2.imread(img_path)
        
        # Add the global arrow
        GLOBAL_START       = [225, 100]
        GLOBAL_COLOR       = (0, 255, 255)
        GLOBAL_THICKNESS   = 3
        global_end         = calculate_endpoint(GLOBAL_START, 75, orientation)
        cv2.arrowedLine(img, GLOBAL_START, global_end, GLOBAL_COLOR, GLOBAL_THICKNESS, tipLength=0.3)

        # Add steering angle
        if x_size == 0:
            x_size = int(img.shape[1]/2)
        STEER_START       = [x_size, 500]
        STEER_COLOR       = (0, 0, 255)
        STEER_THICKNESS   = 4
        steer_end         = calculate_endpoint(STEER_START, 100, -steering_angle*3)
        cv2.arrowedLine(img, STEER_START, steer_end, STEER_COLOR, STEER_THICKNESS, tipLength=0.3)

        # Add the global labels
        FONT_SCALE      = 1
        FONT_COLOR      = (255, 255, 255)
        FONT_THICKNESS  = 2
        POSITION_NORTH  = (215, 25)
        POSITION_EAST   = (300, 110)
        POSITION_WEST   = (125, 110)
        POSITION_SOUTH  = (215, 200)
        cv2.putText(img, 'N', POSITION_NORTH, cv2.FONT_HERSHEY_SIMPLEX , FONT_SCALE, FONT_COLOR, FONT_THICKNESS, lineType=cv2.LINE_AA)
        cv2.putText(img, 'E', POSITION_EAST, cv2.FONT_HERSHEY_SIMPLEX , FONT_SCALE, FONT_COLOR, FONT_THICKNESS, lineType=cv2.LINE_AA)
        cv2.putText(img, 'W', POSITION_WEST, cv2.FONT_HERSHEY_SIMPLEX , FONT_SCALE, FONT_COLOR, FONT_THICKNESS, lineType=cv2.LINE_AA)
        cv2.putText(img, 'S', POSITION_SOUTH, cv2.FONT_HERSHEY_SIMPLEX , FONT_SCALE, FONT_COLOR, FONT_THICKNESS, lineType=cv2.LINE_AA)

        # Display the image
        cv2.imshow('Image', img)

        # Wait for a specified time (in milliseconds)
        cv2.waitKey(100)
    
    # Destroy the opencv windows
    cv2.destroyAllWindows()