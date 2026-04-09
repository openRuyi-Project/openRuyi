# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           colorstring
%define go_import_path  github.com/mitchellh/colorstring
%define commit_id d06e56a500db4d08c33db0b79461e7c9beafca2d

Name:           go-github-mitchellh-colorstring
Version:        0+git20190213.d06e56a
Release:        %autorelease
Summary:        Go (golang) library for colorizing strings for terminal output.
License:        MIT
URL:            https://github.com/mitchellh/colorstring
#!RemoteAsset
Source0:        https://github.com/mitchellh/colorstring/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mitchellh/colorstring) = %{version}

%description
colorstring is a Go library for outputting colored strings to
a console using a simple inline syntax in your string
to specify the color to print as.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
