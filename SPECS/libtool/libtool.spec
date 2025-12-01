# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "testsuite"
%define psuffix -testsuite
%else
%define psuffix %{nil}
%endif
Name:           libtool%{psuffix}
Version:        2.4.7
Release:        %autorelease
Summary:        A Tool to Build Shared Libraries
License:        GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnu.org/software/libtool/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/libtool/libtool-%{version}.tar.xz.sig
Patch0:         libtool-reproducible-hostname.patch
Patch1:         handle-Werror-return-type.patch
Patch2:         libtool-2.4.7-grep-3.8.patch

Buildsystem:    autotools

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gcc-objc
BuildRequires:  help2man
BuildRequires:  lzma
BuildRequires:  texinfo
BuildRequires:  pkgconfig(zlib)
Requires:       automake > 1.4
Requires:       libltdl7 = %{version}
Requires:       m4 >= 1.4.16
Requires:       tar
Provides:       libltdl-devel
Provides:       libtool-ltdl-devel
BuildOption: --enable-ltdl-install

%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in a generic fashion.

%package -n libltdl7
Summary:        Libtool Runtime Library
License:        LGPL-2.1-or-later

%description -n libltdl7
Library needed by programs that use the ltdl interface of GNU libtool.

%conf -p
rm -f doc/libtool.info

%if "%{flavor}" == "testsuite"
%check
trap 'test $? -ne 0 && cat tests/testsuite.log' EXIT
%make_build check

%install
:

%else

%install -a
chmod +x %{buildroot}%{_datadir}/libtool/build-aux/ltmain.sh
# Do not add builder's hostname into generated scripts
sed -i "/uname -n/d" %{buildroot}%{_datadir}/aclocal/libtool.m4
%endif

%if "%{name}" == "libtool"
%files
%license COPYING
%doc AUTHORS NEWS README THANKS ChangeLog
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_includedir}/libltdl
%{_includedir}/ltdl.h
%{_libdir}/libltdl.a
%{_libdir}/libltdl.so
%{_datadir}/aclocal/*.m4
%{_infodir}/libtool.info%{?ext_info}
%{_infodir}/libtool.info-1%{?ext_info}
%{_infodir}/libtool.info-2%{?ext_info}
%{_mandir}/man1/libtool.1%{?ext_man}
%{_mandir}/man1/libtoolize.1%{?ext_man}
%{_datadir}/libtool

%files -n libltdl7
%{_libdir}/libltdl.so.7*
%endif

%changelog
%{?autochangelog}
