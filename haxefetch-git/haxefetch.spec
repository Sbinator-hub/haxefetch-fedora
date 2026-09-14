Name:           haxefetch-git
Version:        1.1.0
Release:        2%{?dist}
Summary:        A fetch program written in Haxe

License:        MIT
Source0:        https://raw.githubusercontent.com/Sbinator-hub/Haxefetch/main/binary/haxefetch

%define debug_package %{nil}

%description
A fetch program written in Haxe

%prep

%setup -q -c -T

cp %{SOURCE0} .

%build
# No compilation required

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 haxefetch %{buildroot}%{_bindir}/haxefetch

%files
%{_bindir}/haxefetch

%changelog
* Mond Set 14 2026 Stefan <stefanbeta2008@gmail.com> - 1.1.0-1
- Added platform checker command