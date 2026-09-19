# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glm
Version:        1.0.3
Release:        %autorelease
Summary:        Header-only C++ mathematics library for graphics software
License:        MIT
URL:            https://glm.g-truc.net/
VCS:            git:https://github.com/g-truc/glm.git
#!RemoteAsset:  git+https://github.com/g-truc/glm.git#%{version}
#!CreateArchive
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildOption(conf):  -DGLM_BUILD_LIBRARY=OFF
BuildOption(conf):  -DGLM_BUILD_TESTS=ON

BuildRequires:  cmake

%description
OpenGL Mathematics (GLM) is a header-only C++ mathematics library based on the
OpenGL Shading Language specification. It provides vectors, matrices and
geometric functions for graphics applications.

%package        devel
Summary:        Development headers and build metadata for GLM

%description    devel
Headers and upstream CMake configuration for the GLM mathematics library.

%files devel
%doc readme.md
%license copying.txt
%{_datadir}/glm/
%{_includedir}/glm/

%changelog
%autochangelog
