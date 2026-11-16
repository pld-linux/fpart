Summary:	a tool that sorts files and packs them into bags
Name:		fpart
Version:	1.7.1
Release:	1
License:	BSD
Source0:	https://github.com/martymac/fpart/archive/%{name}-%{version}.tar.gz
# Source0-md5:	714f519cc202a824a092242fe3e0b02c
URL:		http://contribs.martymac.org/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
Suggests:	cpio
Suggests:	rsync
Suggests:	sudo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc COPYING Changelog.md README.md TODO
%attr(755,root,root) %{_bindir}/fpart
%attr(755,root,root) %{_bindir}/fpsync
%{_mandir}/man1/fpart.1*
%{_mandir}/man1/fpsync.1*
