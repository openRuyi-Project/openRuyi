# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           osutil
%define go_import_path  github.com/tredoe/osutil

# The user test initializer requires root access to the shadow database.
%define go_test_exclude_glob github.com/tredoe/osutil/user

Name:           go-github-tredoe-osutil
Version:        1.5.0
Release:        %autorelease
Summary:        Operating system utilities for Go
License:        MPL-2.0 AND BSD-2-Clause
URL:            https://github.com/tredoe/osutil
#!RemoteAsset:  sha256:3c1f4940e85dcf2c389bb81fa9ce2709005d0fe181f3a48929e4d271bbda7d35
Source0:        https://github.com/tredoe/osutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Integration tests invoke sudo or modify system packages. TestRun assumes
# a fixed directory enumeration order, which differs between OBS workers.
BuildOption(check):  -skip '^(TestSudo|TestPackager|TestRun)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tredoe/osutil) = %{version}

%description
This library provides operating system helpers for files, shell
commands, user accounts and password hashing.

%check -a
# Compile the public user package without running its privileged test setup.
go build %{go_import_path}/user

%files
%doc README.md
%license LICENSE-MPL.txt user/crypt/LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
