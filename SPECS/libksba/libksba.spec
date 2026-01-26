# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libksba
Version:        1.6.7
Release:        %autorelease
Summary:        A X.509 Library
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later AND MIT
URL:            https://www.gnupg.org
VCS:            git:https://git.gnupg.org/libksba.git
#!RemoteAsset
Source:         https://gnupg.org/ftp/gcrypt/libksba/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source2:        https://gnupg.org/ftp/gcrypt/libksba/%{name}-%{version}.tar.bz2.sig
#!RemoteAsset
Source3:        https://gnupg.org/signature_key.asc#/%{name}.keyring
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-pic

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error)

%description
KSBA is a library to simplify the task of working with X.509
certificates, CMS data, and related data. This package contains the
runtime shared libraries.

%package        devel
Summary:        Development files for the libksba library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, documentation, and other files needed
to develop applications that use the libksba library.

%conf -p
autoreconf -vfi

%files
%license COPYING*
%doc README AUTHORS ChangeLog NEWS THANKS TODO
%{_libdir}/libksba.so.8*

%files devel
%{_bindir}/ksba-config
%{_libdir}/libksba.so
%{_libdir}/pkgconfig/ksba.pc
%{_includedir}/ksba.h
%{_datadir}/aclocal/ksba.m4
%{_infodir}/ksba.info%{?ext_info}

%changelog
%{?autochangelog}
