# 0x04. Loops, conditions and parsing

## Resource Links

1. [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
2. [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
3. [Comparison operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
4. [File test operators](https://tldp.org/LDP/abs/html/fto.html)
5. [Make your scripts portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

## Tasks
0. Create a SSH RSA key pair

  Read for this task:

   * Linux and Mac OS users
   * Windows users

  man: ``ssh-keygen``

  You will soon have to manage your own servers concept page hosted on remote [data centers](https://www.youtube.com/watch?v=iuqXFC_qIvA&t=46s). We need to set them up with your RSA public key so that you can access them via SSH.

  Create a RSA key pair.

  Requirements:

   * Share your public key in your answer file ``0-RSA_public_key.pub``
   * Fill the ``SSH public key`` field of your intranet profile with the public key you just generated
   * **Keep the private key to yourself in a secure location**, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects
   * If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase

  SSH and RSA keys will be covered in depth in a later project.

#### 1. For Best School loop

  Write a Bash script that displays ``Best School`` 10 times.

  Requirement:

   * You must use the ``for`` loop (``while`` and ``until`` are forbidden)

#### 2. While Best School loop

  Write a Bash script that displays ``Best School`` 10 times.

  Requirements:

   * You must use the ``while`` loop (``for`` and ``until`` are forbidden)

#### 3. Until Best School loop

  Write a Bash script that displays ``Best School`` 10 times.

  Requirements:

   * You must use the ``until`` loop (``for`` and ``while`` are forbidden)

#### 4. If 9, say Hi!

  Write a Bash script that displays ``Best School`` 10 times, but for the 9th iteration, displays ``Best School`` and then ``Hi`` on a new line.
 
  Requirements:

   * You must use the ``while`` loop (``for`` and ``until`` are forbidden)
   * You must use the ``if`` statement

#### 5. 4 bad luck, 8 is your chance

  Write a Bash script that loops from 1 to 10 and:

   * displays ``bad luck`` for the 4th loop iteration
   * displays ``good luck`` for the 8th loop iteration
   * displays ``Best School`` for the other iterations

  Requirements:

   * You must use the ``while```loop (``for`` and ``until`` are forbidden)
   * You must use the ``if``, ``elif`` and ``else`` statements

etc...
