# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           apr
Version:        1.7.6
Release:        %autorelease
Summary:        Apache Portable Runtime library
License:        Apache-2.0 AND (BSD-4-Clause-UC AND ISC AND Zlib AND Caldera-no-preamble)
URL:            https://apr.apache.org/
VCS:            git:https://github.com/apache/apr
#!RemoteAsset
Source:         https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

# Can't run testsock in qemu user space emulation
Patch2000:      2000-Skip-testsock-test.patch

BuildOption(conf):  --includedir=%{_includedir}/apr-1
BuildOption(conf):  --with-installbuilddir=%{_libdir}/apr-1/build
BuildOption(conf):  --with-devrandom=/dev/urandom
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-sctp

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  libuuid
BuildRequires:  python3
BuildRequires:  make
BuildRequires:  pkgconfig(libxcrypt)

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines, forming a system
portability layer to as many operating systems as possible.

%package        devel
Summary:        APR library development kit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package provides the support files which can be used to
build applications using the APR library.

%conf -p
# regenerate configure script etc.
./buildconf

%build -a
strfn=`echo XXX APR_INT64_STRFN | cpp -I./include -I./include/arch/unix -include include/arch/unix/apr_private.h \
            | sed -n '/^XXX/{s/XXX //;p;}'`
if test "x$strfn" = "x"; then
    echo "configure failed to detect working strtol, bailing." >&2
    exit 1
fi

%install -a
install -d -m 755 %{buildroot}%{_datadir}/aclocal
install -m 644 build/find_apr.m4 %{buildroot}%{_datadir}/aclocal
install -m 644 build/apr_common.m4 %{buildroot}%{_datadir}/aclocal

sed -ri '/^dependency_libs/{s,-l(uuid|crypt) ,,g}' %{buildroot}%{_libdir}/libapr-1.la
sed -ri '/^LIBS=/{s,-l(uuid|crypt) ,,g;s/  */ /g}' %{buildroot}%{_bindir}/apr-1-config
sed -ri '/^Libs/{s,-l(uuid|crypt) ,,g}' %{buildroot}%{_libdir}/pkgconfig/apr-1.pc

install -d -m 755 %{buildroot}%{_libdir}/apr-1/build
sed -i '1s,/.*,/usr/bin/python3,' build/gen-build.py
for f in build/gen-build.py build/install.sh build/config.*; do
    install -c -m755 $f %{buildroot}%{_libdir}/apr-1/build
done

rm -f %{buildroot}%{_libdir}/apr.exp
rm -f %{buildroot}%{_libdir}/libapr-1.a

%check -p
# Build tests serially to avoid race conditions
%define _smp_build_ncpus 1

%files
%doc CHANGES LICENSE NOTICE README*
%{_libdir}/libapr-1.so.*

%files devel
%doc docs/APRDesign.html docs/canonical_filenames.html docs/incomplete_types docs/non_apr_programs
%{_bindir}/apr-1-config
%{_libdir}/libapr-1.so
%{_libdir}/pkgconfig/apr-1.pc
%dir %{_libdir}/apr-1
%dir %{_libdir}/apr-1/build
%{_libdir}/apr-1/build/*
%dir %{_includedir}/apr-1
%{_includedir}/apr-1/*.h
%{_datadir}/aclocal/*.m4

%changelog
%{?autochangelog}
