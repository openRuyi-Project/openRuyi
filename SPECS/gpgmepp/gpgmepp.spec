# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gpgmepp
Version:        2.0.0
Release:        %autorelease
Summary:        C++ bindings/wrapper for GPGME
License:        LGPL-2.1-or-later
URL:            https://gnupg.org/software/gpgme/index.html
VCS:            git:https://dev.gnupg.org/source/gnupg.git
#!RemoteAsset:  sha256:d4796049c06708a26f3096f748ef095347e1a3c1e570561701fe952c3f565382
Source0:        https://gnupg.org/ftp/gcrypt/gpgmepp/gpgmepp-%{version}.tar.xz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(gpgme)

%description
GPGME++ is a C++ wrapper for the GnuPG project's GPGME library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for GPGME++.

%files
%license COPYING.LIB COPYING.LESSER
%{_libdir}/libgpgmepp.so.*

%files devel
%doc NEWS README ChangeLog AUTHORS
%{_includedir}/gpgme++/
%{_libdir}/libgpgmepp.so
%{_libdir}/pkgconfig/gpgmepp.pc
%{_libdir}/cmake/Gpgmepp/

%changelog
%autochangelog
