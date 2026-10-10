# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tclap
Version:        1.2.5
Release:        %autorelease
Summary:        Templatized C++ Command Line Parser
License:        MIT
URL:            http://tclap.sourceforge.net
VCS:            git:https://git.code.sf.net/p/tclap/code
#!RemoteAsset:  sha256:bb649f76dae35e8d0dcba4b52acfd4e062d787e6a81b43f7a4b01275153165a6
Source:         https://downloads.sourceforge.net/tclap/tclap-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig

%description
TCLAP is a header-only, flexible C++ library for parsing command line arguments.
This is a metapackage that requires the development files.

%install -a
install -d "%{buildroot}%{_docdir}/%{name}"

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/tclap
%{_libdir}/pkgconfig/tclap.pc
%doc %{_docdir}/tclap/

%changelog
%autochangelog
