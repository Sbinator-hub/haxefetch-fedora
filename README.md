# Official Fedora Linux copr repo for Haxefetch

## How to install this?

1. Enable Copr repo
- `dnf copr enable stefan2008/Haxefetch`

2. Refresh Fedora repos
- `dnf update`

3. Install Haxefetch 
- `dnf install haxefetch`

---

### Wanna support?
Go here
- https://copr.fedorainfracloud.org/coprs/stefan2008/Haxefetch/

> **Note:** Due to how Fedora handles metadata caches, you have to wait for bit fully sync new package version and vel in order to install different, but if you want to get new package with new vel number, you can force dnf to refresh new metadata cache `dnf upgrade --refresh haxefetch` 
