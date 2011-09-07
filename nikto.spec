Summary:	Web server assessment tool
Summary(pl.UTF-8):	Skrypt do testowania zabezpieczeń serwera WWW
Name:		nikto
Version:	2.1.4
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.cirt.net/nikto/%{name}-%{version}.tar.bz2
# Source0-md5:	0d58d9ca27b9f387b60130e125db8687
URL:		http://www.cirt.net/nikto2/
Patch0:		%{name}-paths.patch
Suggests:	nmap
Suggests:	perl-Net-SSLeay
Suggests:	openssl-devel
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
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}

install nikto.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -a nikto.pl $RPM_BUILD_ROOT%{_bindir}
cp -a plugins templates $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a docs/nikto.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nikto.pl
%doc docs/*.txt docs/nikto.dtd docs/nikto_manual.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nikto.conf
%{_datadir}/%{name}
%{_mandir}/man1/nikto.1*
