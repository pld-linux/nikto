Summary:	web server assessment tool
Summary(pl.UTF-8):	skrypt do testowania zabezpieczeń serwera www
Name:		nikto
Version:	2.1.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.cirt.net/nikto/%{name}-%{version}.tar.bz2
# Source0-md5:	ce971262e14f5ac1ff634b86366bdaa8
URL:		http://www.cirt.net/nikto2/
Patch0:		%{name}-paths.patch
Requires:	openssl-devel
Requires:	perl-Net-SSLeay
Suggests:	nmap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nikto is a web server assessment tool. It is designed to find various
default and insecure files, configurations and programs on any type of
web server.

%description -l pl.UTF-8
Nikto to narzędzie do oceny zabezpieczeń serwera www. Zostało
zaprojektowane tak by wyszukiwać różne domyślne i niezabezpieczone
pliki, konfiguracje i programy dowolnego typu zainstalowane na
serwerze www.

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/templates
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_sysconfdir}

install nikto.pl $RPM_BUILD_ROOT%{_bindir}
install plugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins
install templates/*.tmpl $RPM_BUILD_ROOT%{_datadir}/%{name}/templates
install docs/{CHANGES.txt,LICENSE.txt,nikto_manual.html,nikto.dtd} $RPM_BUILD_ROOT%{_docdir}/%{name}
install docs/nikto.1 $RPM_BUILD_ROOT%{_mandir}/man1
install nikto.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nikto.pl
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nikto.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/plugins
%dir %{_datadir}/%{name}/templates
%dir %{_docdir}/%{name}
%{_datadir}/%{name}/plugins/*
%{_datadir}/%{name}/templates/*.tmpl
%{_docdir}/%{name}/*
%{_mandir}/man1/nikto.1*
