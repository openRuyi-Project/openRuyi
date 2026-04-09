# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           svgo
%define go_import_path  github.com/ajstarks/svgo
%define upstream_version go.weekly.2012-01-27

Name:           go-github-ajstarks-svgo
Version:        2012.01.27
Release:        %autorelease
Summary:        Go Language Library for SVG generation
License:        CC-BY-3.0
URL:            https://github.com/ajstarks/svgo
#!RemoteAsset
Source0:        https://github.com/ajstarks/svgo/archive/%{upstream_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}.%{upstream_version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/ajstarks/svgo) = %{version}

%description
The library generates SVG as defined by the Scalable Vector Graphics 1.1
Specification ((http://www.w3.org/TR/SVG11/)). Output goes to the
specified io.Writer.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
