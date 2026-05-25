# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           deepcopy
%define go_import_path  github.com/mohae/deepcopy
%define commit_id c48cc78d482608239f6c4c92a4abd87eb8761c90

Name:           go-github-mohae-deepcopy
Version:        0+git20170929.c48cc78
Release:        %autorelease
Summary:        Deep copy things
License:        MIT
URL:            https://github.com/mohae/deepcopy
#!RemoteAsset:  sha256:6b171346026b553c49584c10a72267ebabae71e229b08c42cf9d23bd4ddcd6f2
Source0:        https://github.com/mohae/deepcopy/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n deepcopy-c48cc78d482608239f6c4c92a4abd87eb8761c90

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mohae/deepcopy) = %{version}


%description
deepCopy

[Image: GoDoc] (https://godoc.org/github.com/mohae/deepcopy?status.svg)
(https://godoc.org/github.com/mohae/deepcopy)[Image: Build Status]
(https://travis-ci.org/mohae/deepcopy.png) (https://travis-
ci.org/mohae/deepcopy)

DeepCopy makes deep copies of things: unexported field values are not
copied.

Usage

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
