Summary:	Program that allows you IP change on dyndns
Summary(pl):	Program do zmiany IP w dyndns
Name:		updatedd
%define 	sub_ver 1
%define		_ver	2.1
Version:	%{_ver}_%{sub_ver}
Release:	1
License:	GPL
Group:		Networking/Admin
Vendor:		Philipp Benner <philipp@philippb.tk>
Source0:	http://dl.sourceforge.net/sourceforge/updatedd/%{name}_%{_ver}-%{sub_ver}.tar.gz
# Source0-md5:	07244db30ecb3c551f0477b2e3f5fce0
Patch0:		%{name}-config.patch
Patch1:		%{name}-amd64.patch
URL:		http://updatedd.philipp-benner.de/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client supports dyndns/statdns/custom, backmx, MX host, wildcard,
offline mode and sysloging. It uses the web based IP detection and a
script is included which can be used to run updatedd by the ppp daemon.
Supported services: changeip.com, dyndns.org, eurodyndns.org hn.org,
no-ip.com, ods.org, ovh.com, regfish.com, tzo.com.

%description -l pl
Program do automatycznego aktualizowania IP w systemie dynamicznych
domen changeip.com, dyndns.org, eurodyndns.org hn.org, no-ip.com,
ods.org, ovh.com, regfish.com, tzo.com. Korzysta z opartego na WWW
sprawdzania adresu IP. Do³±czony jest skrypt s³u¿acy do uruchamiania
updatedd przez demona ppp.

%prep
%setup -q -n %{name}-%{_ver}
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_datadir}}/%{name}
install -d $RPM_BUILD_ROOT{%{_mandir}/{man1,man5},%{_bindir}}

install src/plugins/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install src/updatedd $RPM_BUILD_ROOT%{_bindir}
install updatedd-wrapper/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install updatedd-wrapper/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install updatedd-wrapper/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install updatedd-wrapper/updatedd-wrapper $RPM_BUILD_ROOT%{_bindir}
install scripts/*.pl $RPM_BUILD_ROOT%{_datadir}/%{name}
install src/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- updatedd < 2.0
echo
echo Configuration files has changed to %{_sysconfdir}/updatedd-wrapper.conf
echo You may run the program by typing %{_bindir}/updatedd-wrapper
echo

%files
%defattr(644,root,root,755)
%doc AUTHORS debian/changelog debian/README.debian Documentation/updatedd-pppd-rc
%attr(700,root,root) %dir %{_sysconfdir}/%{name}
%attr(600,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*
%attr(755,root,root) %{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
