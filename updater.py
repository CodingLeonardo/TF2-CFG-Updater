from pathlib import Path
from git import Repo
import shutil

class CFGUpdater:
  def __init__(self):
    self.cfg_path = "/mnt/c/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/cfg"
    self.cfg_repository_path = Path(str(Path.home()) + "/TF2-config")
    self.cfg_repository_git_url = "git@github.com:CodingLeonardo/TF2-config.git"
    self.cfg_repository_git = Repo(self.cfg_repository_path)
    self.update()

  def update(self):
    if not (self.cfg_repository_path.exists()):
      Repo.clone_from(self.cfg_repository_git_url, self.cfg_repository_path)
    else:
      self.cfg_repository_git.remotes.origin.pull()

    shutil.rmtree(self.cfg_path)
    shutil.copytree(str(self.cfg_repository_path) + "/cfg", self.cfg_path)
    print("CFG Updated!")