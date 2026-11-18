# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tclap
Version:        1.6.0
Release:        %autorelease
Summary:        Templatized C++ Command Line Parser
License:        MIT
URL:            https://github.com/DAarno/tclap
VCS:            git:https://github.com/DAarno/tclap.git
#!RemoteAsset:  sha256:2ed4bb7655cb4feb7a0432311f1194875bf2d61d6624bf3e513fa101cb0bcb10
Source:         https://github.com/DAarno/tclap/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  docbook-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  pkgconfig(python3)

%description
TCLAP is a header-only, flexible C++ library for parsing command line arguments.
This is a metapackage that requires the development files.

%conf -p
sed -i 's|/usr/share/xml/docbook/stylesheet/docbook-xsl/html/docbook.xsl|%{_datadir}/sgml/docbook/xsl-stylesheets/html/docbook.xsl|' docs/CMakeLists.txt

%files
%doc AUTHORS ChangeLog NEWS README
%doc %{_docdir}/tclap/*.html
%doc %{_docdir}/tclap/style.css
%doc %{_docdir}/tclap/test1.cpp
%doc %{_docdir}/tclap/html/
%license COPYING
%{_includedir}/tclap
%{_libdir}/cmake/TCLAP/
%{_libdir}/pkgconfig/tclap.pc

%changelog
%autochangelog
