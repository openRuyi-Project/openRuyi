# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zlib
Version:        1.3.1
Release:        %autorelease
Summary:        Library implementing the DEFLATE compression algorithm
License:        Zlib
URL:            https://www.zlib.net/
#!RemoteAsset
Source0:        https://zlib.net/zlib-%{version}.tar.gz
#!RemoteAsset
Source1:        https://zlib.net/zlib-%{version}.tar.gz.asc
Source4:        LICENSE
Patch1:         zlib-format.patch
Patch2:         0001-Do-not-try-to-store-negative-values-in-unsigned-int.patch
# we should simply rely on soname versioning to protect us
Patch3:         zlib-no-version-check.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package -n libz1
Summary:        Library implementing the DEFLATE compression algorithm
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n libz1
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

%package devel
Summary:        Development files for zlib, a data compression library
Requires:       glibc-devel
Requires:       libz1 = %{version}

%description devel
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

This subpackage holds the development headers for the library.

The zlib data format is itself portable across platforms. Unlike the
LZW compression method used in unix compress(1) and in the GIF image
format, the compression method currently used in zlib essentially
never expands the data. (LZW can double or triple the file size in
extreme cases.) zlib's memory footprint is also independent of the
input data and can be reduced, if necessary, at some cost in
compression.

%package devel-static
Summary:        Static library for zlib
Requires:       %{name}-devel = %{version}
Provides:       %{name}-devel:%{_libdir}/libz.a

%description devel-static
zlib is a general-purpose lossless data-compression library,
implementing an API for the DEFLATE algorithm, the latter of
which is being used by, for example, gzip and the ZIP archive
format.

This subpackage contains the static version of the library
used for development.

%package -n libminizip1
Summary:        Library for manipulation with .zip archives

%description -n libminizip1
Minizip is a library for manipulation with files from .zip archives.

%package -n minizip-devel
Summary:        Development files for the minizip library
Requires:       %{name}-devel = %{version}
Requires:       libminizip1 = %{version}
Requires:       pkgconfig

%description -n minizip-devel
This package contains the libraries and header files needed for
developing applications which use minizip.

%package testsuite
Summary:        Provide the test examples to reproduce test suite
Requires:       libz1 = %{version}

%description testsuite
To run the testsuite, execute %{_libexecdir}/%{name}/testsuite

It should exit 0

%prep
%autosetup
cp %{SOURCE4} .

%conf
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export LDFLAGS="-Wl,-z,relro,-z,now"
# For sure not autotools build
CC="cc" CFLAGS="%{optflags}" ./configure \
    --shared \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    %{nil}

%build
%make_build

# And build minizip
cd contrib/minizip
autoreconf -fvi
%configure \
    --disable-static \
    --disable-silent-rules
%make_build

%check
%make_build check

%install
mkdir -p %{buildroot}%{_libdir}
%make_install
# manpage
install -m 644 zlib.3 %{buildroot}%{_mandir}/man3
install -m 644 zutil.h %{buildroot}%{_includedir}
# examples
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r examples/ %{buildroot}%{_docdir}/%{name}/

install -D examplesh %{buildroot}%{_libexecdir}/%{name}/testsuite

# Install minizip
cd contrib/minizip
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libz1
%license LICENSE
%{_libdir}/libz.so.1.3.1
%{_libdir}/libz.so.1

%files devel
%doc README ChangeLog
%dir %{_docdir}/%{name}/
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/*
%{_mandir}/man3/zlib.3%{?ext_man}
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_includedir}/zutil.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc

%files -n libminizip1
%doc contrib/minizip/MiniZip64_info.txt contrib/minizip/MiniZip64_Changes.txt
%{_libdir}/libminizip.so.*

%files -n minizip-devel
%dir %{_includedir}/minizip
%{_includedir}/minizip/*.h
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc

%files devel-static
%{_libdir}/libz.a

%files testsuite
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/testsuite

%changelog
%{?autochangelog}
