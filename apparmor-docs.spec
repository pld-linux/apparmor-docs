%define		_ver 2.0.1
%define		_svnrel 237
Summary:	Novell AppArmor Host Application Security Suite Documentation package
Summary(pl.UTF-8):	Pakiet z dokumentacją Novell AppArmor Host Application Security Suite
Name:		apparmor-docs
Version:	%{_ver}.%{_svnrel}
Release:	1
Epoch:		1
Group:		Documentation
Source0:	http://forgeftp.novell.com/apparmor/Development%20-%20March%2007%20-%20SnapShot/%{name}-%{_ver}-%{_svnrel}.tar.gz
# Source0-md5:	7c7874c998f97bcc0671db4ad87db46d
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

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację dla AppArmor Host Application Security
Suite. Jest częścią zestawu narzędzi znanych wcześniej pod nazwą
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
