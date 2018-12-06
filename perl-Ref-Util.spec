#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Ref-Util
Version  : 0.204
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARC/Ref-Util-0.204.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libref-util-perl/libref-util-perl_0.204-1.debian.tar.xz
Summary  : 'Utility functions for checking references'
Group    : Development/Tools
License  : MIT
Requires: perl-Ref-Util-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Ref::Util::XS)

%description
This archive contains the distribution Ref-Util,
version 0.204:
Utility functions for checking references

%package dev
Summary: dev components for the perl-Ref-Util package.
Group: Development
Provides: perl-Ref-Util-devel = %{version}-%{release}

%description dev
dev components for the perl-Ref-Util package.


%package license
Summary: license components for the perl-Ref-Util package.
Group: Default

%description license
license components for the perl-Ref-Util package.


%prep
%setup -q -n Ref-Util-0.204
cd ..
%setup -q -T -D -n Ref-Util-0.204 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Ref-Util-0.204/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Ref-Util
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Ref-Util/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1Ref/Util.pm
/usr/lib/perl5/vendor_perl/5.28.1Ref/Util/PP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Ref::Util.3
/usr/share/man/man3/Ref::Util::PP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Ref-Util/LICENSE
