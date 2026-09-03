# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           clipboard
%define go_import_path  github.com/atotto/clipboard

Name:           go-github-atotto-clipboard
Version:        0.1.4
Release:        %autorelease
Summary:        clipboard for golang
License:        BSD-3-Clause
URL:            https://github.com/atotto/clipboard
#!RemoteAsset:  sha256:cafd64dc78f293c1e774386186f3f817461a1a8940ef86d5d9e9524b58aa791e
Source0:        https://github.com/atotto/clipboard/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/atotto/clipboard) = %{version}

%description
clipboard provides cross-platform clipboard copy/paste access for Go (using xsel/xclip on Linux).

%check
# Compile every package and its tests before tolerating integration failures.
%buildsystem_golangmodules_check -run '^$'
# Clipboard integration tests require xsel/xclip and a graphical clipboard
# session, which are unavailable in the isolated OBS build environment.
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
