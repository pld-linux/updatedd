Summary:	updatedd program allows you change ip on dyndns
Summary(pl):	updatedd program do zmiany ip w dyndns
Name:		updatedd
Version:	1.7
Release:	1
License:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Vendor:         Philipp Benner <philipp@philippb.tk>
Source0:	http://dl.sourceforge.net/sourceforge/updatedd/%{name}-%{version}.tar.gz
# Source0-md5:	5b0c4ce09da203dbe28a7318aed3c7f3
Patch0:		updatedd_config.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	sbindir  /usr/sbin
%define 	libdir 	 /usr/lib
%define		etc	 /etc/updatedd

%description
This client supports dyndns/statdns/custom, backmx, mx host, wildcard, 
offline mode and sysloging. It uses the web based IP detection and a script 
is included which can be used to run updatedd by the ppp daemon. Ovh.net, 
ods.org, no-ip.org and hn.org are also supported

%description -l pl
Program do automatycznego aktualizowania ip w systemie dynamicznych domen
dyndns.org, Ovh.net, ods.org, no-ip.org, hn.org

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{libdir}/updatedd
install -d $RPM_BUILD_ROOT%{sbindir}
install -d $RPM_BUILD_ROOT%{etc}
install bin/*.so $RPM_BUILD_ROOT%{libdir}/updatedd
install bin/updatedd $RPM_BUILD_ROOT%{sbindir}
install Documentation/rc_updatedd* $RPM_BUILD_ROOT%{etc}
ln -s %{libdir}/updatedd/dyndns.so $RPM_BUILD_ROOT%{libdir}/updatedd/default.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/README.german
%attr(700,root,root) %{etc}/*
%attr(700,root,root) %{sbindir}/*
%{libdir}/updatedd/*
