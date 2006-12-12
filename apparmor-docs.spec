%define		_ver 2.0
%define		_svnrel 57
Summary:	Novell AppArmor Host Application Security Suite Documentation package
Summary(pl):	Pakiet z dokumentacj± Novell AppArmor Host Application Security Suite
Name:		apparmor-docs
Version:	%{_ver}.%{_svnrel}
Release:	1
Group:		Documentation
Source0:	http://forgeftp.novell.com/apparmor/Development%20-%20October%20Snapshot/%{name}-%{_ver}-%{_svnrel}.tar.gz
# Source0-md5:	3c371d0d471a4a52499b8d0135dae096
License:	GPL
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
BuildRequires:	perl-tools-pod
Provides:	subdomain-docs
Obsoletes:	subdomain-docs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains documentation for the AppArmor Host Application
Security Suite. This package is part of a suite of tools that used to
be named SubDomain.

%description -l pl
Ten pakiet zawiera dokumentacjê dla AppArmor Host Application Security
Suite. Jest czê¶ci± zestawu narzêdzi znanych wcze¶niej pod nazw±
SubDomain.

%prep
%setup -q -n %{name}-%{_ver}

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install_manpages \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.[0-9].*html immunix.css
%{_mandir}/man?/*
