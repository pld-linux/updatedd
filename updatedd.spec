Summary:	Program that allows you IP change on dyndns
Summary(pl.UTF-8):	Program do zmiany IP w dyndns
Name:		updatedd
Version:	2.6
Release:	1
License:	GPL
Group:		Networking/Admin
Vendor:		Philipp Benner <philipp@philippb.tk>
Source0:	http://savannah.nongnu.org/download/updatedd/%{name}_%{version}.tar.gz
# Source0-md5:	95655596eb6e0e381d60a458f6a45fee
Patch0:		%{name}-config.patch
URL:		http://updatedd.philipp-benner.de/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client supports dyndns/statdns/custom, backmx, MX host, wildcard,
offline mode and sysloging. It uses the web based IP detection and a
script is included which can be used to run updatedd by the ppp
daemon. Supported services: changeip.com, dyndns.org, eurodyndns.org
hn.org, no-ip.com, ods.org, ovh.com, regfish.com, tzo.com.

%description -l pl.UTF-8
Program do automatycznego aktualizowania IP w systemie dynamicznych
domen changeip.com, dyndns.org, eurodyndns.org hn.org, no-ip.com,
ods.org, ovh.com, regfish.com, tzo.com. Korzysta z opartego na WWW
sprawdzania adresu IP. Dołączony jest skrypt służący do uruchamiania
updatedd przez demona ppp.

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install updatedd-wrapper/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- updatedd < 2.0
echo
echo Configuration files has changed to %{_sysconfdir}/updatedd-wrapper.conf
echo You may run the program by typing %{_bindir}/updatedd-wrapper
echo

%files
%defattr(644,root,root,755)
%doc AUTHORS Documentation/updatedd-pppd-rc Documentation/updatedd-2.4-english.pdf
%lang(de) %doc Documentation/updatedd-2.4-german.pdf
%attr(700,root,root) %dir %{_sysconfdir}/%{name}
%attr(600,root,root) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*so*
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
