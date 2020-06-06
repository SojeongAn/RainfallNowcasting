import tensorflow as tf
import numpy as np
from matplotlib import colors
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['font.size'] = 20
plt.rcParams['lines.linewidth'] = 3

def plot_history(history, results, archi, nom_test, save=False, foldername=''):
  plt.figure(figsize=(12,6))
  plt.plot(history.history['loss'], label='Train')
  plt.plot(history.history['val_loss'], label='Val')
  plt.axhline(results['loss'], linestyle='--', color='k', label='Test')
  plt.ylabel('loss')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_loss.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['prec'], label='Train')
  plt.plot(history.history['val_prec'], label='Val')
  plt.axhline(results['prec'], linestyle='--', color='k', label='Test')
  plt.ylabel('prec')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_prec.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['recall'], label='Train')
  plt.plot(history.history['val_recall'], label='Val')
  plt.axhline(results['recall'], linestyle='--', color='k', label='Test')
  plt.ylabel('recall')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_recall.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['cor'], label='Train')
  plt.plot(history.history['val_cor'], label='Val')
  plt.axhline(results['cor'], linestyle='--', color='k', label='Test')
  plt.ylabel('cor')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_cor.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['acc'], label='Train')
  plt.plot(history.history['val_acc'], label='Val')
  plt.axhline(results['acc'], linestyle='--', color='k', label='Test')
  plt.ylabel('acc')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_acc.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['ssim'], label='Train')
  plt.plot(history.history['val_ssim'], label='Val')
  plt.axhline(results['ssim'], linestyle='--', color='k', label='Test')
  plt.ylabel('ssim')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_ssim.png')
    plt.close()
  #
  plt.figure(figsize=(12,6))
  plt.plot(history.history['psnr'], label='Train')
  plt.plot(history.history['val_psnr'], label='Val')
  plt.axhline(results['psnr'], linestyle='--', color='k', label='Test')
  plt.ylabel('psnr')
  plt.xlabel('epoch')
  plt.legend(loc='upper left')
  if save == True:
    plt.savefig(foldername+archi+'_'+nom_test+'_psnr.png')
    plt.close()


##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################


def plot_track(true_track, track, threshold_value, new_size, Ninput, Noutput,
               lat, lon, archi, nom_test, tag, save=False, foldername=''):
  #
  if len(new_size) > 0:
          lat = tf.image.resize(lat[:,:,None], new_size)
          lat = np.asarray(lat)[:,:,0]
          lon = tf.image.resize(lon[:,:,None], new_size)
          lon = np.asarray(lon)[:,:,0]
  #
  cmap = colors.ListedColormap(['silver','white', 'darkslateblue', 'mediumblue','dodgerblue',
                              'skyblue','olive','mediumseagreen','cyan','lime','yellow',
                              'khaki','burlywood','orange','brown','pink','red','plum'])
  bounds = [-1,0,2,4,6,8,10,15,20,25,30,35,40,45,50,55,60,65,75]
  norm = colors.BoundaryNorm(bounds, cmap.N)
  #
  track = track*threshold_value
  true_track = true_track*threshold_value
  #
  for i in range(Ninput+Noutput):
      plt.figure(figsize=(15, 8))
      plt.subplot(121)
      if i >= Ninput:
          plt.text(-5.7, 46.4, 'Prediction', color='k')
      else:
          plt.text(-5.7, 46.4, 'Initial trajectory', color='k')
      plt.pcolormesh(lon, lat, track[0, i, :, :, 0], cmap=cmap, norm=norm)
      plt.xlabel('$x$ [$^{\circ}E$]')
      plt.ylabel('$y$ [$^{\circ}N$]')
      plt.subplot(122)
      plt.text(-5.7, 46.4, 'Ground truth', color='k')
      plt.pcolormesh(lon, lat, true_track[i, :, :, 0], cmap=cmap, norm=norm)
      plt.xlabel('$x$ [$^{\circ}E$]')
      plt.ylabel('$y$ [$^{\circ}N$]')
      cbar = plt.colorbar(cmap=cmap, norm=norm, boundaries=bounds, ticks=bounds,
                orientation= 'vertical').set_label('Rainfall [1/100 mm]')
      if save == True:
          plt.savefig(foldername+archi+'_'+nom_test+'_'+tag+'_%i.png' % (i+1))
          plt.close()
