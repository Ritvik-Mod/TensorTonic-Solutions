import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""

    data = np.array(data,dtype=np.float64)

    # element_wise = np.where(data>threshold)
    # element_wise_final = np.zeros(data.shape)
    # element_wise_final[element_wise] = data[element_wise]
    element_wise_final = np.where(data>threshold,1,0)

    row_any = np.any(data>threshold, axis=1)
    row_any_final = np.zeros(data.shape)
    row_any_final[row_any] = data[row_any]
    # r1 = np.where(row_any_final>threshold)
    # row_any_final[:,:] = 0
    # row_any_final[r1] = data[r1]
    
    row_all = np.all(data>threshold, axis = 1)
    row_all_final = np.zeros(data.shape)
    row_all_final[row_all] = data[row_all]
    # r2 = np.where(row_all_final>threshold)
    # row_all_final[:,:] = 0
    # row_all_final[r2] = data[r2]
    
    return np.array([element_wise_final,row_any_final,row_all_final])