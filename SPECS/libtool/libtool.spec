# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtool
Version:        2.5.4
Release:        %autorelease
Summary:        A Tool to Build Shared Libraries
License:        GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnu.org/software/libtool/
VCS:            git:https://git.savannah.gnu.org/git/libtool.git
#!RemoteAsset:  sha256:f81f5860666b0bc7d84baddefa60d1cb9fa6fceb2398cc3baca6afaa60266675
Source0:        https://ftpmirror.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
Buildsystem:    autotools

BuildOption(conf):  --enable-ltdl-install

BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gcc-objc
BuildRequires:  help2man
BuildRequires:  lzma
BuildRequires:  texinfo
BuildRequires:  pkgconfig(zlib)

Requires:       automake > 1.4
Requires:       libltdl = %{version}-%{release}
Requires:       m4 >= 1.4.16
Requires:       tar


%description
GNU libtool is a set of shell scripts to automatically configure UNIX
architectures to build shared libraries in a generic fashion.

%package     -n libltdl
Summary:        Libtool Runtime Library
License:        LGPL-2.1-or-later

%description -n libltdl
Library needed by programs that use the ltdl interface of GNU libtool.

%conf -p
rm -f doc/libtool.info

%install -a
chmod +x %{buildroot}%{_datadir}/libtool/build-aux/ltmain.sh
# Do not add builder's hostname into generated scripts
sed -i "/uname -n/d" %{buildroot}%{_datadir}/aclocal/libtool.m4

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

%files -n libltdl
%{_libdir}/libltdl.so.7*

%changelog
%{?autochangelog}
