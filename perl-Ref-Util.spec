#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Ref-Util
Version  : 0.204
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libref-util-perl/libref-util-perl_0.204-1.debian.tar.xz
Summary  : 'Utility functions for checking references'
Group    : Development/Tools
License  : MIT
Requires: perl-Ref-Util-license = %{version}-%{release}
Requires: perl-Ref-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Ref::Util::XS)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Ref-Util,
version 0.204:
Utility functions for checking references

%package dev
Summary: dev components for the perl-Ref-Util package.
Group: Development
Provides: perl-Ref-Util-devel = %{version}-%{release}
Requires: perl-Ref-Util = %{version}-%{release}

%description dev
dev components for the perl-Ref-Util package.


%package license
Summary: license components for the perl-Ref-Util package.
Group: Default

%description license
license components for the perl-Ref-Util package.


%package perl
Summary: perl components for the perl-Ref-Util package.
Group: Default
Requires: perl-Ref-Util = %{version}-%{release}

%description perl
perl components for the perl-Ref-Util package.


%prep
%setup -q -n Ref-Util-0.204
cd %{_builddir}
tar xf %{_sourcedir}/libref-util-perl_0.204-1.debian.tar.xz
cd %{_builddir}/Ref-Util-0.204
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Ref-Util-0.204/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Ref-Util
cp %{_builddir}/Ref-Util-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Ref-Util/7546885f6438a43ac916b550dd5c623d667a7fc4 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Ref-Util/138c662d9dd39191eb94bee4188ec2d3ded00d07 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Ref::Util.3
/usr/share/man/man3/Ref::Util::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Ref-Util/138c662d9dd39191eb94bee4188ec2d3ded00d07
/usr/share/package-licenses/perl-Ref-Util/7546885f6438a43ac916b550dd5c623d667a7fc4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
