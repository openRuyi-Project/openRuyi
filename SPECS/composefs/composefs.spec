# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           composefs
Version:        1.0.8
Release:        %autorelease
Summary:        Tools to handle creating and mounting composefs images
License:        LGPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/containers/composefs
#!RemoteAsset:  sha256:207384deb196198ac4764c5b42bb558f7c661494302b380afc09447678538386
Source0:        https://github.com/containers/composefs/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -D fuse=enabled
BuildOption(conf):  -D man=disabled

BuildRequires:  meson
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(fuse3)

%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.
Please see https://github.com/containers/composefs for more information.

%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Devel files for %{name}.

%files
%doc README.md
%license COPYING COPYING.GPL-2.0-only COPYING.GPL-2.0-or-later COPYING.LGPL-2.1-or-later LICENSE.Apache-2.0
%{_bindir}/mkcomposefs
%{_bindir}/composefs-info
%{_sbindir}/mount.composefs
%{_libdir}/libcomposefs.so.*

%files devel
%{_includedir}/libcomposefs
%{_libdir}/libcomposefs.so
%{_libdir}/pkgconfig/composefs.pc
%{_libdir}/libcomposefs.a

%changelog
%autochangelog
