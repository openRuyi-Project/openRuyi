# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-radix
%define go_import_path  github.com/armon/go-radix

Name:           go-github-armon-go-radix
Version:        1.0.0
Release:        %autorelease
Summary:        Golang implementation of Radix trees
License:        MIT
URL:            https://github.com/armon/go-radix
#!RemoteAsset
Source0:        https://github.com/armon/go-radix/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/armon/go-radix) = %{version}

%description
Provides the radix package that implements a radix tree
(http://en.wikipedia.org/wiki/Radix_tree). The package only provides a
single Tree implementation, optimized for sparse nodes.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
