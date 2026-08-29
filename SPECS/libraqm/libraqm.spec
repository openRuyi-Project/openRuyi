# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libraqm
Version:        0.10.5
Release:        %autorelease
Summary:        A library for complex text layout
License:        MIT
URL:            https://github.com/HOST-Oman/libraqm
#!RemoteAsset:  sha256:563053e724892a7b037913110ea2daef50ad575d4fa9f7c368ae1e4515f5e856
Source:         https://github.com/HOST-Oman/libraqm/releases/download/v%{version}/raqm-%{version}.tar.xz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(fribidi)

%description
Raqm is a small library that encapsulates the logic
for complex text layout and provides a convenient API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/libraqm.so.*

%files devel
%{_includedir}/raqm.h
%{_includedir}/raqm-version.h
%{_libdir}/libraqm.so
%{_libdir}/pkgconfig/raqm.pc

%changelog
%autochangelog
