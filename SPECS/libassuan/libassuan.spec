# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libassuan
Version:        3.0.2
Release:        %autorelease
Summary:        IPC library used by GnuPG version 2
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://www.gnupg.org/related_software/libassuan/index.en.html
#!RemoteAsset
Source0:        https://www.gnupg.org/ftp/gcrypt/libassuan/%{name}-%{version}.tar.bz2
#!RemoteAsset
Source2:        https://www.gnupg.org/ftp/gcrypt/libassuan/%{name}-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
#!RemoteAsset
Source3:        https://gnupg.org/signature_key.asc#/%{name}.keyring
BuildSystem:    autotools

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  texinfo

%description
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

%package devel
Summary:        IPC library used by GnuPG version 2
Requires:       %{name} = %{version}
Requires:       pkgconfig(gpg-error)

%description devel
Libassuan is the IPC library used by gpg2 (GnuPG version 2)

gpgme also uses libassuan to communicate with a libassuan-enabled GnuPG
v2 server, but it uses it's own copy of libassuan.

%files
%license COPYING COPYING.LIB
%{_libdir}/libassuan.so.*

%files devel
%{_bindir}/libassuan-config
%{_includedir}/assuan.h
%{_libdir}/libassuan.so
%{_libdir}/pkgconfig/libassuan.pc
%{_infodir}/assuan.info*
%{_datadir}/aclocal/libassuan.m4

%changelog
%{?autochangelog}
