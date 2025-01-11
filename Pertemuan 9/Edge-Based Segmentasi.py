import cv2 
Image = cv2.imread('20bf4531-e499-425e-be66-5dd2a3bb9869.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(Image, 100, 200)
cv2.imshow('Edges Detected', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()