# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           uuid
Version:        1.6.2
Release:        %autorelease
Summary:        Universally Unique Identifier library
License:        MIT
URL:            http://www.ossp.org/pkg/lib/uuid/
#!RemoteAsset
Source0:        http://www.mirrorservice.org/sites/ftp.ossp.org/pkg/lib/uuid/%{name}-%{version}.tar.gz

BuildRequires:  config
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  chrpath
BuildSystem:    autotools
BuildOption(conf): --disable-static
BuildOption(conf): --without-perl
BuildOption(conf): --without-php
BuildOption(conf): --with-dce
BuildOption(conf): --with-cxx
BuildOption(conf): --without-pgsql
%patchlist
# Rename library and binaries from uuid to ossp-uuid to avoid conflicts
uuid-1.6.1-ossp.patch
# pgsql: define mkinstalldirs using shtool for directory creation
uuid-1.6.1-mkdir.patch
# php: update extension for PHP 5.4+ by using ZEND_ macros and arg info*
uuid-1.6.2-php54.patch
# Add support for AF_PACKET and netpacket/packet.h
uuid-1.6.2-hwaddr.patch
# Do not strip binaries
uuid-1.6.2-nostrip.patch
# uuid.1: document the -r option as equivalent to -F BIN
uuid-1.6.2-manfix.patch
# Use ldflags for libs too
uuid-1.6.2-ldflags.patch

%description
OSSP uuid is a ISO-C:1999 application programming interface (API) and corresponding
command line interface (CLI) for the generation of DCE 1.1, ISO/IEC 11578:1996 and
RFC 4122 compliant Universally Unique Identifier (UUID).
It supports DCE 1.1 variant UUIDs of version 1 (time and node based), version 3
(name based, MD5), version 4 (random number based) and version 5 (name based, SHA-1).
Additional API bindings are provided for the languages ISO-C++:1998 and Perl:5 Optional
backward compatibility exists for the ISO-C DCE-1.1 and Perl Data::UUID APIs.

UUIDs are 128 bit numbers which are intended to have a high likelihood of uniqueness
over space and time and are computationally difficult to guess. They are globally
unique identifiers which can be locally generated without contacting a global
registration authority. UUIDs are intended as unique identifiers for both mass tagging
objects with an extremely short lifetime and to reliably identifying very persistent
objects across a network.

%package        devel
Summary:        Development support for UUID library
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description    devel
Development headers and libraries for OSSP uuid.

%package        c++
Summary:        C++ support for UUID library
Requires:       %{name} = %{version}-%{release}

%description    c++
C++ libraries for OSSP uuid.

%package        c++-devel
Summary:        C++ development support for UUID library
Requires:       %{name}-c++ = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description    c++-devel
C++ development headers and libraries for OSSP uuid.

%package        perl
Summary:        Perl support for UUID library
BuildRequires:  perl-devel
BuildRequires:  perl-macros
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       %{name} = %{version}-%{release}
Requires:       perl(Data::UUID)

%description    perl
Perl OSSP uuid module.

%package        dce
Summary:        DCE support for UUID library
Requires:       %{name} = %{version}-%{release}

%description    dce
Perl OSSP uuid module.

%package        dce-devel
Summary:        DCE development support for UUID library
Requires:       %{name}-dce = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description    dce-devel
DCE development headers and libraries for OSSP uuid.

%conf -p
export LIB_NAME=libossp-uuid.la DCE_NAME=libossp-uuid_dce.la CXX_NAME=libossp-uuid++.la
export PHP_NAME=$(pwd)/php/modules/ossp-uuid.so PGSQL_NAME=$(pwd)/pgsql/libossp-uuid.so
export CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"

%build -a

pushd perl
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" COMPAT=0
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
%make_build
popd

%install -a
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
chmod 755 %{buildroot}%{_libdir}/*.so.*.*.*

pushd perl
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name '*.bs' -size 0 | xargs rm -f
find %{buildroot} -type f -name .packlist | xargs rm -f
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
popd

chrpath -d %{buildroot}/%{_bindir}/%{name}

%check
make check

pushd perl
LD_LIBRARY_PATH=../.libs make test
perl -MData::UUID -e 'print "Testing compatibility of Data::UUID version $Data::UUID::VERSION\n";'
LD_LIBRARY_PATH=../.libs make test TEST_FILES=uuid_compat.ts
popd

%files
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%{_bindir}/uuid
%{_libdir}/libossp-uuid.so.*
%{_mandir}/man1/*
%exclude %{_mandir}/man1/uuid-config.*

%files devel
%{_bindir}/uuid-config
%{_includedir}/uuid.h
%{_libdir}/{libossp-uuid.so,pkgconfig/ossp-uuid.pc}
%{_mandir}/man3/ossp-uuid.3*
%{_mandir}/man1/uuid-config.*

%files c++
%{_libdir}/libossp-uuid++.so.*

%files c++-devel
%{_includedir}/uuid++.hh
%{_libdir}/libossp-uuid++.so
%{_mandir}/man3/uuid++.3*

%files perl
%{perl_vendorarch}/{auto/*,OSSP*}
%{_mandir}/man3/OSSP::uuid.3*

%files dce
%{_libdir}/libossp-uuid_dce.so.*

%files dce-devel
%{_includedir}/uuid_dce.h
%{_libdir}/libossp-uuid_dce.so

%changelog
%{?autochangelog}
