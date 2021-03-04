Summary:	a tool that sorts files and packs them into bags
Name:		fpart
Version:	1.2.0
Release:	1
License:	BSD
URL:		http://contribs.martymac.org
Source0:	https://github.com/martymac/fpart/archive/%{name}-%{version}.tar.gz
# Source0-md5:	4a2a71f1d92feebf935808fed6dc493b
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
Suggests:	cpio
Suggests:	rsync
Suggests:	sudo

%description
Fpart is a tool that helps you sort file trees and pack them into bags
(called "partitions"). It is developed in C and available under the
BSD license.

It splits a list of directories and file trees into a certain number
of partitions, trying to produce partitions with the same size and
number of files. It can also produce partitions with a given number of
files or a limited size.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
autoreconf --install
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README TODO
%attr(755,root,root) %{_bindir}/fpart
%attr(755,root,root) %{_bindir}/fpsync
%{_mandir}/man1/fpart.1*
%{_mandir}/man1/fpsync.1*
