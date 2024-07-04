if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Ashik231/Advance-EvaMaria.git /Advance-EvaMaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Advance-EvaMaria
fi
cd /Advance-EvaMaria
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
