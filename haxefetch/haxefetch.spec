Name:   haxefetch
Version:    1.0.0
Release:    1%{?dist}
Summary:    A fetch program written in Haxe

License:    MIT
Source0:    https://raw.githubusercontent.com/Sbinator-hub/Haxefetch/main/binary/haxefetch

%define debug_package %{nil}

%description
A fetch tool written in Haxe

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/haxefetch

%files
%{_bindir}/haxefetch