import numpy as np

def crop_and_concat(encoder_features: np.ndarray, decoder_features: np.ndarray) -> np.ndarray:
    """
    Crop encoder features to match decoder spatial dims, then concatenate along channels.
    """
    # Your implementation 
    if(encoder_features.shape[1]!=decoder_features.shape[1]):
        crop_dist_x = (encoder_features.shape[1] - decoder_features.shape[1])//2
        crop_dist_y = (encoder_features.shape[2] - decoder_features.shape[2])//2
        cropped_encoder = encoder_features[:,crop_dist_x:decoder_features.shape[1]+crop_dist_x,crop_dist_y:decoder_features.shape[2]+crop_dist_y,:]
        final_arr = np.concatenate((cropped_encoder,decoder_features),axis=-1)
    else:
        final_arr = np.concatenate((encoder_features,decoder_features),axis=-1)
    return final_arr