# $Id: time-machine.spec,v 1.3 2015/04/21 00:18:06 davidj Exp $
# Authority: ICSI

Summary: ICSI utilities for IDS systems
Name: icsiids-utils
Version: 0.1.1
Release: 1.ICSI
License: distributable 
Group: Applications/Internet
# URL: https://www.ICSI.Berkeley.EDU

Packager: David Johnson
Vendor: ICSI, http://www.ICSI.Berkeley.EDU

Source: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: Python

%description
Utilities useful in working with IDS systems

%prep
%setup -n %{name}-%{version}

%build
./configure --prefix=%{_prefix}
%{__make} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.md
%{_bindir}/*

%changelog
* Thu May  7 2015 David Johnson <davidj@ICSI.Berkeley.EDU>
- Initial package.

