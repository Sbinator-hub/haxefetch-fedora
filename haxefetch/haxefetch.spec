Name:           haxefetch
Version:        1.0.0
Release:        1%{?dist}
Summary:        A fetch program written in Haxe

License:        MIT
URL:            https://github.com/Sbinator-hub/Haxefetch
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

%define debug_package %{nil}

%description
A fetch program written in Haxe

%prep
%autosetup -c

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 0755 haxefetch %{buildroot}%{_bindir}/haxefetch

%files
%{_bindir}/haxefetch

%changelog
* Mon Aug 24 2026 Stefan <stefan@localhost> - 1.0.0-1
- Initial release of Haxefetch