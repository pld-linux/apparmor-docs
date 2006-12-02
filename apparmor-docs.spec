Summary:	Novell AppArmor Host Application Security Suite Documentation package
Name:		apparmor-docs
Version:	2.0
Release:	1
Group:		Documentation
Source0:	%{name}-%{version}-57.tar.gz
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

%prep
%setup -q

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
