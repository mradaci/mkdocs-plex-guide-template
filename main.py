import os
from datetime import datetime


def define_env(env):
    """
    This hook is called when the config is loading.
    """
    username = "ICADAR"
    repo_name = os.getenv('GITHUB_REPOSITORY',
                          'mkdocs-plex-guide-template').split('/')[-1]
    current_year = datetime.now().year

    # Explicitly check for missing or empty values and assign defaults
    request_url = "mattflixrequests.icadar.com"
    plex_url = "https://app.plex.tv/"
    plex_libraries = os.getenv('PLEX_LIBRARIES') or "Movies and TV Shows"
    noreply_email = os.getenv('NOREPLY_EMAIL') or "noreply@example.com"

    env.variables.update({
        "username": username,
        "repo_name": repo_name,
        "year": current_year,
        "request_url": request_url,
        "plex_url": plex_url,
        "plex_libraries": plex_libraries,
        "noreply_email": noreply_email,
    })
