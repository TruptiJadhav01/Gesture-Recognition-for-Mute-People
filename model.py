
# coding: utf-8

# In[1]:


import numpy as np
from keras.layers import Conv2D, Dense, Flatten, Dropout, MaxPooling2D
from keras.models import Sequential, save_model
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import os
import cv2


# In[2]:


path = 'preprocessed_new/'


# In[3]:


gestures = os.listdir(path)


# In[4]:


dict_labels = {
    'A': 1,
    'B': 2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'K':10,
    'L':11,
    'M':12,
    'N':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    
}


# In[5]:


print(list(dict_labels.keys()))


# In[6]:


x, y = [], []
for ix in gestures:
    images = os.listdir(path + ix)
    for cx in images:
        img_path = path + ix + '/' + cx
        img = cv2.imread(img_path, 0)
        img = img.reshape((50,50,1))
        img = img/255.0
        x.append(img)
        y.append(dict_labels[ix])


# In[7]:


X = np.array(x)
Y = np.array(y)
Y = np_utils.to_categorical(Y)
Y.shape


# In[29]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[30]:


plt.figure(figsize = (18,8))
sns.countplot(x=list(dict_labels.keys()))


# In[33]:


Y.shape


# In[34]:


categories = Y.shape[1]


# In[35]:


X, Y = shuffle(X, Y, random_state=0)


# In[36]:


X.shape


# In[95]:


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)


# In[96]:


print(X_train.shape, X_test.shape)
print(Y_train.shape, Y_test.shape)


# In[97]:


model = Sequential()
model.add(Conv2D(64, kernel_size=(3,3), activation = 'relu', input_shape=(50,50 ,1) ))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(128, activation = 'relu'))
model.add(Dropout(0.20))
model.add(Dense(categories, activation = 'softmax'))

model.summary()


# In[98]:


model.compile(optimizer='Adam', metrics=['accuracy'], loss='categorical_crossentropy')


# In[99]:


history = model.fit(X_train, Y_train, batch_size=128, epochs=50, validation_data=[X_test, Y_test])


# In[100]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[101]:


plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title("Accuracy")
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['train','test'])
plt.show()


# In[102]:


model.save('./new_model7.h5')


# In[31]:


from keras.models import load_model


# In[32]:


m = load_model('./new_model7.h5')


# In[33]:


test_data = os.listdir('./test_data/')


# In[34]:


x, y = [], []
for ix in test_data:
    images = os.listdir('./test_data/' + ix)
    for cx in range(1,201):
        img_path = './test_data/' + ix + '/' + str(cx) + '.jpg'
        img = cv2.imread(img_path, 0)
        img = img.reshape((50,50,1))
        img = img/255.0
        x.append(img)
        y.append(dict_labels[ix])


# In[35]:


X_t = np.array(x)
y_t = np.array(y)
Y_t = np_utils.to_categorical(y_t)


# In[36]:


X_t.shape


# In[37]:


y_pred = m.predict(X_t)


# In[38]:


from sklearn.metrics import accuracy_score


# In[39]:


accuracy_score(Y_t, y_pred.round())


# In[40]:


from sklearn.metrics import classification_report, confusion_matrix


# In[41]:


print(classification_report(y_pred.round(), Y_t))

