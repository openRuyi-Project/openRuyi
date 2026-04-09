# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libbluray
Version:        1.4.1
Release:        %autorelease
Summary:        Library to access Blu-Ray disks for video playback
License:        LGPL-2.0-or-later
URL:            https://www.videolan.org/developers/libbluray.html
VCS:            git:https://code.videolan.org/videolan/libbluray
#!RemoteAsset:  sha256:76b5dc40097f28dca4ebb009c98ed51321b2927453f75cc72cf74acd09b9f449
Source0:        https://download.videolan.org/pub/videolan/libbluray/%{version}/libbluray-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dbdj_jar=disabled
BuildOption(conf):  -Denable_docs=true
BuildOption(conf):  -Denable_devtools=true
BuildOption(conf):  -Denable_examples=true
BuildOption(conf):  -Ddefault_library=shared

BuildRequires:  meson
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
This package is aiming to provide a full portable free open source Blu-Ray
library, which can be plugged into popular media players to allow full Blu-Ray
navigation and playback on Linux.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libbluray.so.3*
%{_bindir}/*

%files devel
%{_docdir}/libbluray/html/
%{_includedir}/libbluray
%{_libdir}/libbluray.so
%{_libdir}/pkgconfig/libbluray.pc

%changelog
%autochangelog
