# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           slog-shim
%define go_import_path  github.com/sagikazarmark/slog-shim

Name:           go-github-sagikazarmark-slog-shim
Version:        0.1.0
Release:        %autorelease
Summary:        Compatibility shim for Go structured logging
License:        BSD-3-Clause
URL:            https://github.com/sagikazarmark/slog-shim
#!RemoteAsset:  sha256:a594ec7e138265768a5c23f8ab460724d8215db45dc1bddde4743bca3373803d
Source0:        https://github.com/sagikazarmark/slog-shim/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n slog-shim-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/exp)

Provides:       go(github.com/sagikazarmark/slog-shim) = %{version}

Requires:       go(golang.org/x/exp)

%description
Compatibility shim for Go structured logging.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
