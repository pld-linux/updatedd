Summary:	Program that allows you IP change on dyndns
Summary(pl):	Program do zmiany IP w dyndns
Name:		updatedd
Version:	1.7
Release:	1
License:	GPL
Group:		Networking/Admin
Vendor:		Philipp Benner <philipp@philippb.tk>
Source0:	http://dl.sourceforge.net/sourceforge/updatedd/%{name}-%{version}.tar.gz
# Source0-md5:	5b0c4ce09da203dbe28a7318aed3c7f3
Patch0:		%{name}-config.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client supports dyndns/statdns/custom, backmx, MX host, wildcard,
offline mode and sysloging. It uses the web based IP detection and a
script is included which can be used to run updatedd by the ppp
daemon. Ovh.net, ods.org, no-ip.org and hn.org are also supported.

%description -l pl
Program do automatycznego aktualizowania IP w systemie dynamicznych
domen dyndns.org, Ovh.net, ods.org, no-ip.org, hn.org . Korzysta z
opartego na WWW sprawdzania adresu IP. Do³±czony jest skrypt s³u¿acy
do uruchamiania updatedd przez demona ppp. 

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{{%{_sysconfdir},%{_libdir}}/%{name},%{_sbindir}}
install bin/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install bin/updatedd $RPM_BUILD_ROOT%{_sbindir}
install Documentation/rc_updatedd* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s %{_libdir}/%{name}/dyndns.so $RPM_BUILD_ROOT%{_libdir}/%{name}/default.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%lang(de) %doc Documentation/README.german
%attr(700,root,root) %dir %{_sysconfdir}/%{name}
%attr(600,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*
