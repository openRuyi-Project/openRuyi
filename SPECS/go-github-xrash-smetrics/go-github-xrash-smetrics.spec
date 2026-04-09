# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           smetrics
%define go_import_path  github.com/xrash/smetrics
%define commit_id 55b8f293f34240a78d581f12dd61738357eb6c34

Name:           go-github-xrash-smetrics
Version:        0+git20250705.55b8f29
Release:        %autorelease
Summary:        String metrics library written in Go.
License:        MIT
URL:            https://github.com/xrash/smetrics
#!RemoteAsset
Source0:        https://github.com/xrash/smetrics/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xrash/smetrics) = %{version}

%description
smetrics is "string metrics".

Package smetrics provides a bunch of algorithms for calculating the
distance between strings.

There are implementations for calculating the popular Levenshtein
distance (aka Edit Distance or Wagner-Fischer), as well as the Jaro
distance, the Jaro-Winkler distance, and more.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
