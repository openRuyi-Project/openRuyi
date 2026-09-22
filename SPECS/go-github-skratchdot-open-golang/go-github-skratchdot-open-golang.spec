# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           open-golang
%define go_import_path  github.com/skratchdot/open-golang
%define commit_id       79abb63cd66e41cb1473e26d11ebdcd68b04c8e5

Name:           go-github-skratchdot-open-golang
Version:        0+git20260922.79abb63
Release:        %autorelease
Summary:        Open files and URLs with the default application
License:        MIT
URL:            https://github.com/skratchdot/open-golang
#!RemoteAsset:  sha256:685af171835e0cb7486d252fba5224b0bebe692cdcbc69cdc1d8bec9f4fb2194
Source0:        https://github.com/skratchdot/open-golang/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# All four upstream tests open a graphical browser, unavailable in OBS.
# Compile the test suite while excluding those desktop integration tests.
BuildOption(check):  -skip '^(TestRun|TestStart|TestRunWith|TestStartWith)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/skratchdot/open-golang) = %{version}

%description
This library opens files, directories and URLs with a chosen application
or the desktop's default application.

%prep -a
rm -rf vendor

%files
%doc README.md
%license LICENSE-MIT
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
