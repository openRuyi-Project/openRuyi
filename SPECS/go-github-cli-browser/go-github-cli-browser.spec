# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           browser
%define go_import_path  github.com/cli/browser

Name:           go-github-cli-browser
Version:        1.3.0
Release:        %autorelease
Summary:        Helpers for opening content in the default web browser
License:        BSD-2-Clause
URL:            https://github.com/cli/browser
#!RemoteAsset:  sha256:b0e9730c2ebc1e352b847cf3bcbcdce23e75ea811862ff8b1ee24fe285de06f1
Source0:        https://github.com/cli/browser/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/cli/browser) = %{version}

%description
browser provides Go helpers for opening URLs, files and readers in the system's
default web browser.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
