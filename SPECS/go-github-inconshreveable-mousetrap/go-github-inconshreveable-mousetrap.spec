# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mousetrap
%define go_import_path  github.com/inconshreveable/mousetrap

Name:           go-github-inconshreveable-mousetrap
Version:        1.1
Release:        %autorelease
Summary:        Detect starting from Windows explorer
License:        Apache-2.0
URL:            https://github.com/inconshreveable/mousetrap
#!RemoteAsset
Source0:        https://github.com/inconshreveable/mousetrap/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/inconshreveable/mousetrap) = %{version}

%description
mousetrap is a tiny library that answers a single question.

On a Windows machine, was the process invoked by someone double clicking on the executable file while browsing in explorer?

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
