# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           graphite2
Version:        1.3.14
Release:        %autorelease
Summary:        Font rendering capabilities for complex non-Roman writing systems
License:        LGPL-2.1-or-later OR MPL-2.0 OR GPL-2.0-or-later
URL:            https://graphite.sil.org
VCS:            git:https://github.com/silnrsi/graphite
#!RemoteAsset
Source0:        https://github.com/silnrsi/graphite/releases/download/%{version}/%{name}-%{version}.tgz
BuildSystem:    cmake

# Let other package find the cmake files
Patch0:         0001-graphite2-1.2.0-cmakepath.patch
# This fixes compilation with gcc15
Patch1:         0002-graphite2-1.3.14-gcc15.patch

BuildOption(conf):  -DGRAPHITE2_COMPARE_RENDERER=OFF
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(check):  -E 'nametabletest'

BuildRequires:  cmake
BuildRequires:  pkgconfig(freetype2)

%description
Graphite2 is a project within SIL’s Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create “smart fonts” capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package        devel
Summary:        Files for developing with graphite2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Includes and definitions for developing with graphite2.

%files
%license LICENSE COPYING
%doc ChangeLog README.md
%{_bindir}/gr2fonttest
%{_libdir}/libgraphite2.so.3*

%files devel
%dir %{_libdir}/graphite2/
%{_includedir}/graphite2/
# Naming of this file is changed by CMAKE_BUILD_TYPE. - 251
%{_libdir}/graphite2/graphite2-*.cmake
%{_libdir}/graphite2/graphite2.cmake
%{_libdir}/libgraphite2.so
%{_libdir}/pkgconfig/graphite2.pc

%changelog
%autochangelog
