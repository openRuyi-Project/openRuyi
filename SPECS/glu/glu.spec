# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glu
Version:        9.0.3
Release:        %autorelease
Summary:        Mesa libGLU library
License:        MIT
URL:            http://mesa3d.org/
VCS:            git:https://gitlab.freedesktop.org/mesa/glu
#!RemoteAsset
Source0:        https://gitlab.freedesktop.org/mesa/glu/-/archive/glu-%{version}/glu-glu-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gl)

%description
Mesa implementation of the standard GLU OpenGL utility API.
This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a
find %{buildroot} -name '*.a' -delete

%files
%{_libdir}/libGLU.so.1*

%files devel
%{_includedir}/GL/glu*.h
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc

%changelog
%autochangelog
