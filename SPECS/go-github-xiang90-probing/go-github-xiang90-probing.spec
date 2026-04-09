# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           probing
%define go_import_path  github.com/xiang90/probing

Name:           go-github-xiang90-probing
Version:        0.0.2
Release:        %autorelease
Summary:        Go library for HTTP probing
License:        MIT
URL:            https://github.com/xiang90/probing
#!RemoteAsset
Source0:        https://github.com/xiang90/probing/archive/refs/tags/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xiang90/probing) = %{version}

%description
Library for simple probing via HTTP.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
