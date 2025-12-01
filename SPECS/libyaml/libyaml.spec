# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Mahno <bestwow2014@gmail.com>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libyaml
Version:        0.2.5
Release:        %autorelease
Summary:        A YAML parser and emitter written in C
License:        MIT
URL:            https://pyyaml.org/wiki/LibYAML
#!RemoteAsset
Source:         http://pyyaml.org/download/libyaml/yaml-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildSystem:    autotools
BuildOption(conf): --disable-static

%description
A YAML parser and emitter written in C

%package devel
Summary:        Development files for libyaml
Requires:              %{name} = %{version}

%description devel
This package holds the development files for libyaml,
a YAML parser and emitter written in C.

%prep
%autosetup -n yaml-%{version}

%files
%{_libdir}/libyaml-0.so.2
%{_libdir}/libyaml-0.so.2.0.*

%files devel
%{_includedir}/yaml.h
%{_libdir}/libyaml.so
%{_libdir}/pkgconfig/yaml-0.1.pc

%changelog
%{?autochangelog}
