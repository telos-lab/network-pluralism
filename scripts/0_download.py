from network_pluralism.download.decisions import download_all_decisions
from network_pluralism.download.statutes import download_all_statutes

if __name__ == "__main__":
    print("Downloading all decisions data")
    download_all_decisions()

    print("Downloading all statutes data")
    download_all_statutes()
